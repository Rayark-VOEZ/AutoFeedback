import json
import os.path


class Config:
    __config = {
        "webdriver_cache_day": 7,
        "display_browser": False,
        "user_info": {
            "username": '',
            "password": '',
            "isRemember": False
        }
    }

    def __init__(self):
        self.load_config()

    def init_config(self) -> None:
        """
        初始化配置文件
        :return:
        """
        with open("config.json", "w", encoding="utf-8") as file:
            json.dump(self.__config, file)

    def save_config(self) -> None:
        """
        保存配置文件
        :param setting:
        :return: None
        """
        if not os.path.isfile("config.json"):
            # 如果不存在config.json，则创建一个
            self.init_config()
        with open("config.json", "w", encoding="utf-8") as file:
            json.dump(self.__config, file)

    def load_config(self):
        """
        加载配置文件
        :return:
        """
        if not os.path.isfile("config.json"):
            # 如果不存在config.json，则创建一个
            self.init_config()

        self.__config = json.load(open("config.json", encoding="utf-8"))

    def get_webdriver_cache_day(self) -> int:
        """
        加载缓存天数
        :return: str - 缓存天数
        """
        return self.__config.get("webdriver_cache_day")

    def set_webdriver_cache_day(self, day: int) -> None:
        """
        设置缓存天数
        :param day:
        :return:
        """
        self.__config["webdriver_cache_day"] = day

    def get_display_browser(self) -> str:
        """
        加载是否显示浏览器
        :return: True or False
        """
        return self.__config.get("display_browser")

    def set_display_browser(self, display: bool) -> None:
        """
        设置是否显示浏览器
        :param display:
        :return:
        """
        self.__config["display_browser"] = display

    def get_user_info(self) -> dict:
        """
        加载用户信息
        :return:
        """
        return self.__config.get("user_info")

    def set_user_info(self, username, password, is_remember):
        """
        设置用户信息
        :return:
        """
        self.__config["user_info"] = {"username": username, "password": password, "isRemember": is_remember}


