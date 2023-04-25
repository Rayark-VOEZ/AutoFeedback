import json
import os.path
import sys

from PySide6.QtCore import Slot, QThread, Signal, Qt
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox

from AutoFeedback import Ui_AutoFeedback
from Browser import Browser


class Main(QWidget):
    FEEDBACK_START = Signal()

    def __init__(self):
        super().__init__()
        self.ui = Ui_AutoFeedback()
        self.ui.setupUi(self)

        self.thread = QThread()

        self.state_label = self.ui.stateLabel
        self.usernameEdit = self.ui.usernameEdit
        self.passwordEdit = self.ui.passwordEdit
        self.__suggestionEdit = self.ui.suggestionEdit
        self.__aCheck = self.ui.ACheck
        self.__bCheck = self.ui.BCheck
        self.__cCheck = self.ui.CCheck
        self.__dCheck = self.ui.DCheck
        self.__rememberCheck = self.ui.rememberCheck
        self.__anonymityCheck = self.ui.anonymityCheck
        self.__submitButton = self.ui.submitButton
        self.userinfo_group = self.ui.userinfoGroup
        self.level_group = self.ui.levelGroup
        self.suggestion_group = self.ui.suggestionGroup

        self.__aCheck.clicked.connect(self.__on_aCheck_clicked)
        self.__bCheck.clicked.connect(self.__on_bCheck_clicked)
        self.__cCheck.clicked.connect(self.__on_cCheck_clicked)
        self.__dCheck.clicked.connect(self.__on_dCheck_clicked)
        self.__submitButton.clicked.connect(self.__on_submitButton_clicked)

        self.__load_config()

        self.__level_range = set()

    def __load_config(self):
        if os.path.isfile("userinfo.json"):
            config = json.load(open("userinfo.json", encoding="utf-8"))
            self.usernameEdit.setText(config.get("username"))
            self.passwordEdit.setText(config.get("password"))
            self.__rememberCheck.setChecked(config.get("isRemember"))

    @Slot()
    def __on_submitButton_clicked(self):

        if not (self.__aCheck.isChecked() or self.__bCheck.isChecked() or self.__cCheck.isChecked() or self.__dCheck.isChecked()):
            if QMessageBox.warning(self, "警告", "掌握程度不能为空！", QMessageBox.Ok) == QMessageBox.Ok:
                return

        self.__submitButton.setEnabled(False)
        self.userinfo_group.setEnabled(False)
        self.level_group.setEnabled(False)
        self.suggestion_group.setEnabled(False)

        self.__submitButton.setText("正在执行...")

        # 通过判断rememberCheck的状态来决定是否将账号密码写入userinfo.json
        if self.__rememberCheck.isChecked():
            # 将账号密码写入userinfo.json
            json.dump(
                {"username": self.usernameEdit.text(), "password": self.passwordEdit.text(), "isRemember": True},
                open("userinfo.json", "w", encoding="utf-8"))
        else:
            # 移除userinfo.json
            if os.path.isfile("userinfo.json"):
                os.remove("userinfo.json")

        __username = self.usernameEdit.text()
        __password = self.passwordEdit.text()
        __suggestion = self.__suggestionEdit.toPlainText()
        __isAnonymous = self.__anonymityCheck.isChecked()

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
    window.setWindowFlags(window.windowFlags() | Qt.WindowStaysOnTopHint)
    window.show()

    sys.exit(app.exec())
