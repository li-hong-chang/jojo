import tkinter as tk
import tkinter.font as tkFont
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


mem = {'A': '洪文政', 'B': '陳信宏', 'C': '曾英傑', 'D': '蔡孟洲', '101': '黃國峰', '102': '周家宇', '103': '林易進', '104': '吳信慧', '105': '郭霆宥',
      '106': '呂信賢', '107': '蘇偉銘', '108': '鄭志康', '109': '李政廣', '110': '黃俊淳', '111': '陳台俊', '112': '沈子恩', '201': '吳俊億', '202': '李易融',
      '203': '黃偉智', '204': '陳忠志', '205': '陳晟暉', '206': '廖阜億', '207': '陳冠呈', '208': '王南翔', '209': '周少軒', '210': '顏永全', '211': '黃科翰',
      '212': '吳柏霆', '301': '陳昇勳', '302': '杜仇軒志', '303': '張勝凱', '304': '黃楷棠', '305': '詹家豪'}
c_mem = {'A': '0', 'B': '1', 'C': '2', 'D': '3', '101': '4', '102': '5', '103': '6', '104': '7', '105': '8', '106': '9', '107': '10', '108': '11',
      '109': '12', '110': '13', '111': '14', '112': '15', '113': '16', '201': '17', '202': '18', '203': '19', '204': '20', '205': '21', '206': '22',
      '207': '23', '208': '24', '209': '25', '210': '26', '211': '27', '212': '28', '301': '29', '302': '30', '303': '31', '304': '32', '305': '33'}
leader = {'A': '11', 'B': '2', 'C': '8', 'D': '10'}

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
        url = self.entry_usr_name.get()
        usr_name = '洪文政'
        usr_pass = 'Vv22962640..'
        '''StartPage.name = usr_name'''
        my_option = webdriver.ChromeOptions()
        # my_option.add_argument('--incognito')
        my_option.add_argument('--no-sandingbox')
        my_option.add_argument("--disable-notifications")
        service = Service(executable_path=url)
        StartPage.driver = webdriver.Chrome(service=service, options=my_option)
        StartPage.driver.get('http://172.28.16.66:8078/login.aspx') # 開啟
        time.sleep(5)
        name_box = StartPage.driver.find_element('xpath', '//*[@id="txt_ac"]')
        pass_box = StartPage.driver.find_element('xpath', '//*[@id="txt_pwd"]')
        name_box.send_keys(usr_name)
        pass_box.send_keys(usr_pass)
        StartPage.driver.find_element('xpath', '//*[@id="DropDownList1"]').click()
        StartPage.driver.find_element('xpath', '//*[@id="DropDownList1"]/option[2]').click()

    def ntsp(self):
        StartPage.driver.find_element('xpath', '//*[@id="btnCarPerson"]').click()
        time.sleep(1)
        StartPage.driver.find_element('xpath', '//*[@id="LinkButton4"]/span').click()
        time.sleep(1)
        StartPage.driver.find_element('xpath', '//*[@id="ContentPlaceHolder1_btn_insertdata"]').click()
        self.destroy()
        self.master.switch_frame(state)

    def createWidgets(self):
        # 創造可以用place的背景
        self.background = tk.Canvas(self, height=600, width=800, bg='white').pack()
        tk.Label(self, text='輸入', font=('KaiTi', 40), bg='white').place(x=380, y=25)
        tk.Label(self, text='位置:', font=('KaiTi', 26), bg='white').place(x=25, y=100)
        self.entry_usr_name = tk.StringVar()
        tk.Entry(self, bg='white', textvariable=self.entry_usr_name, font=('KaiTi', 26)).place(x=230, y=100)
        tk.Button(self, text='登入', bg='#ffcc69', font=('KaiTi', 20), command=self.usr_login).place(x=380, y=450)
        tk.Button(self, text='下一步', bg='#ff0099', font=('KaiTi', 20), command=self.ntsp).place(x=650, y=450)

