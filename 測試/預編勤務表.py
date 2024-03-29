import tkinter as tk
import tkinter.font as tkFont
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from tkinter import ttk


c_mem = {'A': '0', 'B': '1', 'C': '2', 'D': '3'}
leader = {'A': '9', 'B': '3', 'C': '6', 'D': '10'}

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
        self.master.geometry("750x700")
        self.master.minsize(750, 600)
        self.master.maxsize(750, 600)

    def usr_login(self):
        # 獲取使用者輸入的usr_name和
        url = 'C:/Users/user/Desktop/勤務表小工具/勤務公示(假).exe'
        hou = int(self.entry_usr_name.get()) + 1
        usr_name = '洪文政'
        usr_pass = 'aA22962640'
        for i in range(101, hou):
            c_mem[str(i)] = str(i - 97)
        for j in range(201, 214):
            i += 1
            c_mem[str(j)] = str(i - 97)
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
        StartPage.driver.find_element('xpath', '//*[@id="DropDownList1"]/option[4]').click()

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
        self.background = tk.Canvas(self, height=600, width=750, bg='white').pack()
        tk.Label(self, text='輸入', font=('KaiTi', 40), bg='white').place(x=380, y=25)
        tk.Label(self, text='顏浩中番號\n或最後一般隊員番號:', font=('KaiTi', 26), bg='white').place(x=25, y=100)
        self.entry_usr_name = tk.StringVar()
        tk.Entry(self, bg='white', textvariable=self.entry_usr_name, font=('KaiTi', 26)).place(x=230, y=200)
        tk.Button(self, text='登入', bg='#ffcc69', font=('KaiTi', 20), command=self.usr_login).place(x=380, y=450)
        tk.Button(self, text='下一步', bg='#ff0099', font=('KaiTi', 20), command=self.ntsp).place(x=600, y=450)

