from telegram import Bot
import asyncio
from utils.parser import get_bot_config


async def send_doc():
    config = get_bot_config("../config/config.ini", section="telegram_bot")
    print("加载的配置信息:", config)

    bot = Bot(token=config["API_TOKEN"])
    chat_id = config["CHAT_ID"]

    try:
        with open("../投资决策参考.md", "rb") as file:
            await bot.send_document(chat_id=chat_id, document=file, caption="这是定时发送的文件")
        print("文件发送成功！")
    except Exception as e:
        print(f"发送文件失败: {e}")

if __name__ == "__main__":
    asyncio.run(send_doc())
