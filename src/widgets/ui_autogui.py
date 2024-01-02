# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'autogui.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)
import res_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(387, 296)
        icon = QIcon()
        icon.addFile(u":/res/resource/\u684c\u9762\u81ea\u52a8\u5316.ico", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.chooseFilePathBtn = QPushButton(Form)
        self.chooseFilePathBtn.setObjectName(u"chooseFilePathBtn")

        self.gridLayout.addWidget(self.chooseFilePathBtn, 0, 0, 1, 2)

        self.filePathEdit = QLineEdit(Form)
        self.filePathEdit.setObjectName(u"filePathEdit")

        self.gridLayout.addWidget(self.filePathEdit, 0, 2, 1, 3)

        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.partCycleStart = QLineEdit(self.groupBox)
        self.partCycleStart.setObjectName(u"partCycleStart")

        self.gridLayout_2.addWidget(self.partCycleStart, 0, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 0, 2, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)

        self.partCycleEnd = QLineEdit(self.groupBox)
        self.partCycleEnd.setObjectName(u"partCycleEnd")

        self.gridLayout_2.addWidget(self.partCycleEnd, 1, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 1, 2, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 1)

        self.partCycleTime = QLineEdit(self.groupBox)
        self.partCycleTime.setObjectName(u"partCycleTime")

        self.gridLayout_2.addWidget(self.partCycleTime, 2, 1, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 5)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 2)

        self.allCycleTimes = QLineEdit(Form)
        self.allCycleTimes.setObjectName(u"allCycleTimes")

        self.gridLayout.addWidget(self.allCycleTimes, 2, 2, 1, 3)

        self.pwdEdit = QLineEdit(Form)
        self.pwdEdit.setObjectName(u"pwdEdit")

        self.gridLayout.addWidget(self.pwdEdit, 3, 1, 1, 2)

        self.runBtn = QPushButton(Form)
        self.runBtn.setObjectName(u"runBtn")

        self.gridLayout.addWidget(self.runBtn, 3, 3, 1, 1)

        self.stopBtn = QPushButton(Form)
        self.stopBtn.setObjectName(u"stopBtn")

        self.gridLayout.addWidget(self.stopBtn, 3, 4, 1, 1)

        self.createSeckeyPwdBtn = QPushButton(Form)
        self.createSeckeyPwdBtn.setObjectName(u"createSeckeyPwdBtn")

        self.gridLayout.addWidget(self.createSeckeyPwdBtn, 3, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u684c\u9762\u81ea\u52a8\u5316\u5de5\u5177", None))
        self.chooseFilePathBtn.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u6587\u4ef6", None))
        self.filePathEdit.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u5c40\u90e8\u5faa\u73af\u8bbe\u7f6e", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u5faa\u73af\u5f00\u59cb\u533a\u95f4", None))
        self.partCycleStart.setText(QCoreApplication.translate("Form", u"-1", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u884c", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u5faa\u73af\u7ed3\u675f\u533a\u95f4", None))
        self.partCycleEnd.setText(QCoreApplication.translate("Form", u"-1", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u884c", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u5c40\u90e8\u5faa\u73af\u6b21\u6570", None))
        self.partCycleTime.setText(QCoreApplication.translate("Form", u"-1", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u6574\u4e2a\u6d41\u7a0b\u5faa\u73af\u6b21\u6570", None))
        self.allCycleTimes.setText(QCoreApplication.translate("Form", u"1", None))
        self.pwdEdit.setText("")
        self.pwdEdit.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u5bc6\u7801", None))
        self.runBtn.setText(QCoreApplication.translate("Form", u"\u8fd0\u884c", None))
        self.stopBtn.setText(QCoreApplication.translate("Form", u"\u4e2d\u6b62", None))
        self.createSeckeyPwdBtn.setText(QCoreApplication.translate("Form", u"\u70b9\u51fb\u751f\u6210\u5bc6\u94a5", None))
    # retranslateUi