class state(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self)
        self.grid()
        self.createWidgets()
        self.master.title('預編勤務表')
        self.master.geometry("700x700")
        self.master.minsize(700, 700)
        self.master.maxsize(700, 700)

    def day_create(self):
        StartPage.driver.find_element('xpath', '//*[@id="listDay"]').click()
        StartPage.driver.find_element('xpath', '//*[@id="listDay"]/option[' + self.entry_day.get() + ']').click()
        StartPage.driver.find_element('xpath', '//*[@id="btnCreateGroup"]').click()

    def ntsp(self):
        StartPage.driver.find_element('xpath', '//*[@id="btnSetVacation"]').click()
        StartPage.driver.find_element('xpath', '//*[@id="gridVacation_listVacationType_' + c_mem['116'] + '"]').click()
        StartPage.driver.find_element('xpath', '//*[@id="gridVacation_listVacationType_' + c_mem['116'] + '"]/option[13]').click()
        #輪休ing
        vac = self.entry_vac.get().split('.')
        try:
            vac.remove('402')
        except:
            pass
        try:
            vac.remove('401')
        except:
            pass
        try:
            for i in vac:
                StartPage.driver.find_element('xpath', '//*[@id="gridVacation_listVacationType_' + c_mem[i] + '"]').click()
                StartPage.driver.find_element('xpath', '//*[@id="gridVacation_listVacationType_' + c_mem[i] + '"]/option[2]').click()
        except:
            print('輪休失敗')
        # 外宿ing
        if self.entry_out.get() != '':
            out = self.entry_out.get().split('.')
            try:
                out.remove('402')
            except:
                pass
            try:
                out.remove('401')
            except:
                pass
            for i in out:
                StartPage.driver.find_element('xpath', '//*[@id="gridVacation_listVacationType_' + c_mem[i] + '"]').click()
                StartPage.driver.find_element('xpath', '//*[@id="gridVacation_listVacationType_' + c_mem[i] + '"]/option[14]').click()
        try:
            StartPage.driver.find_element('xpath', '//*[@id="btnVacationSave"]').click()
            StartPage.driver.find_element('xpath', '//*[@id="listLeader"]').click()
            StartPage.driver.find_element('xpath', '//*[@id="listLeader"]/option[' + leader[self.entry_cmd.get()] + ']').click()
            time.sleep(6)
            StartPage.driver.find_element('xpath', '//*[@id="listGroupType"]').click()
            StartPage.driver.find_element('xpath', '//*[@id="listGroupType"]/option[3]').click()
            time.sleep(1)
            StartPage.driver.find_element('xpath', '//*[@id="listItemName"]').click()
            StartPage.driver.find_element('xpath', '//*[@id="listItemName"]/option[23]').click()
            StartPage.driver.find_element('xpath', '//*[@id="btnAddItem"]').click()
            time.sleep(1)
        # 打攻擊車
            StartPage.driver.find_element('xpath', '//*[@id="listItemName"]/option[16]').click()
            time.sleep(1)
            StartPage.driver.find_element('xpath', '//*[@id="txtItemName"]').click()
            StartPage.driver.find_element('xpath', '//*[@id="txtItemName"]').send_keys('11')
            StartPage.driver.find_element('xpath', '//*[@id="btnAddItem"]').click()
            time.sleep(1)
        # 打水箱車
            StartPage.driver.find_element('xpath', '//*[@id="listItemName"]').click()
            StartPage.driver.find_element('xpath', '//*[@id="listItemName"]/option[12]').click()
            time.sleep(1)
            StartPage.driver.find_element('xpath', '//*[@id="txtItemName"]').click()
            StartPage.driver.find_element('xpath', '//*[@id="txtItemName"]').send_keys('16')
            StartPage.driver.find_element('xpath', '//*[@id="btnAddItem"]').click()
            time.sleep(1)
        # 打31車
            StartPage.driver.find_element('xpath', '//*[@id="listItemName"]').click()
            StartPage.driver.find_element('xpath', '//*[@id="listItemName"]/option[7]').click()
            time.sleep(1)
            StartPage.driver.find_element('xpath', '//*[@id="txtItemName"]').click()
            StartPage.driver.find_element('xpath', '//*[@id="txtItemName"]').send_keys('31')
            StartPage.driver.find_element('xpath', '//*[@id="btnAddItem"]').click()
            time.sleep(1)
        # 打91車
            StartPage.driver.find_element('xpath', '//*[@id="listItemName"]').click()
            StartPage.driver.find_element('xpath', '//*[@id="listItemName"]/option[3]').click()
            time.sleep(1)
            StartPage.driver.find_element('xpath', '//*[@id="txtItemName"]').click()
            StartPage.driver.find_element('xpath', '//*[@id="txtItemName"]').send_keys('92')
            StartPage.driver.find_element('xpath', '//*[@id="btnAddItem"]').click()
            time.sleep(1)
        # 打92車
            StartPage.driver.find_element('xpath', '//*[@id="listItemName"]').click()
            StartPage.driver.find_element('xpath', '//*[@id="listItemName"]/option[4]').click()
            StartPage.driver.find_element('xpath', '//*[@id="txtItemName"]').click()
            time.sleep(1)
            StartPage.driver.find_element('xpath', '//*[@id="txtItemName"]').send_keys('93')
            StartPage.driver.find_element('xpath', '//*[@id="btnAddItem"]').click()
            time.sleep(1)
        except:
            print('修宿、帶隊官、打車失敗')
        self.destroy()
        self.master.switch_frame(working)

    def createWidgets(self):
        # 創造可以用place的背景
        self.background = tk.Canvas(self, height=700, width=700, bg='white').pack()
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
        tk.Button(self, text='下一步', bg='#ff0099', font=('KaiTi', 20), command=self.ntsp).place(x=600, y=620)

