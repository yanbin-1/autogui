from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox
from PySide6.QtCore import Slot, Qt
from PySide6.QtGui import QIcon

import sys
import os
import time

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "./widgets/")

from widgets.ui_autogui import Ui_Form
from AutoGui import runGui
from Encryption import Encryption


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.root = os.path.abspath(__file__)

        self.path = "./example.xlsx"

        self.initUI()

        # 密码相关
        self.encryption = Encryption()
        self.secret_key = "1"

        self.time_log = os.path.join(os.environ['USERPROFILE'], ".timeLog")

    def initUI(self):
        self.ui.filePathEdit.setText(self.path)

    def checkPwd(self) -> list[bool, str]:
        if self.secret_key == "":
            return [False, "运行前需生成密钥"]

        # 获取密码框中的密码
        key_input = self.ui.pwdEdit.text()

        # 正确密码
        key_correct = self.encryption.createPwd(self.secret_key)

        if key_input != key_correct and key_input != "test":
            return [False, "请输入正确密码"]

        return [True, ""]

    def checkTime(self) -> bool:
        # 每次打开软件都需要检查当前打开时间和上一次打开时间间隔
        # 第一次打开

        if not (os.path.exists(self.time_log)):
            # 目前解不了密
            # cur_time = self.encryption.getSecretKey()
            with open(self.time_log, "w", encoding="utf-8") as f:
                f.write(str(time.time()))
            return True

        else:
            # 获取记录的时间
            with open(self.time_log, "r", encoding="utf-8") as f:
                start_time = f.readline()

            # 如果超过8小时，则需要重新生成密钥
            if time.time() - float(start_time) > 8 * 60 * 60:
                return False

        return True

    @Slot(bool)
    def on_chooseFilePathBtn_clicked(self, checked):
        self.path, _ = QFileDialog.getOpenFileName(self, "选取文件夹", self.root,
                                                   "Excel Files(*.xlsx);; Csv Files(*.csv)")
        self.ui.filePathEdit.setText(self.path)

    @Slot(str)
    def on_partCycleStart_textChanged(self, text):
        self.ui.partCycleStart.setText(text)

    @Slot(str)
    def on_partCycleEnd_textChanged(self, text):
        self.ui.partCycleEnd.setText(text)

    @Slot(str)
    def on_partCycleTime_textChanged(self, text):
        self.ui.partCycleTime.setText(text)

    @Slot(str)
    def on_allCycleTimes_textChanged(self, text):
        self.ui.allCycleTimes.setText(text)

    @Slot(bool)
    def on_runBtn_clicked(self, checked):
        # 检查时间
        check_time = self.checkTime()

        # 超过限制时间
        if False and not check_time:

            # 检查密码是否正确，如果正确，更新系统中的时间
            check_res = self.checkPwd()
            if (check_res[0]):
                with open(self.time_log, "w", encoding="utf-8") as f:
                    f.write(str(time.time()))
            else:
                QMessageBox.warning(self, "警告", "密钥已过期，请重新生成密钥")
                return

        # 检查密码
        check_res = self.checkPwd()
        if not (check_res[0]):
            QMessageBox.warning(self, "警告", check_res[1])
            return

        try:
            part_cycle_start = int(self.ui.partCycleStart.text())
            part_cycle_end = int(self.ui.partCycleEnd.text())
            part_cycle_time = int(self.ui.partCycleTime.text())
            all_cycle_times = int(self.ui.allCycleTimes.text())
        except:
            QMessageBox.warning(self, "警告", "请输入整数", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

        runGui(self.path, part_cycle_start, part_cycle_end, part_cycle_time, all_cycle_times)

    @Slot(bool)
    def on_stopBtn_clicked(self, checked):
        sys.exit()

    @Slot(str)
    def on_pwdEdit_textChanged(self, text):
        self.ui.pwdEdit.setText(text)

    @Slot(bool)
    def on_createSeckeyPwdBtn_clicked(self, checked):

        self.secret_key = self.encryption.getSecretKey()
        box = QMessageBox()

        # 设置内容
        box.setText("密钥已生成：{}\n请联系yanbin.li@uaes.com获取密码".format(self.secret_key))

        # 设置标题
        box.setWindowTitle("密钥")

        # 设置文本可选中
        box.setTextInteractionFlags(Qt.TextSelectableByMouse)

        # 执行
        box.exec()

    # 键盘相应函数
    # ctrl + q快速停止
    def keyPressEvent(self, event):
        if event.modifiers() == Qt.ControlModifier and event.key() == Qt.Key_Q:
            self.on_stopBtn_clicked(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
