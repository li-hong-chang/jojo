import tkinter as tk
import tkinter.font as tkFont
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self)
        self.grid()
        self.createWidgets()
        self.master.title('預編勤務表')
        self.master.geometry("800x600")
        self.master.minsize(800, 600)
        self.master.maxsize(800, 600)

    def usr_login(self):
        # 獲取使用者輸入的usr_name和
        usr_name = self.entry_usr_name.get()
        usr_pass = self.entry_usr_pass.get()
        '''StartPage.name = usr_name'''
        my_option = webdriver.ChromeOptions()
        my_option.add_argument('--incognito')
        # my_option.add_argument('--headless')
        my_option.add_argument("--disable-notifications")
        service = Service(executable_path=r'C:/chromedriver/chromedriver.exe')
        StartPage.driver = webdriver.Chrome(service=service, options=my_option)
        StartPage.driver.get('https://cloud.ntpc.gov.tw/indexIE6.jsp') # 開啟
        time.sleep(6)
        name_box = StartPage.driver.find_element('xpath', '/html/body/form/div/div/div[3]/div[1]/table/tbody/tr[1]/td[2]/div/input')
        pass_box = StartPage.driver.find_element('xpath', '//*[@id="txtpassword"]')
        name_box.send_keys(usr_name)
        pass_box.click()
        time.sleep(1)
        pass_box = StartPage.driver.find_element('xpath', '//*[@id="mpswd"]')
        pass_box.send_keys(usr_pass)

    def ntsp(self):
        self.destroy()
        self.master.switch_frame(state)

    def createWidgets(self):
        # 創造可以用place的背景
        self.background = tk.Canvas(self, height=600, width=800, bg='white').pack()
        tk.Label(self, text='輸入', font=('KaiTi', 40), bg='white').place(x=380, y=25)
        tk.Label(self, text='帳號:', font=('KaiTi', 26), bg='white').place(x=25, y=100)
        tk.Label(self, text='密碼:', font=('KaiTi', 26), bg='white').place(x=25, y=150)
        self.entry_usr_name = tk.StringVar()
        tk.Entry(self, bg='white', textvariable=self.entry_usr_name, font=('KaiTi', 26)).place(x=150, y=100)
        self.entry_usr_pass = tk.StringVar()
        tk.Entry(self, bg='white', textvariable=self.entry_usr_pass, font=('KaiTi', 26)).place(x=150, y=150)
        tk.Button(self, text='登入', bg='#ffcc69', font=('KaiTi', 20), command=self.usr_login).place(x=380, y=450)
        tk.Button(self, text='下一步', bg='#ff0099', font=('KaiTi', 20), command=self.ntsp).place(x=650, y=450)

class state(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self)
        self.grid()
        self.createWidgets()
        self.master.title('預編勤務表')
        self.master.geometry("800x600")
        self.master.minsize(800, 600)
        self.master.maxsize(800, 600)


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()