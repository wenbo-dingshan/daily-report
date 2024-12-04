import asyncio
import json
import schedule
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from spiders.spider import Spider
from utils.update_files import *
from utils.send_files import send_files


def load_config(config_path):
    with open(config_path, "r", encoding="utf-8") as f:
        return json.load(f)


def run_spider_task(task):
    print(f"开始任务: {task['name']}")
    spider = Spider(task)
    spider.run()
    print(f"完成任务: {task['name']}")


def main():
    try:
        config = load_config("./config/config.json")
        tasks = config["tasks"]

        glassnode_tasks = [task for task in tasks if task.get("custom_handler") == "glassnode_handler"]
        macro_event_task = [task for task in tasks if task.get("custom_handler") == "macro_event_handler"]

        other_tasks = [task for task in tasks if task.get("custom_handler") != "glassnode_handler" and task.get("custom_handler") != "macro_event_handler"]

        with ThreadPoolExecutor() as executor:
            futures = [executor.submit(run_spider_task, task) for task in other_tasks]
            for future in as_completed(futures):
                try:
                    future.result()
                except Exception as e:
                    print(f"任务执行失败: {e}")

        for task in glassnode_tasks:
            try:
                run_spider_task(task)
            except Exception as e:
                print(f"GlassNode 任务执行失败: {e}")

        run_spider_task(macro_event_task[0])
        update_second_table("./投资参考报告_template.md", "./data/本周重要宏观事件.txt")
        md_to_html("./投资参考报告.md", "./投资参考报告.html")
        asyncio.run(send_files())

    except Exception as e:
        print(f"发生异常: {e}")
        print("重新尝试运行 main 函数...")
        time.sleep(5)
        main()


schedule.every().day.at("16:00").do(main)

if __name__ == "__main__":
    # main()
    while True:
        schedule.run_pending()
        time.sleep(60)