class working(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self)
        self.grid()
        self.createWidgets()
        self.master.title('預編勤務表')
        self.master.geometry("700x700")
        self.master.minsize(700, 700)
        self.master.maxsize(700, 700)

    def day_create(self):
        person = self.entry_vac.get().split('.')
        for i in person:
            StartPage.driver.find_element('xpath', '//*[@id="listFireMan_ctrl' + str(int(c_mem[i]) // 6) + '_chkManCar_' + c_mem[i] + '"]').click()
        num = self.entry_day.get()
        StartPage.driver.find_element('xpath', '//*[@id="gridGroupFightMan_rdoItemName_' + num + '"]').click()
        time.sleep(0.5)
        car = self.entry_out.get()
        if car == '11':
            StartPage.driver.find_element('xpath', '//*[@id="listCar_ctrl0_chkManCar_0"]').click()
        elif car == '16':
            StartPage.driver.find_element('xpath', '//*[@id="listCar_ctrl0_chkManCar_1"]').click()
        elif car == '31':
            StartPage.driver.find_element('xpath', '//*[@id="listCar_ctrl0_chkManCar_2"]').click()
        elif car == '93':
            StartPage.driver.find_element('xpath', '//*[@id="listCar_ctrl1_chkManCar_11"]').click()
        elif car == '92':
            StartPage.driver.find_element('xpath', '//*[@id="listCar_ctrl1_chkManCar_10"]').click()
        else:
            StartPage.driver.find_element('xpath', '//*[@id="listCar_ctrl2_chkManCar_12"]').click()
        start = self.entry_cmd.get()
        fin = self.entry_fin.get()
        if int(fin) < int(start):
            for i in range(int(start), 24):
                StartPage.driver.find_element('xpath', '//*[@id="gridGroupFightMan_Button' + str(i) + '"]').click()
                time.sleep(0.5)
            for i in range(0, int(fin)):
                StartPage.driver.find_element('xpath', '//*[@id="gridGroupFightMan_Button' + str(i) + '"]').click()
                time.sleep(0.5)
        else:
            for i in range(int(start), int(fin)):
                StartPage.driver.find_element('xpath', '//*[@id="gridGroupFightMan_Button' + str(i) + '"]').click()
                time.sleep(0.5)
        time.sleep(1)
        self.entry_vac.set('')
        self.entry_cmd.current(i+1)
        StartPage.driver.find_element('xpath', '//*[@id="listFireMan_btnClearFireMan"]').click()
        StartPage.driver.find_element('xpath', '//*[@id="listFireMan_btnClearFireMan"]').click()
        time.sleep(1)
        StartPage.driver.find_element('xpath', '//*[@id="listCar_btnClearCar"]').click()
        StartPage.driver.find_element('xpath', '//*[@id="listCar_btnClearCar"]').click()


    def ntsp(self):
        try:
            StartPage.driver.find_element('xpath', '//*[@id="listGroupType"]').click()
            StartPage.driver.find_element('xpath', '//*[@id="listGroupType"]/option[2]').click()
            time.sleep(1)
            StartPage.driver.find_element('xpath', '//*[@id="listItemType"]').click()
            StartPage.driver.find_element('xpath', '//*[@id="listItemType"]/option[3]').click()
            time.sleep(1)
            StartPage.driver.find_element('xpath', '//*[@id="DropDownList1"]').click()
            StartPage.driver.find_element('xpath', '//*[@id="DropDownList1"]/option[5]').click()
            time.sleep(1)
            StartPage.driver.find_element('xpath', '//*[@id="listItemName"]').click()
            StartPage.driver.find_element('xpath', '//*[@id="listItemName"]/option[1]').click()
            StartPage.driver.find_element('xpath', '//*[@id="btnAddItem"]').click()
            time.sleep(1)
            StartPage.driver.find_element('xpath', '//*[@id="listItemName"]').click()
            StartPage.driver.find_element('xpath', '//*[@id="listItemName"]/option[3]').click()
            StartPage.driver.find_element('xpath', '//*[@id="btnAddItem"]').click()
            time.sleep(1)
            StartPage.driver.find_element('xpath', '//*[@id="listItemName"]').click()
            StartPage.driver.find_element('xpath', '//*[@id="listItemName"]/option[4]').click()
            time.sleep(1)
            StartPage.driver.find_element('xpath', '//*[@id="txtItemName"]').click()
            StartPage.driver.find_element('xpath', '//*[@id="txtItemName"]').send_keys('服務區查察')
            StartPage.driver.find_element('xpath', '//*[@id="btnAddItem"]').click()
            time.sleep(1)
            StartPage.driver.find_element('xpath', '//*[@id="txtItemName"]').click()
            StartPage.driver.find_element('xpath', '//*[@id="txtItemName"]').clear()
            StartPage.driver.find_element('xpath', '//*[@id="txtItemName"]').send_keys('TP訓')
            StartPage.driver.find_element('xpath', '//*[@id="btnAddItem"]').click()
        except:
            print('服務區查察建置有錯')
        self.destroy()
        self.master.switch_frame(leaving)


    def createWidgets(self):
        # 創造可以用place的背景
        self.background = tk.Canvas(self, height=700, width=700, bg='white').pack()
        tk.Button(self, text='打入', bg='#ffcc69', font=('KaiTi', 20), command=self.day_create).place(x=380, y=620)
        tk.Button(self, text='下一步', bg='#ff0099', font=('KaiTi', 20), command=self.ntsp).place(x=600, y=620)
        tk.Label(self, text='幾時誰上?', font=('KaiTi', 40), bg='white').place(x=250, y=25)
        tk.Label(self, text='第幾項\n從0開始:', font=('KaiTi', 26), bg='white').place(x=25, y=100)
        self.entry_day = tk.StringVar()
        tk.Entry(self, bg='white', textvariable=self.entry_day, font=('KaiTi', 26)).place(x=230, y=100)
        tk.Label(self, text='車:', font=('KaiTi', 26), bg='white').place(x=25, y=250)
        self.entry_out = tk.StringVar()
        tk.Entry(self, bg='white', textvariable=self.entry_out, font=('KaiTi', 26)).place(x=150, y=250)
        tk.Label(self, text='人\n用.分開:', font=('KaiTi', 26), bg='white').place(x=25, y=400)
        self.entry_vac = tk.StringVar()
        tk.Entry(self, bg='white', textvariable=self.entry_vac, font=('KaiTi', 26)).place(x=150, y=400)
        tk.Label(self, text='結束時間:', font=('KaiTi', 26), bg='white').place(x=400, y=550)
        self.entry_fin = ttk.Combobox(font=('KaiTi', 26), values=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                                        '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
                                        '21', '22', '23', '24'], width=5)
        self.entry_fin.place(x=580, y=550)
        tk.Label(self, text='開始時間:', font=('KaiTi', 26), bg='white').place(x=25, y=550)
        self.entry_cmd = ttk.Combobox(font=('KaiTi', 26), values=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                                        '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
                                        '21', '22', '23', '24'], width=5)
        self.entry_cmd.place(x=200, y=550)

