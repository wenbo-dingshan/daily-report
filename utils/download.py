import os
from datetime import datetime


def save_to_file(file_path, content, encoding="utf-8"):
    try:
        with open(file_path, "w", encoding=encoding) as f:
            f.write(content)
        print(f"数据已保存至: {file_path}")
    except Exception as e:
        print(f"保存文件失败: {e}")