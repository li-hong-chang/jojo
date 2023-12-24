import tkinter as tk
import tkinter.font as tkFont

radio = tk.Tk()

def usr_login():
    a = entry_yesterday.get().split('.')
    b = entry_today.get().split('.')
    try:
        a.remove('401')
    except:
        pass
    try:
        b.remove('401')
    except:
        pass
    go = []
    for i in a:
        if i not in b:
            go.append(i)
    go.sort()
    tk.Label(text='上:', font=('KaiTi', 26), bg='white').place(x=100, y=300)
    tk.Label(text=', '.join(go), font=('KaiTi', 26), bg='pink').place(x=150, y=350)
    down = []
    for i in b:
        if i not in a:
            down.append(i)
    down.sort()
    tk.Label(text='下:', font=('KaiTi', 26), bg='white').place(x=100, y=400)
    tk.Label(text=', '.join(down), font=('KaiTi', 26), bg='yellow').place(x=150, y=450)


radio.title('無線電交接')
radio.geometry("800x600")
radio.background = tk.Canvas(height=600, width=800, bg='white').pack()
entry_yesterday = tk.StringVar()
tk.Entry(bg='white', textvariable=entry_yesterday, font=('KaiTi', 26)).place(x=230, y=100)
tk.Label(text='昨天休息:', font=('KaiTi', 26), bg='white').place(x=25, y=100)
tk.Label(text='別忘了補休之類的', font=('KaiTi', 26), bg='red').place(x=25, y=175)
entry_today = tk.StringVar()
tk.Entry(bg='white', textvariable=entry_today, font=('KaiTi', 26)).place(x=230, y=250)
tk.Label(text='今天休息:', font=('KaiTi', 26), bg='white').place(x=25, y=250)
tk.Button(text='登入', bg='#ffcc69', font=('KaiTi', 20), command=usr_login).place(x=380, y=490)

radio.mainloop()
