import configparser
from functools import lru_cache
import os


@lru_cache(maxsize=1)
def get_login_credentials(config_path="./config/config.ini", section="glass_node_login"):
    config = configparser.ConfigParser()
    try:
        config_path = os.path.abspath(config_path)
        print(f"配置文件路径: {config_path}")

        if not os.path.exists(config_path):
            raise FileNotFoundError(f"配置文件未找到: {config_path}")

        if not config.read(config_path, encoding='utf-8'):
            raise ValueError(f"配置文件无法读取: {config_path}")

        if section not in config:
            raise KeyError(f"配置文件中未找到 Section: {section}")

        username = config[section].get("username")
        password = config[section].get("password")

        if not username or not password:
            raise KeyError(f"Section '{section}' 中缺少 'username' 或 'password'")

        return username, password

    except Exception as e:
        raise RuntimeError(f"加载配置文件失败: {e}")



def get_bot_config(config_path="./config/config.ini", section="telegram_bot"):
    config = configparser.ConfigParser()
    try:
        config_path = os.path.abspath(config_path)
        print(f"配置文件路径: {config_path}")

        if not os.path.exists(config_path):
            raise FileNotFoundError(f"配置文件未找到: {config_path}")

        if not config.read(config_path, encoding="utf-8"):
            raise ValueError(f"配置文件无法读取: {config_path}")

        if section not in config:
            raise KeyError(f"配置文件中未找到 Section: {section}")

        api_token = config[section].get("API_TOKEN")
        chat_id = config[section].get("CHAT_ID")
        # file_path = config[section].get("FILE_PATH")

        if not api_token or not chat_id:
            raise KeyError(f"Section '{section}' 中缺少 'API_TOKEN'、'CHAT_ID'")

        return {
            "API_TOKEN": api_token,
            "CHAT_ID": chat_id
            # "FILE_PATH": file_path,
        }

    except Exception as e:
        raise RuntimeError(f"加载配置文件失败: {e}")