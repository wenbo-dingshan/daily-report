import re
import markdown

def parse_txt_to_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Initialize the HTML structure
    html_output = """
    <table style="margin-left:auto; margin-right:auto;">
      <tr>
        <th>日期</th>
        <th>时间</th>
        <th>货币</th>
        <th>活动</th>
        <th>今值</th>
        <th>预测值</th>
        <th>前值</th>
      </tr>
    """

    # Variables to hold data while parsing
    current_date = ""

    for line in lines:
        line = line.strip()  # Remove leading/trailing whitespaces

        # Match the date format (e.g., 2024年12月1日 星期日)
        date_match = re.match(r"(\d{4}年\d{1,2}月\d{1,2}日)\s+(\S+)$", line)
        if date_match:
            current_date = f"{date_match.group(1)} {date_match.group(2)}"
            continue

        # Match the event line (e.g., 08:00 KRW 韩国出口额年率(%) (同比) (十一月) 1.4% 4.6%)
        event_match = re.match(r"(\d{2}:\d{2})\s+(\S+)\s+(.+)\s+([\d\.%B]+)\s+([\d\.%B]+)(\s+([\d\.%B]+))?", line)
        if event_match:
            time = event_match.group(1)
            currency = event_match.group(2)
            event = event_match.group(3)
            actual = event_match.group(4)
            forecast = event_match.group(5)
            previous = event_match.group(7) if event_match.group(7) else ""

            # Add data row to HTML
            html_output += f"""
            <tr>
                <td>{current_date}</td>
                <td>{time}</td>
                <td>{currency}</td>
                <td>{event}</td>
                <td>{actual}</td>
                <td>{forecast}</td>
                <td>{previous}</td>
            </tr>
            """

    # Close the table tag
    html_output += "</table>"
    # print(html_output)
    return html_output


def update_second_table(md_path, txt_path):
    """
    替换 Markdown 文件中的第二个 <table> 部分。
    """
    try:
        # 解析 TXT 文件内容为 HTML 表格
        new_table = parse_txt_to_html(txt_path)

        # 读取 Markdown 文件
        with open(md_path, "r", encoding="utf-8") as file:
            content = file.read()

        # 匹配所有 <table> 标签
        table_matches = list(re.finditer(r"<table.*?</table>", content, flags=re.DOTALL))

        if len(table_matches) >= 3:
            # 获取第二个表格的位置
            second_table = table_matches[2]
            updated_content = (
                content[:second_table.start()]
                + new_table
                + content[second_table.end():]
            )

            # print(updated_content)
            # 保存更新后的内容到新文件
            output_path = "投资参考报告.md"
            with open(output_path, "w", encoding="utf-8") as file:
                file.write(updated_content)

            print(f"第二个表格已更新，保存为 {output_path}")
        else:
            print("未找到第二个表格，无法进行替换。")

    except Exception as e:
        print(f"更新失败: {e}")


def md_to_html(md_path, output_html_path):
    """
    将 Markdown 文件转换为 HTML 并保存，并在 HTML 中添加 headers 保证支持中文。
    """
    try:
        # 读取 Markdown 文件，确保使用 utf-8 编码
        with open(md_path, "r", encoding="utf-8") as md_file:
            md_content = md_file.read()

        # 使用 markdown 库将 Markdown 内容转换为 HTML
        html_content = markdown.markdown(md_content)

        # 添加 HTML headers 确保中文支持
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

        # 将转换后的 HTML 保存到文件，确保使用 utf-8 编码
        with open(output_html_path, "w", encoding="utf-8") as html_file:
            html_file.write(html_content_with_headers)

        print(f"Markdown 文件已成功转换为 HTML，保存为 {output_html_path}")

    except Exception as e:
        print(f"转换失败: {e}")

# # 示例调用
update_second_table("../投资参考报告_template.md", "../data/本周重要宏观事件.txt")
md_to_html("./投资参考报告.md", "../投资参考报告.html")