from agents import Agent, Runner, function_tool
from main import config
from dotenv import load_dotenv
import os
import requests

load_dotenv()
weather_api_key=os.getenv("WEATHER_API_KEY")
weather_api_base_url=os.getenv("BASE_URL")

@function_tool
def usd_to_pkr():
    return "Today USD to PKR is 285."

@function_tool
def get_weather(city: str) -> str:
    response=requests.get(f"{weather_api_base_url}?key={weather_api_key}&q={city}")
    data=response.json()
    return f"The current weather in {city} is {data['current']['temp_c']}C with {data['current']['condition']['text']}."

agent = Agent(
    name="General Agent",
    instructions="You are a helpful assisstant. Your task is to help the user with their queries.",
    tools=[usd_to_pkr, get_weather]
)

result = Runner.run_sync(
    agent,
    'What is the current weather in Karachi today?',
    run_config=config
)

print(result.final_output)