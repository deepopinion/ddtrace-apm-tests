from ddtrace import patch_all
patch_all()

import asyncio

from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI


def check_openai_sync() -> None:
    model = ChatOpenAI(model="gpt-3.5-turbo")
    message = model.invoke([HumanMessage(content="Hi! I'm sync Bob")])
    print(message)


async def check_openai_async() -> None:
    model = ChatOpenAI(model="gpt-3.5-turbo")
    message = await model.ainvoke([HumanMessage(content="Hi! I'm async Bob")])
    print(message)


def main() -> None:
    check_openai_sync()
    asyncio.run(check_openai_async())


if __name__ == '__main__':
    main()
