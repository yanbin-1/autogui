import pandas as pd
import pyautogui
import time
import pyperclip
import os
import datetime

from typing import Union


def replaceRunNum(string: str, sub_string: str) -> str:
    # 方法字典
    run_num_dict = {
        "$addNum": GetRunNum.addRunNum,
        "$subNum": GetRunNum.subRunNum
    }

    value_ = ""
    left, right = 0, len(sub_string)
    while right < len(string) + 1:
        if string[left: right] == sub_string:
            # 执行相应全局计时器操作
            run_num_dict[sub_string]()

            # 替换
            value_ += str(GetRunNum.getRunNum())

            # 左右指针向前移动
            left = right
            right += right
        else:
            # 原封不动添加
            value_ += string[left]

            # 左右指针向前移动
            left += 1
            right += 1

    # 添加剩余字符串
    value_ += string[left:]

    return value_


class GetRunNum:
    # 全局计数器
    __run_num = 1

    @classmethod
    def addRunNum(cls):
        cls.__run_num += 1

    @classmethod
    def subRunNum(cls):
        cls.__run_num -= 1

    @classmethod
    def getRunNum(cls):
        return cls.__run_num


def myLog(*BUF, log_method=1):
    # 输出到文件
    if log_method == 1:
        with open("./log.txt", "a") as log:
            print(datetime.datetime.now().strftime("%F %T"), file=log, end="\t")
            for i in BUF:
                print(i, file=log, end=" ")
            print("", file=log)

    # 输出到控制台
    elif log_method == 2:
        print(datetime.datetime.now().strftime("%F %T"), end="\t")
        for i in BUF:
            print(i, end=" ")
        print(end="\n")


def readCheckData(path: str) -> pd.DataFrame:
    # 读取数据，返回数据
    df = pd.read_excel(path, header=0)
    return df


def checkParseCommand(source_command: str) -> dict:
    """
    检查所给command格式是否正确并解析
    Args:
        source_command:

    Returns:

    """
    command_dict = {}

    source_command = source_command.replace("，", ",")

    # 格式错误
    if source_command.count(",") + 1 != source_command.count("="):
        myLog("{}有误".format(source_command))
        return command_dict

    # 格式正确 a = 1, b = 2
    # 将间隔符全部替换为"="
    source_command = source_command.replace(",", "=")
    command_list = source_command.split("=")

    # source_command中的奇数元素位命令，偶数元素为参数
    for i in range(0, len(command_list), 2):
        # 去除首位空格
        cur_command = command_list[i].strip()
        cur_param = command_list[i + 1].strip()

        # 存储
        command_dict[cur_command] = cur_param
    return command_dict


def detectImage(img_path, command_value):
    """
    检测屏幕中是否有图片
    Args:
        img_path:
        command_value:

    Returns:

    """
    while True:
        location = pyautogui.locateCenterOnScreen(image=img_path, confidence=0.95)
        if command_value == "出现":
            if location:
                break

        elif command_value == "消失":
            if not location:
                break

        time.sleep(0.1)


def detectFile(command_value, method=1):
    """
    检测文件出现或消失
    Args:
        command_value: 文件路径
            单个文件——C:\Yan\test.txt
            多个文件——C:\Yan\test.txt && C:\Yan\test1.txt && C:\Yan\test2.txt
        method: method=1检测出现，method=2检测消失

    Returns:

    """
    # 根据command_value进行单个文件和多个文件检测
    command_value_split = command_value.split("&&")

    for command_value in command_value_split:

        # 去除首尾空格
        command_value = command_value.strip()

        # 检测文件出现
        if method == 1:
            while not os.path.exists(command_value):
                time.sleep(0.1)

        # 检测文件消失
        elif method == 2:
            while os.path.exists(command_value):
                time.sleep(0.1)


