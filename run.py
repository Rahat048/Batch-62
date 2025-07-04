from agents import Agent, OpenAIChatCompletionsModel, Runner, RunConfig, AsyncOpenAI

import asyncio

from dotenv import load_dotenv
import os

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

external_client = AsyncOpenAI(
    api_key = gemini_api_key,
    base_url = "https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model = "gemini-2.0-flash",
    openai_client = external_client,
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True,
)
async def my_fun():
    agent = Agent(
        name = "Assistant",
        instructions = "You are a helpful assistant that can answer questions and help with tasks.",
    )

    result = await Runner.run(
        agent, "capital if india?", run_config=config,
    )

    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(my_fun())