import datetime
import re
import markdown

def parse_txt_to_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    html_output = """
<table style="margin-left:auto; margin-right:auto; border-collapse: collapse; width: 80%;">
<tr>
    <th style="text-align: center;">日期</th>
    <th style="text-align: center;">时间</th>
    <th style="text-align: center;">货币</th>
    <th style="text-align: center;">活动</th>
    <th style="text-align: center;">今值</th>
    <th style="text-align: center;">预测值</th>
    <th style="text-align: center;">前值</th>
</tr>
"""

    current_date = ""

    for line in lines:
        line = line.strip()

        # 日期行匹配
        date_match = re.match(r"(\d{4}年\d{1,2}月\d{1,2}日)\s+(\S+)$", line)
        if date_match:
            current_date = f"{date_match.group(1)} {date_match.group(2)}"
            continue

        # 事件行匹配
        # 匹配活动、今值、预测值和前值（如果有的话）
        event_match = re.match(
            r"(\d{2}:\d{2})\s+(\S+)\s+(.+?)\s+([\d\.%]+)\s*(?:([\d\.%]+))?\s*(?:([\d\.%]+))?", line
        )
        if event_match:
            time = event_match.group(1)  # 时间
            currency = event_match.group(2)  # 货币
            event = event_match.group(3)  # 活动
            actual = event_match.group(4) if event_match.group(5) else ""   # 今值
            forecast = event_match.group(5) if event_match.group(5) else ""  # 预测值（如果没有，使用空字符串）
            previous = event_match.group(6) if event_match.group(6) else ""  # 前值（如果没有，使用空字符串）

            # 确保列顺序正确
            html_output += f"""
<tr>
    <td style="text-align: center;">{current_date}</td>
    <td style="text-align: center;">{time}</td>
    <td style="text-align: center;">{currency}</td>
    <td style="text-align: center;">{event}</td>
    <td style="text-align: center;">{actual}</td>
    <td style="text-align: center;">{forecast}</td>
    <td style="text-align: center;">{previous}</td>
</tr>
"""

    html_output += "</table>"
    return html_output


def update_second_table(md_path, txt_path):
    try:
        new_table = parse_txt_to_html(txt_path)
        with open(md_path, "r", encoding="utf-8") as file:
            content = file.read()

        table_matches = list(re.finditer(r"<table.*?</table>", content, flags=re.DOTALL))

        if len(table_matches) >= 3:
            second_table = table_matches[2]
            updated_content = (
                content[:second_table.start()]
                + new_table
                + content[second_table.end():]
            )
            output_path = "投资参考报告.md"
            with open(output_path, "w", encoding="utf-8") as file:
                file.write(updated_content)

            print(f"第二个表格已更新，保存为 {output_path}")
        else:
            print("未找到第二个表格，无法进行替换。")

    except Exception as e:
        print(f"更新失败: {e}")


def md_to_html(md_path, output_html_path):
    try:
        with open(md_path, "r", encoding="utf-8") as md_file:
            md_content = md_file.read()

        html_content = markdown.markdown(md_content)

        html_content_with_headers = f"""
        <!DOCTYPE html>
        <html lang="zh">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Converted Markdown</title>
        </head>
        <body>
            {html_content}
        </body>
        </html>
        """

        with open(output_html_path, "w", encoding="utf-8") as html_file:
            html_file.write(html_content_with_headers)

        print(f"Markdown 文件已成功转换为 HTML，保存为 {output_html_path}")

    except Exception as e:
        print(f"转换失败: {e}")

def update_date_in_markdown(md_path):
    current_date = datetime.now().strftime("%Y 年 %m 月 %d 日 %a")
    weekday_mapping = {
        "Mon": "星期一",
        "Tue": "星期二",
        "Wed": "星期三",
        "Thu": "星期四",
        "Fri": "星期五",
        "Sat": "星期六",
        "Sun": "星期天"
    }
    current_date = current_date.replace(current_date.split()[-1], weekday_mapping[current_date.split()[-1]])
    try:
        with open(md_path, "r", encoding="utf-8") as file:
            content = file.read()
        date_pattern = re.compile(r"\d{4} 年 \d{1,2} 月 \d{1,2} 日 星期[一二三四五六日]")
        updated_content = date_pattern.sub(current_date, content)

        with open("投资参考报告.md", "w", encoding="utf-8") as file:
            file.write(updated_content)
        print(f"Markdown 文件已更新，保存为 {"投资参考报告.md"}")

    except Exception as e:
        print(f"更新失败: {e}")