def executeCommand(img_path: str, command_dict: dict, interval: float) -> None:
    """
    根据给的那个参数执行相应逻辑命令
    定位图片中心、移动、偏移、左键、右键、中键、输入、按住、松开、检测（暂定给定图片检测出现和消失的瞬间）、
    打开软件、关闭软件、等待、区间内循环、检测文件是否出现，检测文件是否消失、新建文件夹

    当输入为"$inputNum"，则替换为全局计数器并加1，如果输入"$getNum"，则输入全局计数器
    当"$addNum"和"$subNum"内嵌在语句中，则直接将其替换为相应的全局计数器，如"$getNum123$addNumfbaxx$subNumxx" -> "11232fbaxx1xx"

    检测单个文件——C:\Yan\test.txt
    检测多个文件——C:\Yan\test.txt && C:\Yan\test1.txt && C:\Yan\test2.txt
    Args:
        img_path: 图片路径
        command_dict: 命令参数{命令：参数}
            i.e., {左键：1， 中键：10，右键：-1}
        interval: 每个动作后的等待时间

    Returns:

    """
    # 是否可以移动到图片
    move_flag = True

    for command_key, command_value in command_dict.items():
        if "$getNum" in command_value:
            input_num = str(GetRunNum.getRunNum())
            command_value = command_value.replace("$getNum", input_num)

        # 如果输入全局计数器
        if "$addNum" == command_value:
            GetRunNum.addRunNum()
        # 全局计数器内嵌在语句中，将$addNum替换为相应的数
        elif "$addNum" in command_value:
            command_value = replaceRunNum(command_value, "$addNum")

        if "$subNum" == command_value:
            GetRunNum.subRunNum()
        elif "$subNum" in command_value:
            command_value = replaceRunNum(command_value, "$subNum")

        # show
        myLog("图片：{}，命令：{} {}".format(img_path, command_key, command_value))

        # 有图片路径
        if pd.notna(img_path) and os.path.exists(img_path):
            # 检测
            if command_key == "检测":
                detectImage(img_path, command_value)

            # 定位图片中心并移动
            elif move_flag:
                start = time.time()

                while True:
                    # 获得图片中心位置
                    location = pyautogui.locateCenterOnScreen(image=img_path, confidence=0.95)

                    if location:
                        location_x = location.x
                        location_y = location.y

                        # 移动到图片中心
                        pyautogui.moveTo(location_x, location_y)
                        move_flag = False
                        break

                    if time.time() - start > 10:
                        pyautogui.alert(text=img_path + "查找超时", title="错误")
                        return

                        # 移动（根据像素点移动）
        if command_key == "移动":
            # 获取目标点像素点
            coordinate = command_value.split("/")
            location_x = int(coordinate[0].strip())
            location_y = int(coordinate[1].strip())

            # 移动
            pyautogui.moveTo(location_x, location_y)

        # 偏移(根据像素点偏移)
        elif command_key == "偏移":
            # 获取目标点偏移量
            coordinate = command_value.split("/")
            offset_x = int(coordinate[0].strip())
            offset_y = int(coordinate[1].strip())

            # 偏移
            pyautogui.moveRel(offset_x, offset_y)

        # 按住鼠标
        elif command_key == "按住左键":
            # 获取目标点像素点
            coordinate = command_value.split("/")
            location_x = int(coordinate[0].strip())
            location_y = int(coordinate[1].strip())

            pyautogui.mouseDown(location_x, location_y, "left")

        elif command_key == "鼠标拖动":
            # 获取目标点像素点
            coordinate = command_value.split("/")
            location_x = int(coordinate[0].strip())
            location_y = int(coordinate[1].strip())

            pyautogui.dragTo(100, 300, duration=1)

        elif command_key == "检测文件出现":
            detectFile(command_value)

        elif command_key == "检测文件消失":
            detectFile(command_value, 2)

        elif command_key == "输入":
            # 原本剪切板的内容
            text_backup = pyperclip.paste()

            # 输入内容复制进剪切板
            pyperclip.copy(command_value)

            # 输入
            pyautogui.hotkey("ctrl", "v")
            time.sleep(0.1)
            pyperclip.copy(text_backup)

        elif command_key == "按住":
            pyautogui.keyDown(command_value)

        elif command_key == "松开":
            pyautogui.keyUp(command_value)

        # 左键点击n次
        elif command_key == "左键":
            for _ in range(int(command_value)):
                pyautogui.leftClick()
                time.sleep(0.01)

        # 右键
        elif command_key == "右键":
            for _ in range(int(command_value)):
                pyautogui.rightClick()
                time.sleep(0.01)

        # 中键
        elif command_key == "中键":
            for _ in range(int(command_value)):
                pyautogui.middleClick()
                time.sleep(0.01)

        # 打开软件
        elif command_key == "打开软件":
            # 打开软件的盘符位置
            drive_location = command_value[0]

            # 获取软件根目录和软件名
            split_text = command_value.split("\\")
            root = "\\".join(split_text[:-1])
            name = split_text[-1]

            # 进入盘符位置并打开软件
            os.system("{}: & cd {} & start {}".format(drive_location, root, name))

        # 关闭软件
        elif command_key == "关闭软件":
            os.system("taskkill /f /t /im {}".format(command_value))

        # 等待
        elif command_key == "等待":
            try:
                command_value = float(command_value)
            except:
                pyautogui.alert(text="等待时间请输入数字", title="错误")

            time.sleep(float(command_value))

        # 如果输入新建文件夹
        # 新建文件夹 = C:\yan\1-400
        elif command_key == "新建文件夹":
            value_split = command_value.split("\\")
            root = "\\".join(value_split[:-1])
            names = value_split[-1]
            split_text = names.split("-")
            if len(split_text) != 2:
                pyautogui.alert(text="未指定起始终止文件夹", title="错误")

            try:
                start_name = int(split_text[0])
                end_name = int(split_text[1])
                if end_name < start_name:
                    pyautogui.alert(text="终止文件夹不能小于起始文件夹吧", title="错误")

            except:
                pyautogui.alert(text="起始终止文件夹名称必须为整数", title="错误")

            # 创建文件夹
            [os.mkdir(os.path.join(root, str(name))) for name in range(start_name, end_name + 1)]


        # 等待
        time.sleep(interval)