class leaving(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self)
        self.grid()
        self.createWidgets()
        self.master.title('預編勤務表')
        self.master.geometry("700x700")
        self.master.minsize(700, 700)
        self.master.maxsize(700, 700)

    def day_create(self):
        person = self.entry_vac.get().split('.')
        for i in person:
            StartPage.driver.find_element('xpath', '//*[@id="listFireMan_ctrl' + str(int(c_mem[i]) // 6) + '_chkManCar_' + c_mem[i] + '"]').click()
        num = self.entry_day.get()
        StartPage.driver.find_element('xpath', '//*[@id="gridGroupWorkMan_rdoItemName_' + num + '"]').click()
        time.sleep(1)
        car = self.entry_out.get()
        if car == '11':
            StartPage.driver.find_element('xpath', '//*[@id="listCar_ctrl0_chkManCar_0"]').click()
        elif car == '16':
            StartPage.driver.find_element('xpath', '//*[@id="listCar_ctrl0_chkManCar_1"]').click()
        elif car == '31':
            StartPage.driver.find_element('xpath', '//*[@id="listCar_ctrl0_chkManCar_2"]').click()
        elif car == '93':
            StartPage.driver.find_element('xpath', '//*[@id="listCar_ctrl1_chkManCar_11"]').click()
        elif car == '92':
            StartPage.driver.find_element('xpath', '//*[@id="listCar_ctrl1_chkManCar_10"]').click()
        else:
            StartPage.driver.find_element('xpath', '//*[@id="listCar_ctrl2_chkManCar_12"]').click()
        start = self.entry_cmd.get()
        fin = self.entry_fin.get()
        if int(fin) < int(start):
            for i in range(int(start), 24):
                StartPage.driver.find_element('xpath', '//*[@id="gridGroupWorkMan_Button' + str(i) + '"]').click()
                time.sleep(0.5)
            for i in range(0, int(fin)):
                StartPage.driver.find_element('xpath', '//*[@id="gridGroupWorkMan_Button' + str(i) + '"]').click()
                time.sleep(0.5)
        else:
            for i in range(int(start), int(fin)):
                StartPage.driver.find_element('xpath', '//*[@id="gridGroupWorkMan_Button' + str(i) + '"]').click()
                time.sleep(0.5)
        time.sleep(1)
        self.entry_vac.set('')
        self.entry_cmd.current(i+1)
        StartPage.driver.find_element('xpath', '//*[@id="listFireMan_btnClearFireMan"]').click()
        StartPage.driver.find_element('xpath', '//*[@id="listFireMan_btnClearFireMan"]').click()
        time.sleep(1)
        StartPage.driver.find_element('xpath', '//*[@id="listCar_btnClearCar"]').click()
        StartPage.driver.find_element('xpath', '//*[@id="listCar_btnClearCar"]').click()


    def createWidgets(self):
        # 創造可以用place的背景
        self.background = tk.Canvas(self, height=700, width=700, bg='white').pack()
        tk.Button(self, text='打入', bg='#ffcc69', font=('KaiTi', 20), command=self.day_create).place(x=380, y=620)
        tk.Label(self, text='誰能逃獄?', font=('KaiTi', 40), bg='white').place(x=250, y=25)
        tk.Label(self, text='第幾項\n從0開始:', font=('KaiTi', 26), bg='white').place(x=25, y=100)
        self.entry_day = tk.StringVar()
        tk.Entry(self, bg='white', textvariable=self.entry_day, font=('KaiTi', 26)).place(x=230, y=100)
        tk.Label(self, text='車:', font=('KaiTi', 26), bg='white').place(x=25, y=250)
        self.entry_out = tk.StringVar()
        tk.Entry(self, bg='white', textvariable=self.entry_out, font=('KaiTi', 26)).place(x=150, y=250)
        tk.Label(self, text='人\n用.分開:', font=('KaiTi', 26), bg='white').place(x=25, y=400)
        self.entry_vac = tk.StringVar()
        tk.Entry(self, bg='white', textvariable=self.entry_vac, font=('KaiTi', 26)).place(x=150, y=400)
        tk.Label(self, text='結束時間:', font=('KaiTi', 26), bg='white').place(x=400, y=550)
        self.entry_fin = ttk.Combobox(font=('KaiTi', 26), values=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                                        '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
                                        '21', '22', '23', '24'], width=5)
        self.entry_fin.place(x=580, y=550)
        tk.Label(self, text='開始時間:', font=('KaiTi', 26), bg='white').place(x=25, y=550)
        self.entry_cmd = ttk.Combobox(font=('KaiTi', 26), values=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                                        '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
                                        '21', '22', '23', '24'], width=5)
        self.entry_cmd.place(x=200, y=550)


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
