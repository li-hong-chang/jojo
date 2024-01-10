import tkinter as tk
import tkinter.font as tkFont

class radio(tk.Frame):

    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.createWidgets()
        self.master.title('無線電交接')
        self.master.geometry("800x600")
        self.master.minsize(800, 600)
        self.master.maxsize(800, 600)


    def usr_login(self):
        a = self.entry_yesterday.get().split('.')
        b = self.entry_today.get().split('.')
        try:
            a.remove('401')
        except:
            pass
        try:
            b.remove('402')
        except:
            pass
        go = []
        for i in a:
            if i not in b:
                go.append(i)
        go.sort()
        tk.Label(self, text='上:', font=('KaiTi', 26), bg='white').place(x=100, y=300)
        tk.Label(self, text=', '.join(go), font=('KaiTi', 26), bg='pink').place(x=150, y=350)
        down = []
        for i in b:
            if i not in a:
                down.append(i)
        down.sort()
        tk.Label(self, text='下:', font=('KaiTi', 26), bg='white').place(x=100, y=400)
        tk.Label(self, text=', '.join(down), font=('KaiTi', 26), bg='yellow').place(x=150, y=450)


    def createWidgets(self):
        background = tk.Canvas(self, height=600, width=800, bg='white').pack()
        self.entry_yesterday = tk.StringVar()
        tk.Entry(self, bg='white', textvariable=self.entry_yesterday, font=('KaiTi', 26)).place(x=230, y=100)
        tk.Label(self, text='昨天休息:', font=('KaiTi', 26), bg='white').place(x=25, y=100)
        tk.Label(self, text='別忘了補休之類的', font=('KaiTi', 26), bg='red').place(x=25, y=175)
        self.entry_today = tk.StringVar()
        tk.Entry(self, bg='white', textvariable=self.entry_today, font=('KaiTi', 26)).place(x=230, y=250)
        tk.Label(self, text='今天休息:', font=('KaiTi', 26), bg='white').place(x=25, y=250)
        tk.Button(self, text='交接', bg='#ffcc69', font=('KaiTi', 20), command=self.usr_login).place(x=380, y=500)


if __name__ == "__main__":
    app = radio()
    app.mainloop()