class state(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self)
        self.grid()
        self.createWidgets()
        self.master.title('預編勤務表')
        self.master.geometry("780x780")
        self.master.minsize(800, 800)
        self.master.maxsize(800, 800)

    def day_create(self):
        StartPage.driver.find_element('xpath', '//*[@id="listDay"]').click()
        StartPage.driver.find_element('xpath', '//*[@id="listDay"]/option[' + self.entry_day.get() + ']').click()
        StartPage.driver.find_element('xpath', '//*[@id="btnCreateGroup"]').click()

    def ntsp(self):
        StartPage.driver.find_element('xpath', '//*[@id="btnSetVacation"]').click()
        StartPage.driver.find_element('xpath', '//*[@id="gridVacation_listVacationType_16"]').click()
        StartPage.driver.find_element('xpath', '//*[@id="gridVacation_listVacationType_16"]/option[13]').click()
        StartPage.driver.find_element('xpath', '//*[@id="gridVacation_listVacationType_12"]').click()
        StartPage.driver.find_element('xpath', '//*[@id="gridVacation_listVacationType_12"]/option[2]').click()
        #輪休ing
        vac = self.entry_vac.get().split('.')
        for i in vac:
            StartPage.driver.find_element('xpath', '//*[@id="gridVacation_listVacationType_' + c_mem[i] + '"]').click()
            StartPage.driver.find_element('xpath', '//*[@id="gridVacation_listVacationType_' + c_mem[i] + '"]/option[2]').click()
        # 外宿ing
        out = self.entry_out.get().split('.')
        for i in out:
            StartPage.driver.find_element('xpath', '//*[@id="gridVacation_listVacationType_' + c_mem[i] + '"]').click()
            StartPage.driver.find_element('xpath', '//*[@id="gridVacation_listVacationType_' + c_mem[i] + '"]/option[14]').click()
        StartPage.driver.find_element('xpath', '//*[@id="btnVacationSave"]').click()
        StartPage.driver.find_element('xpath', '//*[@id="listLeader"]').click()
        StartPage.driver.find_element('xpath', '//*[@id="listLeader"]/option[' + leader[self.entry_cmd.get()] + ']').click()
        time.sleep(6)
        StartPage.driver.find_element('xpath', '//*[@id="listGroupType"]').click()
        StartPage.driver.find_element('xpath', '//*[@id="listGroupType"]/option[3]').click()
        StartPage.driver.find_element('xpath', '//*[@id="listItemName"]').click()
        # 打攻擊車
        StartPage.driver.find_element('xpath', '//*[@id="listItemName"]/option[16]').click()
        StartPage.driver.find_element('xpath', '//*[@id="txtItemName"]').click()
        StartPage.driver.find_element('xpath', '//*[@id="txtItemName"]').send_keys('11')
        StartPage.driver.find_element('xpath', '//*[@id="btnAddItem"]').click()
        # 打水箱車
        StartPage.driver.find_element('xpath', '//*[@id="listItemName"]/option[12]').click()
        StartPage.driver.find_element('xpath', '//*[@id="txtItemName"]').click()
        StartPage.driver.find_element('xpath', '//*[@id="txtItemName"]').send_keys('16')
        StartPage.driver.find_element('xpath', '//*[@id="btnAddItem"]').click()
        # 打31車
        StartPage.driver.find_element('xpath', '//*[@id="listItemName"]/option[7]').click()
        StartPage.driver.find_element('xpath', '//*[@id="txtItemName"]').click()
        StartPage.driver.find_element('xpath', '//*[@id="txtItemName"]').send_keys('31')
        StartPage.driver.find_element('xpath', '//*[@id="btnAddItem"]').click()
        # 打91車
        StartPage.driver.find_element('xpath', '//*[@id="listItemName"]/option[3]').click()
        StartPage.driver.find_element('xpath', '//*[@id="txtItemName"]').click()
        StartPage.driver.find_element('xpath', '//*[@id="txtItemName"]').send_keys('93')
        StartPage.driver.find_element('xpath', '//*[@id="btnAddItem"]').click()
        # 打92車
        StartPage.driver.find_element('xpath', '//*[@id="listItemName"]/option[4]').click()
        StartPage.driver.find_element('xpath', '//*[@id="txtItemName"]').click()
        StartPage.driver.find_element('xpath', '//*[@id="txtItemName"]').send_keys('92')
        StartPage.driver.find_element('xpath', '//*[@id="btnAddItem"]').click()
        self.destroy()
        self.master.switch_frame(working)

    def createWidgets(self):
        # 創造可以用place的背景
        self.background = tk.Canvas(self, height=800, width=800, bg='white').pack()
        tk.Label(self, text='誰休息?', font=('KaiTi', 40), bg='white').place(x=350, y=25)
        tk.Label(self, text='日期(幾號):', font=('KaiTi', 26), bg='white').place(x=25, y=100)
        self.entry_day = tk.StringVar()
        tk.Entry(self, bg='white', textvariable=self.entry_day, font=('KaiTi', 26)).place(x=230, y=100)
        tk.Button(self, text='打入', bg='#ffcc69', font=('KaiTi', 20), command=self.day_create).place(x=380, y=150)
        tk.Label(self, text='輪休\n用.分開:', font=('KaiTi', 26), bg='white').place(x=25, y=250)
        self.entry_vac = tk.StringVar()
        tk.Entry(self, bg='white', textvariable=self.entry_vac, font=('KaiTi', 26)).place(x=150, y=250)
        tk.Label(self, text='外宿\n用.分開:', font=('KaiTi', 26), bg='white').place(x=25, y=400)
        self.entry_out = tk.StringVar()
        tk.Entry(self, bg='white', textvariable=self.entry_out, font=('KaiTi', 26)).place(x=150, y=400)
        tk.Label(self, text='帶隊官:', font=('KaiTi', 26), bg='white').place(x=25, y=550)
        self.entry_cmd = tk.StringVar()
        tk.Entry(self, bg='white', textvariable=self.entry_cmd, font=('KaiTi', 26)).place(x=150, y=550)
        tk.Button(self, text='下一步', bg='#ff0099', font=('KaiTi', 20), command=self.ntsp).place(x=650, y=700)

