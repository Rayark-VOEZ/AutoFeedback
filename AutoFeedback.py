# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AutoFeedback.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGroupBox, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTextEdit,
    QWidget)

class Ui_AutoFeedback(object):
    def setupUi(self, AutoFeedback):
        if not AutoFeedback.objectName():
            AutoFeedback.setObjectName(u"AutoFeedback")
        AutoFeedback.resize(400, 480)
        self.submitButton = QPushButton(AutoFeedback)
        self.submitButton.setObjectName(u"submitButton")
        self.submitButton.setGeometry(QRect(160, 440, 80, 30))
        self.userinfoGroup = QGroupBox(AutoFeedback)
        self.userinfoGroup.setObjectName(u"userinfoGroup")
        self.userinfoGroup.setGeometry(QRect(20, 140, 360, 110))
        self.ACheck = QCheckBox(self.userinfoGroup)
        self.ACheck.setObjectName(u"ACheck")
        self.ACheck.setGeometry(QRect(10, 20, 150, 20))
        self.BCheck = QCheckBox(self.userinfoGroup)
        self.BCheck.setObjectName(u"BCheck")
        self.BCheck.setGeometry(QRect(190, 20, 150, 20))
        self.CCheck = QCheckBox(self.userinfoGroup)
        self.CCheck.setObjectName(u"CCheck")
        self.CCheck.setGeometry(QRect(10, 50, 150, 20))
        self.DCheck = QCheckBox(self.userinfoGroup)
        self.DCheck.setObjectName(u"DCheck")
        self.DCheck.setGeometry(QRect(190, 50, 150, 20))
        self.suggestionGroup = QGroupBox(AutoFeedback)
        self.suggestionGroup.setObjectName(u"suggestionGroup")
        self.suggestionGroup.setGeometry(QRect(20, 260, 360, 140))
        self.suggestionEdit = QTextEdit(self.suggestionGroup)
        self.suggestionEdit.setObjectName(u"suggestionEdit")
        self.suggestionEdit.setGeometry(QRect(10, 30, 340, 70))
        self.anonymityCheck = QCheckBox(self.suggestionGroup)
        self.anonymityCheck.setObjectName(u"anonymityCheck")
        self.anonymityCheck.setGeometry(QRect(10, 110, 79, 20))
        self.levelGroup = QGroupBox(AutoFeedback)
        self.levelGroup.setObjectName(u"levelGroup")
        self.levelGroup.setEnabled(True)
        self.levelGroup.setGeometry(QRect(20, 20, 360, 110))
        self.usernameLabel = QLabel(self.levelGroup)
        self.usernameLabel.setObjectName(u"usernameLabel")
        self.usernameLabel.setGeometry(QRect(10, 20, 50, 20))
        self.passwordLabel = QLabel(self.levelGroup)
        self.passwordLabel.setObjectName(u"passwordLabel")
        self.passwordLabel.setGeometry(QRect(10, 50, 50, 20))
        self.rememberCheck = QCheckBox(self.levelGroup)
        self.rememberCheck.setObjectName(u"rememberCheck")
        self.rememberCheck.setGeometry(QRect(10, 80, 100, 20))
        self.usernameEdit = QLineEdit(self.levelGroup)
        self.usernameEdit.setObjectName(u"usernameEdit")
        self.usernameEdit.setGeometry(QRect(70, 20, 280, 20))
        self.passwordEdit = QLineEdit(self.levelGroup)
        self.passwordEdit.setObjectName(u"passwordEdit")
        self.passwordEdit.setGeometry(QRect(70, 50, 280, 20))
        self.passwordEdit.setEchoMode(QLineEdit.Password)
        self.stateLabel = QLabel(AutoFeedback)
        self.stateLabel.setObjectName(u"stateLabel")
        self.stateLabel.setGeometry(QRect(20, 410, 360, 20))

        self.retranslateUi(AutoFeedback)

        QMetaObject.connectSlotsByName(AutoFeedback)
    # setupUi

    def retranslateUi(self, AutoFeedback):
        AutoFeedback.setWindowTitle(QCoreApplication.translate("AutoFeedback", u"AutoFeedBack", None))
        self.submitButton.setText(QCoreApplication.translate("AutoFeedback", u"\u81ea\u52a8\u53cd\u9988", None))
        self.userinfoGroup.setTitle(QCoreApplication.translate("AutoFeedback", u"\u638c\u63e1\u7a0b\u5ea6", None))
        self.ACheck.setText(QCoreApplication.translate("AutoFeedback", u"\u975e\u5e38\u6e05\u695a\uff0890%\u4ee5\u4e0a\uff09", None))
        self.BCheck.setText(QCoreApplication.translate("AutoFeedback", u"\u57fa\u672c\u6e05\u695a\uff0870%~90%\uff09\uff09", None))
        self.CCheck.setText(QCoreApplication.translate("AutoFeedback", u"\u6709\u70b9\u6a21\u7cca\uff0850%~70%\uff09", None))
        self.DCheck.setText(QCoreApplication.translate("AutoFeedback", u"\u57fa\u672c\u4e0d\u61c2\uff0850%\u4ee5\u4e0b\uff09", None))
        self.suggestionGroup.setTitle(QCoreApplication.translate("AutoFeedback", u"\u5176\u4ed6\u610f\u89c1\u6216\u5efa\u8bae", None))
        self.suggestionEdit.setHtml(QCoreApplication.translate("AutoFeedback", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">--Submit by AutoFeedback. Version 2.0</p></body></html>", None))
        self.anonymityCheck.setText(QCoreApplication.translate("AutoFeedback", u"\u533f\u540d\u53cd\u9988", None))
        self.levelGroup.setTitle(QCoreApplication.translate("AutoFeedback", u"\u7528\u6237\u4fe1\u606f", None))
        self.usernameLabel.setText(QCoreApplication.translate("AutoFeedback", u"\u7528\u6237\u540d", None))
        self.passwordLabel.setText(QCoreApplication.translate("AutoFeedback", u"\u5bc6\u7801", None))
        self.rememberCheck.setText(QCoreApplication.translate("AutoFeedback", u"\u8bb0\u4f4f\u8d26\u53f7\u5bc6\u7801", None))
        self.stateLabel.setText("")
    # retranslateUi

