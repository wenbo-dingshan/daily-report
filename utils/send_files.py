import os
import zipfile
import asyncio
from telegram import Bot
from utils.parser import get_bot_config


def zip_files(md_path, html_path, folder_path, zip_name):
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(md_path, os.path.basename(md_path))
        zipf.write(html_path, os.path.basename(html_path))
        for root, _, files in os.walk(folder_path):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                arcname = os.path.relpath(file_path, start=os.path.dirname(folder_path))
                zipf.write(file_path, arcname=arcname)

        print(f"文件已成功打包为 {zip_name}")

async def send_files():
    config = get_bot_config("./config/config.ini", section="telegram_bot")
    print("加载的配置信息:", config)

    bot = Bot(token=config["API_TOKEN"])
    chat_id = config["CHAT_ID"]

    try:
        # 打包文件
        zip_name = "投资参考报告.zip"
        md_path = "./投资参考报告.md"
        html_path = "./投资参考报告.html"
        folder_path = "./screenshots"
        zip_files(md_path, html_path, folder_path, zip_name)

        with open(zip_name, "rb") as zip_file:
            await bot.send_document(chat_id=chat_id, document=zip_file, caption="定时发送的 Markdown 文件、HTML 文件和图片")
        print(f"ZIP 文件 {zip_name} 发送成功！")

    except Exception as e:
        print(f"发送文件失败: {e}")