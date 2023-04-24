import random

from PySide6.QtCore import QObject, Signal, Slot
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Browser(QObject):
    FEEDBACK_PROGRESS = Signal(str)
    FEEDBACK_COMPLETE = Signal()
    FEEDBACK_ERROR = Signal(str)
    FEEDBACK_WARNING = Signal()

    def __init__(self, username: str, password: str, level_range: list, suggestion: str, isAnonymous: bool):
        """

        :param username: 用户名
        :param password: 密码
        :param suggestion: 意见或建议
        :param isAnonymous: 是否匿名评论
        """
        super().__init__()
        self.__username = username
        self.__password = password
        self.__level_range = level_range
        self.__suggestion = suggestion
        self.__isAnonymous = isAnonymous
        self.__random = random.Random()

        """ 配置驱动 """
        self.service = Service("msedgedriver.exe")
        self.options = webdriver.EdgeOptions()
        self.options.add_argument("--headless")
        self.options.add_experimental_option("excludeSwitches", ["enable-logging"])

        """ 配置浏览器 """
        self.driver = webdriver.Edge(service=self.service, options=self.options)
        # self.driver = webdriver.Edge(service=self.service)
        # self.driver.set_window_size(960, 480)

        """ 配置等待器 """
        self.wait = WebDriverWait(self.driver, 10)

    @Slot()
    def feedback_main(self) -> None:
        """
        反馈主函数
        :return: None
        """

        """ 进入登录页面 """
        self.FEEDBACK_PROGRESS.emit("正在进入登录页面...")
        self.driver.get("https://tlias-stu.boxuegu.com/login")

        # 等待元素加载完成
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, '/html/body/div/div/div[1]/div[2]/div[2]/div[1]/div/input')))
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, '/html/body/div/div/div[1]/div[2]/div[2]/div[2]/div/input')))
            self.wait.until(EC.visibility_of_element_located(
                (By.XPATH, '/html/body/div/div/div[1]/div[2]/button')))
        except Exception:
            self.driver.close()
            self.FEEDBACK_ERROR.emit("登录页面加载失败！")
        else:
            self.FEEDBACK_PROGRESS.emit("正在登录...")
            username_input = self.driver.find_element(By.XPATH,
                                                      '/html/body/div/div/div[1]/div[2]/div[2]/div[1]/div/input')
            password_input = self.driver.find_element(By.XPATH,
                                                      '/html/body/div/div/div[1]/div[2]/div[2]/div[2]/div/input')
            login_button = self.driver.find_element(By.XPATH, '/html/body/div/div/div[1]/div[2]/button')

            username_input.send_keys(self.__username + Keys.ENTER)
            password_input.send_keys(self.__password + Keys.ENTER)
            login_button.click()

        """ 进入主页 """
        try:
            # 等待元素加载完成
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH,
                     '/html/body/div[1]/div/section/section/div/div[1]/div/div/div[1]/div[3]/div[2]/div[1]/div[2]/div[2]/div[4]/div')))
        except Exception:
            self.driver.close()
            self.FEEDBACK_ERROR.emit("用户名密码错误 或 主页加载失败！")
        else:
            self.FEEDBACK_PROGRESS.emit("正在打开每日反馈页面...")
            feedback = self.driver.find_element(By.XPATH,
                                                '/html/body/div[1]/div/section/section/div/div[1]/div/div/div[1]/div[2]/div[2]/div[3]/div')
            if "disabled" in feedback.get_attribute("class"):
                self.driver.close()
                self.FEEDBACK_WARNING.emit()
            else:
                feedback.click()

        # TODO:打开反馈表单之前可能会有弹窗，需要判断，如果有弹窗则点击按钮关闭弹窗

        """ 打开反馈表单 """
        try:
            # 等待元素加载完成
            self.wait.until(EC.visibility_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/section/section/div/div[1]/div/div/div[1]/div[2]/div[1]/div[2]/div[2]/button')))
        except Exception:
            self.driver.close()
            self.FEEDBACK_ERROR.emit("每日反馈页面加载失败！")
        else:
            items = self.driver.find_element(By.XPATH,
                                             '/html/body/div[1]/div/section/section/div/div[1]/div/div/div[1]/div[2]/div[1]/div[2]/div[2]/button')
            if items.text == "开始反馈":
                items.click()
                self.FEEDBACK_PROGRESS.emit("正在打开反馈表单...")
            elif items.text == "查看详情":
                self.driver.close()
                self.FEEDBACK_WARNING.emit()

        """ 填写反馈表单 """
        # 等待元素加载完成
        try:
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'question-list')))
        except Exception:
            self.driver.close()
            self.FEEDBACK_ERROR.emit("反馈表单加载失败！")
        else:
            self.FEEDBACK_PROGRESS.emit("正在填写反馈表单...")
            radio_groups = self.driver.find_elements(By.CLASS_NAME, 'el-radio-group')
            for radio_group in radio_groups:
                # radio_group.find_elements(By.CLASS_NAME, 'el-radio')[1].click()
                radio_group.find_elements(By.CLASS_NAME, 'el-radio')[self.__random.choice(self.__level_range)].click()
            textarea = self.driver.find_element(By.TAG_NAME, 'textarea')
            textarea.send_keys(self.__suggestion)
            if self.__isAnonymous:
                self.driver.find_element(By.CLASS_NAME, 'el-checkbox').click()

        """ 提交反馈表单 """
        try:
            pass
            # 等待元素加载完成
            # self.wait.until(EC.visibility_of_element_located((By.XPATH,
            #                                                   '/html/body/div[1]/div/section/section/div/div[1]/div/div/div[1]/div[2]/div[1]/div/div/div[2]/div[16]/div[3]/button')))
        except Exception:
            self.driver.close()
            self.FEEDBACK_ERROR.emit("反馈表单提交失败！")
        else:
            self.FEEDBACK_PROGRESS.emit("正在提交反馈表单...")

            button = self.driver.find_element(By.CLASS_NAME, 'ml20')
            button.click()

            # buttons = self.driver.find_elements(By.CLASS_NAME, 'el-button')
            # button = buttons[len(buttons) - 1]
            # button.click()

            # submit_button = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/section/section/div/div[1]/div/div/div[1]/div[2]/div[1]/div/div/div[2]/div[16]/div[3]/button')
            # submit_button = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/section/section/div/div[1]/div/div/div[1]/div[2]/div[1]/div/div/div[2]/div[13]/div[3]/button')

            # submit_button.click()

        """ 退出浏览器 """
        self.driver.quit()
        self.FEEDBACK_COMPLETE.emit()
