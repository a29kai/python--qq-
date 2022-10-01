import win32gui
import win32con
import win32clipboard as clipboard
import time
def Send(name, msg):
    # 打开剪贴板
    clipboard.OpenClipboard()
    # 清空剪贴板
    clipboard.EmptyClipboard()
    # 设置剪贴板内容
    clipboard.SetClipboardData(win32con.CF_UNICODETEXT, msg)
    # 获取剪贴板内容
    date = clipboard.GetClipboardData()
    # 关闭剪贴板
    clipboard.CloseClipboard()
    # 获取qq窗口句柄
    handle = win32gui.FindWindow(None, name)
    if handle == 0:
        print('未找到窗口！')
    # 显示窗口
    win32gui.ShowWindow(handle, win32con.SW_SHOW)
    # 把剪切板内容粘贴到qq窗口
    win32gui.SendMessage(handle, win32con.WM_PASTE, 0, 0)
    # 按下后松开回车键，发送消息
    win32gui.SendMessage(handle, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    win32gui.SendMessage(handle, win32con.WM_KEYUP, win32con.VK_RETURN, 0)
    time.sleep(0.1)
    #间隔时间，推荐别太短，我第一次设的0，然后QQ反应不过来
if __name__ == "__main__":
    name = input("输入聊天框名称")
    #此处输入聊天框的名字（备注）
    text = input('请输入轰炸内容')
    for i in range(1000):
        #range内轰炸次数
        Send(name,text)
        #双引号内输入轰炸内容




