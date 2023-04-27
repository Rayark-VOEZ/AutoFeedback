import sys

from PySide6.QtCore import Slot, QThread, Signal, Qt
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox

from auto_feedback import Ui_AutoFeedback
from browser import Browser
from config import Config

VERSION = "v2.3"


class Main(QWidget):
    FEEDBACK_START = Signal()

    def __init__(self):
        super().__init__()
        self.ui = Ui_AutoFeedback()
        self.ui.setupUi(self)

        self.thread = QThread()
        self.config = Config()

        self.state_label = self.ui.stateLabel
        self.username_edit = self.ui.usernameEdit
        self.password_edit = self.ui.passwordEdit
        self.__suggestionEdit = self.ui.suggestionEdit
        self.a_check = self.ui.ACheck
        self.b_check = self.ui.BCheck
        self.c_check = self.ui.CCheck
        self.d_check = self.ui.DCheck
        self.remember_check = self.ui.rememberCheck
        self.anonymity_check = self.ui.anonymityCheck
        self.display_check = self.ui.displayCheck
        self.cache_spin = self.ui.cacheSpin
        self.submit_button = self.ui.submitButton
        self.userinfo_group = self.ui.userinfoGroup
        self.level_group = self.ui.levelGroup
        self.suggestion_group = self.ui.suggestionGroup
        self.setting_group = self.ui.settingGroup

        self.a_check.clicked.connect(self.__on_aCheck_clicked)
        self.b_check.clicked.connect(self.__on_bCheck_clicked)
        self.c_check.clicked.connect(self.__on_cCheck_clicked)
        self.d_check.clicked.connect(self.__on_dCheck_clicked)
        self.submit_button.clicked.connect(self.__on_submitButton_clicked)

        self.__level_range = set()

        # 初始化页面内容
        self.cache_spin.setValue(self.config.get_webdriver_cache_day())
        self.display_check.setChecked(self.config.get_display_browser())
        userinfo = self.config.get_user_info()
        self.username_edit.setText(userinfo.get("username"))
        self.password_edit.setText(userinfo.get("password"))
        self.remember_check.setChecked(userinfo.get("isRemember"))
        self.__suggestionEdit.setText(f"-- Submit by AutoFeedback {VERSION}")


    @Slot()
    def __on_submitButton_clicked(self):

        if not (
                self.a_check.isChecked() or self.b_check.isChecked() or self.c_check.isChecked() or self.d_check.isChecked()):
            if QMessageBox.warning(self, "警告", "掌握程度不能为空！", QMessageBox.Ok) == QMessageBox.Ok:
                return

        self.submit_button.setEnabled(False)
        self.userinfo_group.setEnabled(False)
        self.level_group.setEnabled(False)
        self.suggestion_group.setEnabled(False)
        self.setting_group.setEnabled(False)

        self.submit_button.setText("正在执行...")

        # 通过判断rememberCheck的状态来决定是否将账号密码写入userinfo.json
        if self.remember_check.isChecked():
            # 将账号密码写入userinfo.json
            # json.dump(
            #     {"username": self.username_edit.text(), "password": self.password_edit.text(), "isRemember": True},
            #     open("userinfo.json", "w", encoding="utf-8"))
            # todo: 优化
            self.config.set_user_info(self.username_edit.text(), self.password_edit.text(), True)
        else:
            # 移除userinfo.json
            # if os.path.isfile("userinfo.json"):
            #     os.remove("userinfo.json")
            self.config.set_user_info("", "", False)
        self.config.set_webdriver_cache_day(self.cache_spin.value())
        self.config.set_display_browser(self.display_check.isChecked())
        self.config.save_config()

        __username = self.username_edit.text()
        __password = self.password_edit.text()
        __suggestion = self.__suggestionEdit.toPlainText()
        __isAnonymous = self.anonymity_check.isChecked()

        self.browser = Browser(__username, __password, list(self.__level_range), __suggestion, __isAnonymous)
        self.browser.moveToThread(self.thread)
        self.browser.FEEDBACK_PROGRESS.connect(self.__on_feedback_progress)
        self.browser.FEEDBACK_COMPLETE.connect(self.__on_feedback_completed)
        self.browser.FEEDBACK_WARNING.connect(self.__on_feedback_warning)
        self.browser.FEEDBACK_ERROR.connect(self.__on_feedback_error)
        self.FEEDBACK_START.connect(self.browser.feedback_main)
        self.thread.start()
        self.FEEDBACK_START.emit()

    @Slot()
    def __on_aCheck_clicked(self, state):
        if state:
            self.__level_range.add(0)
        else:
            self.__level_range.remove(0)

    @Slot()
    def __on_bCheck_clicked(self, state):
        if state:
            self.__level_range.add(1)
        else:
            self.__level_range.remove(1)

    @Slot()
    def __on_cCheck_clicked(self, state):
        if state:
            self.__level_range.add(2)
        else:
            self.__level_range.remove(2)

    @Slot()
    def __on_dCheck_clicked(self, state):
        if state:
            self.__level_range.add(3)
        else:
            self.__level_range.remove(3)

    @Slot()
    def __on_feedback_progress(self, message: str):
        self.state_label.setText(message)

    @Slot()
    def __on_feedback_completed(self):
        reply = QMessageBox.information(self, "提示", "提交成功！点击确定退出软件。", QMessageBox.Ok)
        if reply == QMessageBox.Ok:
            self.thread.terminate()
            sys.stdout.close()
            sys.exit()

    @Slot()
    def __on_feedback_warning(self):
        reply = QMessageBox.warning(self, "警告", "反馈还未开始或今日已反馈！点击确定退出软件。", QMessageBox.Ok)
        if reply == QMessageBox.Ok:
            self.thread.terminate()
            sys.stdout.close()
            sys.exit()

    @Slot()
    def __on_feedback_error(self, message: str):
        reply = QMessageBox.critical(self, "错误", f"{message}点击确定退出软件。", QMessageBox.Ok)
        if reply == QMessageBox.Ok:
            self.thread.terminate()
            sys.stdout.close()
            sys.exit()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Main()
    # window.setWindowFlags(window.windowFlags() | Qt.WindowStaysOnTopHint)
    window.setWindowTitle(f"AutoFeedback {VERSION}")
    window.show()

    sys.exit(app.exec())
