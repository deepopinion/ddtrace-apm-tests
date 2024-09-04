from asgiref.sync import async_to_sync
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI


async def check_openai() -> None:
    model = ChatOpenAI(model="gpt-3.5-turbo")
    message = await model.ainvoke([HumanMessage(content="Hi! I'm Bob")])
    print(message)


def main() -> None:
    async_to_sync(check_openai)()


if __name__ == '__main__':
    main()