class working(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self)
        self.grid()
        self.createWidgets()
        self.master.title('預編勤務表')
        self.master.geometry("780x780")
        self.master.minsize(800, 800)
        self.master.maxsize(800, 800)

    def day_create(self):
        person = self.entry_vac.get().split('.')
        for i in person:
            StartPage.driver.find_element('xpath', '//*[@id="listFireMan_ctrl' + str(c_mem[i]//5) + '_chkManCar_' + c_mem[i] + '"]').click()
        num = self.entry_day.get()
        StartPage.driver.find_element('xpath', '//*[@id="gridGroupFightMan_rdoItemName_' + num + '"]').click()
        car = self.entry_out.get()
        if car == '11':
            StartPage.driver.find_element('xpath', '//*[@id="listCar_ctrl0_chkManCar_0"]').click()
        elif car == '16':
            StartPage.driver.find_element('xpath', '//*[@id="listCar_ctrl0_chkManCar_1"]').click()
        elif car == '31':
            StartPage.driver.find_element('xpath', '//*[@id="listCar_ctrl0_chkManCar_3"]').click()
        elif car == '93':
            StartPage.driver.find_element('xpath', '//*[@id="listCar_ctrl1_chkManCar_11"]').click()
        elif car == '92':
            StartPage.driver.find_element('xpath', '//*[@id="listCar_ctrl1_chkManCar_10"]').click()
        else:
            StartPage.driver.find_element('xpath', '//*[@id="listCar_ctrl2_chkManCar_13"]').click()
        time.sleep(0.5)
        hour = self.entry_cmd.get().split('.')
        for i in range(int(hour[0]), int(hour[1])):
            StartPage.driver.find_element('xpath', '//*[@id="gridGroupFightMan_Button' + str(i) + '"]').click()
            time.sleep(0.5)
        StartPage.driver.find_element('xpath', '//*[@id="listFireMan_btnClearFireMan"]').click()
        StartPage.driver.find_element('xpath', '//*[@id="listCar_btnClearCar"]').click()



    def ntsp(self):
        StartPage.driver.find_element('xpath', '//*[@id="listGroupType"]').click()
        StartPage.driver.find_element('xpath', '//*[@id="listGroupType"]/option[2]').click()
        StartPage.driver.find_element('xpath', '//*[@id="listItemType"]').click()
        StartPage.driver.find_element('xpath', '//*[@id="listItemType"]/option[2]').click()
        StartPage.driver.find_element('xpath', '//*[@id="DropDownList1"]').click()
        StartPage.driver.find_element('xpath', '//*[@id="DropDownList1"]/option[5]').click()
        StartPage.driver.find_element('xpath', '//*[@id="listItemName"]').click()
        StartPage.driver.find_element('xpath', '//*[@id="listItemName"]/option[4]').click()
        StartPage.driver.find_element('xpath', '//*[@id="txtItemName"]').send_keys('安檢系統建置、審核業務')
        StartPage.driver.find_element('xpath', '//*[@id="btnAddItem"]').click()
        StartPage.driver.find_element('xpath', '//*[@id="listGroupType"]').click()
        StartPage.driver.find_element('xpath', '//*[@id="listItemType"]/option[3]').click()
        StartPage.driver.find_element('xpath', '//*[@id="listItemType"]').click()
        StartPage.driver.find_element('xpath', '//*[@id="DropDownList1"]/option[18]').click()
        StartPage.driver.find_element('xpath', '//*[@id="listItemName"]').click()
        StartPage.driver.find_element('xpath', '//*[@id="listItemName"]/option[14]').click()
        StartPage.driver.find_element('xpath', '//*[@id="btnAddItem"]').click()
        StartPage.driver.find_element('xpath', '//*[@id="listItemName"]/option[16]').click()
        StartPage.driver.find_element('xpath', '//*[@id="btnAddItem"]').click()
        StartPage.driver.find_element('xpath', '//*[@id="DropDownList1"]').click()
        StartPage.driver.find_element('xpath', '//*[@id="DropDownList1"]/option[5]').click()
        StartPage.driver.find_element('xpath', '//*[@id="listItemName"]').click()
        StartPage.driver.find_element('xpath', '//*[@id="listItemName"]/option[3]').click()
        StartPage.driver.find_element('xpath', '//*[@id="btnAddItem"]').click()
        StartPage.driver.find_element('xpath', '//*[@id="listItemName"]/option[4]').click()
        StartPage.driver.find_element('xpath', '//*[@id="txtItemName"]').send_keys('值班')
        StartPage.driver.find_element('xpath', '//*[@id="btnAddItem"]').click()


    def createWidgets(self):
        # 創造可以用place的背景
        self.background = tk.Canvas(self, height=800, width=800, bg='white').pack()
        tk.Label(self, text='幾時誰上?', font=('KaiTi', 40), bg='white').place(x=350, y=25)
        tk.Label(self, text='第幾項\n從0開始:', font=('KaiTi', 26), bg='white').place(x=25, y=100)
        self.entry_day = tk.StringVar()
        tk.Entry(self, bg='white', textvariable=self.entry_day, font=('KaiTi', 26)).place(x=230, y=100)
        tk.Label(self, text='人\n用.分開:', font=('KaiTi', 26), bg='white').place(x=25, y=250)
        self.entry_vac = tk.StringVar()
        tk.Entry(self, bg='white', textvariable=self.entry_vac, font=('KaiTi', 26)).place(x=150, y=250)
        tk.Label(self, text='車:', font=('KaiTi', 26), bg='white').place(x=25, y=400)
        self.entry_out = tk.StringVar()
        tk.Entry(self, bg='white', textvariable=self.entry_out, font=('KaiTi', 26)).place(x=150, y=400)
        tk.Label(self, text='時間\n開始和結束\n用.分開:', font=('KaiTi', 26), bg='white').place(x=25, y=550)
        self.entry_cmd = tk.StringVar()
        tk.Entry(self, bg='white', textvariable=self.entry_cmd, font=('KaiTi', 26)).place(x=150, y=550)
        tk.Button(self, text='打入', bg='#ffcc69', font=('KaiTi', 20), command=self.day_create).place(x=380, y=700)
        tk.Button(self, text='下一步', bg='#ff0099', font=('KaiTi', 20), command=self.ntsp).place(x=650, y=700)


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
