from typing import List, Union, Generator
from schemas import OpenAIChatMessage


def get_response(
    user_message: str, messages: List[OpenAIChatMessage]
) -> Union[str, Generator]:
    # This is where you can add your custom pipelines like RAG.

    print(messages)
    print(user_message)

    return f"pipeline response to: {user_message}"


async def on_startup():
    # This function is called when the server is started.
    print("onstartup")
    print(__name__)

    pass


async def on_shutdown():
    # This function is called when the server is stopped.
    pass