def runGui(path, part_cycle_start, part_cycle_end, part_cycle_time, all_cycle_times) -> Union[None, str]:
    """
    主程序运行
    Returns:

    """

    for cycle_time in range(1, all_cycle_times + 1):

        myLog("......................开始第{}次循环......................".format(cycle_time))

        # 读取文件
        df = readCheckData(path)

        # 输入的区间是从2开始的，这里减去方便索引
        part_cycle_start -= 2
        part_cycle_end -= 2
        i = 0

        try:
            while i < df.shape[0]:
                # 是否启动该行，当该值为0时不启动，其余情况启动
                enable_flag = df.iloc[i, 1]
                if enable_flag == 0:
                    continue

                # 解析文件列
                img_path = df.iloc[i, 2]  # 图片路劲
                times = 1 if pd.isna(df.iloc[i, 3]) else int(df.iloc[i, 3])  # 运行次数
                timeout_method = df.iloc[i, 4]  # 超时行为
                interval = 0.1 if pd.isna(df.iloc[i, 5]) else df.iloc[i, 5]  # 动作间隔
                source_command = df.iloc[i, 6]  # 执行动作

                # 允许空行
                if pd.isna(source_command) or len(source_command) == 0:
                    continue

                # 检查并解析command格式
                command_dict = checkParseCommand(source_command)

                # 格式不对
                if not command_dict:
                    return

                # 执行
                for _ in range(times):
                    executeCommand(img_path, command_dict, interval)

                # 运行到循环结束区间
                if i == part_cycle_end and part_cycle_time != 1:
                    # 仍需要循环执行，i指向循环起始区间
                    i = part_cycle_start
                    part_cycle_time -= 1
                    continue

                i += 1
        except Exception as e:
            myLog("第{}次循环出错：{}".format(cycle_time, str(e.args[0])))
            return "第{}次循环出错：{}".format(cycle_time, str(e.args[0]))


if __name__ == '__main__':
    # path = r"E:\Code\temp"
    # names = os.listdir(path)
    # detectFile(" && ".join([os.path.join(path, name) for name in names]) + " && E:\\Code\\temp\\test5.txt")

    string = "$getNum123$addNumfbaxx$subNumxx"
    data = {"1": string}
    executeCommand("", data, 0.1)
