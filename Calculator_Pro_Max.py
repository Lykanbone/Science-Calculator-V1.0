import tkinter as tk
import math
import tkinter.messagebox
import tkinter.font
from tkinter import StringVar
from sympy import integrate, symbols
# from PIL import Image, ImageTk

exp_str = ""
History_list = [] # 历史记录
tempnum = 0 # 控制findb
result_out = '' # 简单计算器输出

# *************************************初始窗口**************************************
root = tk.Tk() # 初始化窗口
root.title('Science Calculator V1.0')
root.resizable(0, 0) # 窗口不可变

# image_file=ImageTk.PhotoImage(Image.open('1.png')) # 设置窗口欢迎图片
# label=tk.Label(root,image=image_file)
# label.pack()

# *************************************菜单******************************************
def menubar():

    menu1 = tk.Menu(root, tearoff=0)
    menu1.add_separator() # 添加分隔线
    menu1.add_command(label='一元二次方程', command=equation_solve_twice)
    menu1.add_separator()
    menu1.add_command(label='进制转换', command=numsystem_trans)
    menu1.add_separator()
    menu1.add_command(label='统计', command=statistics)
    menu1.add_separator()
    menu1.add_command(label='积分', command=Integrater)

    menubar = tk.Menu(root)
    menubar.add_cascade(label='简单计算器', command=simple_calculator)
    menubar.add_cascade(label='工具', menu=menu1)
    menubar.add_cascade(label='返回', command=lambda :calculator())
    menubar.add_cascade(label='帮助', command=help1)
    menubar.add_cascade(label='关于', command=about)

    root.config(menu=menubar)

# *************************************简单计算模块************************************
def simple_calculator():
    window = tkinter.Tk() # 新建简单计算器窗口
    window.title("Simple Calculator")
    window.resizable(0, 0)  # 窗口不可变

    def onClick(key):

        global exp_str,tempnum  # 定义全局变量

        if key == "=":
            Output = round(eval(exp_str), 2) # 核心计算模块eval，四舍五入2位
            result["text"] = Output
            frame_right.pack()
            t = tkinter.Label(frame_inner, text=exp_str + "=" + str(Output))
            t.pack()
            History_list.append(t)  # 存储历史记录
        elif key == "AC":
            resultin["text"] = ""
            result["text"] = ""
            exp_str = ""
        elif key == "DEL":
            if exp_str != "":
                resultin["text"] = exp_str[0:-1] # 切片操作
                exp_str = exp_str[0:-1]
        elif key == '.':
            exp_str = exp_str + str(key)
            resultin["text"] = exp_str
        else:
            exp_str = exp_str + str(key)
            result["text"] = result_out
            resultin["text"] = exp_str

    frame_left = tkinter.Frame(window) # 添加输出输入按钮的控件容器
    frame_left.pack(fill="y", side="left")
    frame_right = tkinter.Frame(window, width=200) # 添加历史框的容器控件
    tkinter.Label(frame_right, text="历史", font=("Arial", 14, "underline bold")).pack()
    frame_inner = tkinter.Frame(frame_right) # 添加历史内容的容器控件
    frame_inner.pack(fill="x", side="top")

    resultin = tkinter.Label(frame_left, height=2, font=("Arial", 30, "bold"))  # 设置结果窗口
    resultin.grid(row=0, column=0, columnspan=4, sticky=tkinter.E)  # 采用表格式布局管理器grid
    result = tkinter.Label(frame_left, height=2, font=("Arial", 30, "bold")) # 设置结果窗口
    result.grid(row=1, column=0, columnspan=4, sticky=tkinter.E)  # 采用表格式布局管理器grid

    # 设置按钮
    ac = tkinter.Button(frame_left, text="AC", width=9, height=3, command=lambda: onClick("AC")) # 使用lambda传参
    ac.grid(row=2, column=0)  # (第1行，第0列)
    ac.configure(background="red")

    negative = tkinter.Button(frame_left, text="DEL", width=9, height=3, command=lambda: onClick("DEL"))
    negative.grid(row=2, column=1)
    negative.configure(background="gray")

    percent = tkinter.Button(frame_left, text="%", width=9, height=3, command=lambda: onClick("/100"))
    percent.grid(row=2, column=2)

    division = tkinter.Button(frame_left, text="/", width=9, height=3, command=lambda: onClick("/"))
    division.grid(row=2, column=3)

    num7 = tkinter.Button(frame_left, text="7", width=9, height=3, command=lambda: onClick(7))
    num7.grid(row=3, column=0)

    num8 = tkinter.Button(frame_left, text="8", width=9, height=3, command=lambda: onClick(8))
    num8.grid(row=3, column=1)

    num9 = tkinter.Button(frame_left, text="9", width=9, height=3, command=lambda: onClick(9))
    num9.grid(row=3, column=2)

    multi = tkinter.Button(frame_left, text="*", width=9, height=3, command=lambda: onClick("*"))
    multi.grid(row=3, column=3)

    num4 = tkinter.Button(frame_left, text="4", width=9, height=3, command=lambda: onClick(4))
    num4.grid(row=4, column=0)

    num5 = tkinter.Button(frame_left, text="5", width=9, height=3, command=lambda: onClick(5))
    num5.grid(row=4, column=1)

    num6 = tkinter.Button(frame_left, text="6", width=9, height=3, command=lambda: onClick(6))
    num6.grid(row=4, column=2)

    sub = tkinter.Button(frame_left, text="-", width=9, height=3, command=lambda: onClick("-"))
    sub.grid(row=4, column=3)

    num1 = tkinter.Button(frame_left, text="1", width=9, height=3, command=lambda: onClick(1))
    num1.grid(row=5, column=0)

    num2 = tkinter.Button(frame_left, text="2", width=9, height=3, command=lambda: onClick(2))
    num2.grid(row=5, column=1)

    num3 = tkinter.Button(frame_left, text="3", width=9, height=3, command=lambda: onClick(3))
    num3.grid(row=5, column=2)

    add = tkinter.Button(frame_left, text="+", width=9, height=3, command=lambda: onClick("+"))
    add.grid(row=5, column=3)

    num0 = tkinter.Button(frame_left, text="0", width=20, height=3, command=lambda: onClick(0))
    num0.grid(row=6, column=0, columnspan=2)

    point = tkinter.Button(frame_left, text=".", width=9, height=3, command=lambda: onClick("."))
    point.grid(row=6, column=2)

    equals = tkinter.Button(frame_left, bg='yellow', text="=", width=9, height=3, command=lambda: onClick("="))
    equals.grid(row=6, column=3)

    # 清空运算历史
    def clean_history():

        for x in History_list:
            x.destroy()

    cls_button = tkinter.Button(frame_right, text="清空", command=clean_history)
    cls_button.pack(fill="x", side="top")
    print('功能：简单计算器')
    window.mainloop()

# *************************************进制转换模块************************************
def numsystem_trans():
    root.geometry('400x460') # 自定义选择后窗口大小
    root.title("进制转换")
    blank = tk.Label(root) # 遮挡前一次操作
    blank.place(x=0, y=0, width=400, height=460)
    te1 = tk.StringVar() # 创建可更新的变量
    te2 = tk.StringVar()

    def window():
        entry1 = tk.Entry(root, bg="#FFFACD",bd=5, font=('楷体', 30), justify='right', textvariable=te1) # 创建输入框
        entry1.place(x=10, y=10, width=380, height=50)
        entry2 = tk.Entry(root, font=('楷体', 30), bd=5, bg="#FFFACD", justify='right', textvariable=te2) # 创建结果框
        entry2.place(x=10, y=65, width=380, height=50)

        bD = tk.Button(root, text='D', font=('楷体', 18), command=lambda: numfun('d'))
        bD.place(x=10, y=125, width=50, height=50)
        bE = tk.Button(root, text='E', font=('楷体', 18), command=lambda: numfun('e'))
        bE.place(x=65, y=125, width=50, height=50)
        bF = tk.Button(root, text='F', font=('楷体', 18), command=lambda: numfun('f'))
        bF.place(x=120, y=125, width=50, height=50)
        b_1 = tk.Button(root, text='二进制→十进制', font=('楷体', 18), command=lambda: eqfun('二进制→十进制'))
        b_1.place(x=190, y=125, width=200, height=50)

        bA = tk.Button(root, text='A', font=('楷体', 18), command=lambda: numfun('a'))
        bA.place(x=10, y=180, width=50, height=50)
        bB = tk.Button(root, text='B', font=('楷体', 18), command=lambda: numfun('b'))
        bB.place(x=65, y=180, width=50, height=50)
        bC = tk.Button(root, text='C', font=('楷体', 18), command=lambda: numfun('c'))
        bC.place(x=120, y=180, width=50, height=50)
        b_2 = tk.Button(root, text='十进制→二进制', font=('楷体', 18), command=lambda: eqfun('十进制→二进制'))
        b_2.place(x=190, y=180, width=200, height=50)

        b7 = tk.Button(root, text='7', font=('楷体', 18), command=lambda: numfun('7'))
        b7.place(x=10, y=235, width=50, height=50)
        b8 = tk.Button(root, text='8', font=('楷体', 18), command=lambda: numfun('8'))
        b8.place(x=65, y=235, width=50, height=50)
        b9 = tk.Button(root, text='9', font=('楷体', 18), command=lambda: numfun('9'))
        b9.place(x=120, y=235, width=50, height=50)
        b_3 = tk.Button(root, text='八进制→十进制', font=('楷体', 18), command=lambda: eqfun('八进制→十进制'))
        b_3.place(x=190, y=235, width=200, height=50)

        b4 = tk.Button(root, text='4', font=('楷体', 18), command=lambda: numfun('4'))
        b4.place(x=10, y=290, width=50, height=50)
        b5 = tk.Button(root, text='5', font=('楷体', 18), command=lambda: numfun('5'))
        b5.place(x=65, y=290, width=50, height=50)
        b6 = tk.Button(root, text='6', font=('楷体', 18), command=lambda: numfun('6'))
        b6.place(x=120, y=290, width=50, height=50)
        b_4 = tk.Button(root, text='十进制→八进制', font=('楷体', 18), command=lambda: eqfun('十进制→八进制'))
        b_4.place(x=190, y=290, width=200, height=50)

        b1 = tk.Button(root, text='1', font=('楷体', 18), command=lambda: numfun('1'))
        b1.place(x=10, y=345, width=50, height=50)
        b2 = tk.Button(root, text='2', font=('楷体', 18), command=lambda: numfun('2'))
        b2.place(x=65, y=345, width=50, height=50)
        b3 = tk.Button(root, text='3', font=('楷体', 18), command=lambda: numfun('3'))
        b3.place(x=120, y=345, width=50, height=50)
        b_5 = tk.Button(root, text='十六进制→十进制', font=('楷体', 18), command=lambda: eqfun('十六进制→十进制'))
        b_5.place(x=190, y=345, width=200, height=50)

        b0 = tk.Button(root, text='0', font=('楷体', 18), command=lambda: numfun('0'))
        b0.place(x=10, y=400, width=50, height=50)
        bc = tk.Button(root, text='DEL', font=('楷体', 18), command=lambda: cefun())
        bc.place(x=65, y=400, width=50, height=50)
        bc.configure(background="gray")
        bce = tk.Button(root, text='AC', font=('楷体', 18), command=lambda: cfun())
        bce.place(x=120, y=400, width=50, height=50)
        bce.configure(background="red")
        b_6 = tk.Button(root, text='十进制→十六进制', font=('楷体', 18), command=lambda: eqfun('十进制→十六进制'))
        b_6.place(x=190, y=400, width=200, height=50)

    def numfun(n): # 输入数字
        if n == '0': # 防止输入格式出错
            if te1.get() != '0':
                te1.set(te1.get() + n)
        else:
            te1.set(te1.get() + n)

    def cfun(): # 清空
        te1.set('')
        te2.set('')

    def cefun(): # 退格
        if len(te1.get()) >= 1:
            te1.set(te1.get()[0:-1])

    def eqfun(op): # 进制转换
        ope = op
        s = 0
        t1 = str(te1.get()) # 将输入转换成字符串
        if ope == '二进制→十进制':
            for i in t1: # 检验输入是否只有0和1
                if i in ['0', '1']:
                    s = s + 1
            if s == len(t1):
                t2 = int(t1, 2) # 进制转换
                te2.set(str(t2))
            else:
                te2.set('二进制数输入错误！')
        elif ope == '十进制→二进制':
            for i in t1:
                if i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    s = s + 1
                if s == len(t1):
                    t2 = bin(int(t1))
                    te2.set(str(t2))
                else:
                    te2.set('十进制数输入错误！')
        elif ope == '八进制→十进制':
            for i in t1:
                if i in ['0', '1', '2', '3', '4', '5', '6', '7']:
                    s = s + 1
                if s == len(t1):
                    t2 = int(t1, 8)
                    te2.set(str(t2))
                else:
                    te2.set('八进制数输入错误！')
        elif ope == '十进制→八进制':
            for i in t1:
                if i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    s = s + 1
                if s == len(t1):
                    t2 = oct(int(t1))
                    te2.set(str(t2))
                else:
                    te2.set('十进制数输入错误！')
        elif ope == '十六进制→十进制':
            for i in t1:
                if i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']:
                    s = s + 1
                if s == len(t1):
                    t2 = int(t1, 16)
                    te2.set(str(t2))
                else:
                    te2.set('十六进制数输入错误！')

        elif ope == '十进制→十六进制':
            for i in t1:
                if i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    s = s + 1
                if s == len(t1):
                    t2 = hex(int(t1))
                    te2.set(str(t2))
                else:
                    te2.set('十进制数输入错误！')

    window()
    print('功能：进制转换')

# *************************************一元二次模块************************************
def equation_solve_twice():
    root.geometry('320x290')
    root.title("解一元二次方程")
    blank = tk.Label(root)
    blank.place(width=320, height=290)
    u1 = tk.StringVar()
    u2 = tk.StringVar()
    u3 = tk.StringVar()
    tx1 = tk.StringVar()
    tx2 = tk.StringVar()

    def quaW2():

        l = tk.Label(root, text='请输入方程对应系数', font=('楷体', 20))
        l.place(x=10, y=10, width=300, height=60)

        lti1 = tk.Label(root, text='ax^2+bx+c=0', font=('楷体', 20))
        lti1.place(x=10, y=60, width=300, height=40)

        la = tk.Label(root, text='a', font=('楷体', 20))
        la.place(x=10, y=100, width=40, height=40)

        lb = tk.Label(root, text='b', font=('楷体', 20))
        lb.place(x=10, y=160, width=40, height=40)

        lc = tk.Label(root, text='c', font=('楷体', 20))
        lc.place(x=10, y=220, width=40, height=40)

        ea = tk.Entry(root, textvariable=u1, bg='gainsboro', fg='black', font=('楷体', 20))  # 从键盘输入a的值
        ea.place(x=70, y=100, width=60, height=40)

        eb = tk.Entry(root, textvariable=u2, bg='gainsboro', fg='black', font=('楷体', 20))  # 从键盘输入b的值
        eb.place(x=70, y=160, width=60, height=40)

        ec = tk.Entry(root, textvariable=u3, bg='gainsboro', fg='black', font=('楷体', 20))  # 从键盘输入c的值
        ec.place(x=70, y=220, width=60, height=40)

        lx1 = tk.Label(root, text='x1', font=('楷体', 20))
        lx1.place(x=140, y=100, width=40, height=40)
        lx1p = tk.Label(root, textvariable=tx1, bg='gainsboro', fg='black', font=('楷体', 15))  # x1
        lx1p.place(x=190, y=100, width=100, height=40)

        lx2 = tk.Label(root, text='x2', font=('楷体', 20))
        lx2.place(x=140, y=160, width=40, height=40)
        lx2p = tk.Label(root, textvariable=tx2, bg='gainsboro', fg='black', font=('楷体', 15))  # x2
        lx2p.place(x=190, y=160, width=100, height=40)

        b1 = tk.Button(root, text='确定', command=quaC2)
        b1.place(x=190, y=220, width=50, height=40)
        b1.configure(background="red")

    def quaC2():
        try:
            a = eval(u1.get())
            b = eval(u2.get())
            c = eval(u3.get())
            deta = b * b - 4 * a * c

            if a == 0:
                tk.messagebox.showwarning(title='error', message='请输入正确的一元二次方程系数')
            else:
                re = (-b) / (2 * a)
                if deta < 0:
                    im = (math.sqrt(-deta)) / (2 * a)
                    if re == 0:
                        tx1.set('+{:.2}j'.format(im))
                        tx2.set('-{:.2}j'.format(im))
                    else:
                        tx1.set('{:.2}+{:.2}j'.format(re, im))
                        tx2.set('{:.2}-{:.2}j'.format(re, im))
                else:
                    im = (math.sqrt(deta)) / (2 * a)
                    tx1.set('{:.2}'.format(re + im))
                    tx2.set('{:.2}'.format(re - im))
        except:
            tk.messagebox.showwarning(title='error', message='请输入正确的一元二次方程系数')

    quaW2()
    print('功能：解一元二次方程')

# *************************************统计模块***************************************
def statistics():
    root.geometry('400x460')
    root.title("统计")
    blank = tk.Label(root)
    blank.place(width=400, height=460)
    te1 = tk.StringVar()
    te2 = tk.StringVar()
    te3 = tk.StringVar()
    te4 = tk.StringVar()

    def window():
        entry1 = tk.Entry(root, bg="#FFFACD", bd=5, font=('楷体', 20), justify='right', textvariable=te1)
        entry1.place(x=10, y=10, width=380, height=50)
        entry2 = tk.Entry(root, font=('微软雅黑', 20), bd=5, bg="#FFFACD", justify='right', textvariable=te2)
        entry2.place(x=10, y=55, width=380, height=50)
        entry3 = tk.Entry(root, font=('微软雅黑', 20), bd=5, bg="#FFFACD", justify='right', textvariable=te3)
        entry3.place(x=10, y=95, width=380, height=50)
        entry4 = tk.Entry(root, font=('微软雅黑', 20), bd=5, bg="#FFFACD", justify='right', textvariable=te4)
        entry4.place(x=10, y=135, width=380, height=50)

        b7 = tk.Button(root, text='7', font=('楷体', 18), command=lambda: numfun('7'))
        b7.place(x=10, y=195, width=80, height=60)
        b8 = tk.Button(root, text='8', font=('楷体', 18), command=lambda: numfun('8'))
        b8.place(x=113, y=195, width=80, height=60)
        b9 = tk.Button(root, text='9', font=('楷体', 18), command=lambda: numfun('9'))
        b9.place(x=216, y=195, width=80, height=60)
        bc = tk.Button(root, text='DEL', font=('楷体', 18), command=lambda: cefun())
        bc.place(x=319, y=195, width=70, height=60)
        bc.configure(background="gray")

        b4 = tk.Button(root, text='4', font=('楷体', 18), command=lambda: numfun('4'))
        b4.place(x=10, y=260, width=80, height=60)
        b5 = tk.Button(root, text='5', font=('楷体', 18), command=lambda: numfun('5'))
        b5.place(x=113, y=260, width=80, height=60)
        b6 = tk.Button(root, text='6', font=('楷体', 18), command=lambda: numfun('6'))
        b6.place(x=216, y=260, width=80, height=60)
        bce = tk.Button(root, text='AC', font=('楷体', 18), command=lambda: cfun())
        bce.place(x=319, y=260, width=70, height=60)
        bce.configure(background="red")

        b1 = tk.Button(root, text='1', font=('楷体', 18), command=lambda: numfun('1'))
        b1.place(x=10, y=325, width=80, height=60)
        b2 = tk.Button(root, text='2', font=('楷体', 18), command=lambda: numfun('2'))
        b2.place(x=113, y=325, width=80, height=60)
        b3 = tk.Button(root, text='3', font=('楷体', 18), command=lambda: numfun('3'))
        b3.place(x=216, y=325, width=80, height=60)
        b_1 = tk.Button(root, text='=', font=('楷体', 18), command=lambda: eqfun())
        b_1.place(x=319, y=325, width=70, height=125)
        b_1.configure(background="yellow")

        b0 = tk.Button(root, text='0', font=('楷体', 18), command=lambda: numfun('0'))
        b0.place(x=10, y=390, width=80, height=60)
        b_2 = tk.Button(root, text='.', font=('楷体', 18), command=lambda: numfun('.'))
        b_2.place(x=113, y=390, width=80, height=60)
        b_3 = tk.Button(root, text=',', font=('楷体', 18), command=lambda: numfun(','))
        b_3.place(x=216, y=390, width=80, height=60)

    def numfun(n): #输入数字
        te1.set(te1.get() + n)

    def cfun(): # 清空
        te1.set('')
        te2.set('')
        te3.set('')
        te4.set('')

    def cefun(): # 退格
        if len(te1.get()) >= 1:
            te1.set(te1.get()[0:-1])
        else:
            te1.set('')
        te2.set('')
        te3.set('')
        te4.set('')

    def eqfun(): #统计
        try:
            l1 = str(te1.get()).split(',') # 分割元素
            n = len(l1)
            sum1, sum2 = 0, 0
            for i in range(n):
                sum1 = sum1 + eval(l1[i])
            average = sum1 / n
            l2 = sorted(l1)
            if n % 2 == 0:
                median = (eval(l2[int(n / 2 - 1)]) + eval(l2[int(n / 2)])) / 2 # 求中位数
            else:
                median = eval(l2[int(n / 2)]) # 求中位数
            for j in range(n):
                sum2 = sum2 + pow((eval(l1[j]) - average), 2)
            standard_deviation = math.sqrt((sum2 / (n - 1))) # 求标准差
            te2.set('平均数: {:.2f}'.format(average))
            te3.set('中位数: {:.2f}'.format(median))
            te4.set('标准差: {:.2f}'.format(standard_deviation))
        except:
            te2.set('平均数: 错误')
            te3.set('中位数: 错误')
            te4.set('标准差: 错误')

    window()
    print('功能：统计计算')

# *************************************积分模块***************************************
def Integrater():
    root.geometry('400x460')  # 自定义选择后窗口大小
    root.title("积分")
    blank = tk.Label(root)
    blank.place(x=0, y=0, width=400, height=460)
    f_str: StringVar = tk.StringVar()

    def window():

        entry1 = tk.Entry(root, bg="#FFFACD", bd=5, font=('楷体', 20), justify='right', textvariable=f_str)
        entry1.place(x=10, y=10, width=380, height=50)

        b11 = tk.Button(root, text='integrate', font=('楷体', 11), command=lambda: numfun('integrate'))
        b11.place(x=10, y=65, width=80, height=60)
        b11.configure(background="red")
        b12 = tk.Button(root, text='(', font=('楷体', 18), command=lambda: numfun('('))
        b12.place(x=113, y=65, width=80, height=60)
        b12.configure(background="blue")
        b13 = tk.Button(root, text=')', font=('楷体', 18), command=lambda: numfun(')'))
        b13.place(x=216, y=65, width=80, height=60)
        b13.configure(background="blue")
        b14 = tk.Button(root, text='x', font=('楷体', 18), command=lambda: numfun('x'))
        b14.place(x=319, y=65, width=70, height=60)
        b14.configure(background="red")

        b21 = tk.Button(root, text='+', font=('楷体', 18), command=lambda: numfun('+'))
        b21.place(x=10, y=130, width=80, height=60)
        b22 = tk.Button(root, text='-', font=('楷体', 18), command=lambda: numfun('-'))
        b22.place(x=113, y=130, width=80, height=60)
        b23 = tk.Button(root, text='*', font=('楷体', 18), command=lambda: numfun('*'))
        b23.place(x=216, y=130, width=80, height=60)
        b24 = tk.Button(root, text='/', font=('楷体', 18), command=lambda: numfun('/'))
        b24.place(x=319, y=130, width=70, height=60)

        b31 = tk.Button(root, text='7', font=('楷体', 18), command=lambda: numfun('7'))
        b31.place(x=10, y=195, width=80, height=60)
        b32 = tk.Button(root, text='8', font=('楷体', 18), command=lambda: numfun('8'))
        b32.place(x=113, y=195, width=80, height=60)
        b33 = tk.Button(root, text='9', font=('楷体', 18), command=lambda: numfun('9'))
        b33.place(x=216, y=195, width=80, height=60)
        b34 = tk.Button(root, text='←', font=('楷体', 18), command=lambda: cefun())
        b34.place(x=319, y=195, width=70, height=60)

        b41 = tk.Button(root, text='4', font=('楷体', 18), command=lambda: numfun('4'))
        b41.place(x=10, y=260, width=80, height=60)
        b42 = tk.Button(root, text='5', font=('楷体', 18), command=lambda: numfun('5'))
        b42.place(x=113, y=260, width=80, height=60)
        b43 = tk.Button(root, text='6', font=('楷体', 18), command=lambda: numfun('6'))
        b43.place(x=216, y=260, width=80, height=60)
        b44 = tk.Button(root, text='AC', font=('楷体', 18), command=lambda: cfun())
        b44.place(x=319, y=260, width=70, height=60)
        b44.configure(background="red")

        b51 = tk.Button(root, text='1', font=('楷体', 18), command=lambda: numfun('1'))
        b51.place(x=10, y=325, width=80, height=60)
        b52 = tk.Button(root, text='2', font=('楷体', 18), command=lambda: numfun('2'))
        b52.place(x=113, y=325, width=80, height=60)
        b53 = tk.Button(root, text='3', font=('楷体', 18), command=lambda: numfun('3'))
        b53.place(x=216, y=325, width=80, height=60)
        b54 = tk.Button(root, text='=', font=('楷体', 18), command=lambda: eqfun(f_str))
        b54.place(x=319, y=325, width=70, height=125)
        b54.configure(background="yellow")

        b61 = tk.Button(root, text='0', font=('楷体', 18), command=lambda: numfun('0'))
        b61.place(x=10, y=390, width=80, height=60)
        b62 = tk.Button(root, text='.', font=('楷体', 18), command=lambda: numfun('.'))
        b62.place(x=113, y=390, width=80, height=60)
        b63 = tk.Button(root, text=',', font=('楷体', 18), command=lambda: numfun(','))
        b63.place(x=216, y=390, width=80, height=60)

    def numfun(n):  # 输入
        f_str.set(f_str.get() + n)

    def cfun():  # 清空
        f_str.set('')

    def cefun():  # 退格
        if len(f_str.get()) >= 1:
            f_str.set(f_str.get()[0:-1])
        else:
            f_str.set('')

    def eqfun(f_str):
        try:
            x = symbols('x')
            tmp = {'x': x, 'integrate': integrate}
            result = eval(f_str.get(), tmp)
            f_str.set(result)
        except:
            f_str.set('错误')

    window()
    print('功能：积分')

# *************************************帮助模块***************************************
def help1():
    root = tk.Tk()
    root.title('帮助')
    root.geometry('700x500')
    text = tk.Text(root, width=200, height=200, font=('微软雅黑', 12))
    text.place(x=0, y=0, width=700, height=500)
    text.insert("insert", '科学计算器：\n\n'
        '1、一元二次方程：\n输入格式：ax²+bx+c（系数为负数时将‘+’改为‘-’即可）\n计算结果时要按“一元二次”按键（不要按‘=’）\n\n'
        '2、进行位运算时，输出结果要按“位运算”按键（不要按‘=’）\n\n'
        '3、“十进制”和“二进制”按键只能进行计算结果的进制转换，使用时点击一次即可，不要多次点击，小数部分只转换小数点后三位，可能会造成部分失真……\n\n'
        '4、统计部分：输入样本数据时数据之间需要用‘,’隔开')
    print("功能：帮助")

# *************************************关于模块***************************************
def about():
    root = tk.Tk()
    root.title('关于')
    root.geometry('700x400')
    text = tk.Text(root, width=200, height=200, font=('微软雅黑', 12))
    text.place(x=0, y=0, width=700, height=500)
    text.insert("insert", '作者：\n吴毅东 2019212336\n\n版本：\nV1.0\n\n日期：\n2021.12.28')
    print('功能：关于')

# *************************************科学计算器模块**********************************
class calculator:
    def __init__(self):
        self.string = tk.StringVar()
        root.geometry('412x520')
        blank = tk.Label(root)
        blank.place(width=412, height=520)
        entry = tk.Entry(root,font=('楷体',30),bd=5,bg="#FFFACD", textvariable=self.string, )
        entry.grid(row=0, column=0, columnspan=6)
        entry.configure(background="white")
        entry.focus()

        values = ["AC", "DEL", "(", ")", "%", "gcd",
                  "sin", "sqrt", "e", "pow", "/", "radians",
                  "cos", "7", "8", "9", "*", "degrees",
                  "tan", "4", "5", "6", "-", "ceil",
                  "pi", "1", "2", "3", "+", "hypot",
                  "log", ",", "0", ".", "="]
        i = 0
        row = 1
        col = 0
        for txt in values:
            padx = 10
            pady = 10
            if i == 6:
                row = 2
                col = 0
            if i == 12:
                row = 3
                col = 0
            if i == 18:
                row = 4
                col = 0
            if i == 24:
                row = 5
                col = 0
            if i == 30:
                row = 6
                col = 0
            if txt == '=':
                btn = tk.Button(root,bd=5, height=2, width=4, padx=50, pady=pady, text=txt,
                             command=lambda txt=txt: self.equals())
                btn.grid(row=row, column=col, columnspan=3, padx=2, pady=2)
                btn.configure(background="yellow")

            elif txt == 'DEL':
                btn = tk.Button(root,bd=5, height=2, width=4, padx=padx, pady=pady, text=txt,
                             command=lambda txt=txt: self.delete())
                btn.grid(row=row, column=col, padx=1, pady=1)
                btn.configure(background="grey")
            elif txt == 'AC':
                btn = tk.Button(root,bd=5, height=2, width=4, padx=padx, pady=pady, text=txt,
                             command=lambda txt=txt: self.clearall())
                btn.grid(row=row, column=col, padx=1, pady=1)
                btn.configure(background="red")
            else:
                btn = tk.Button(root,bd=5, height=2, width=4, padx=padx, pady=pady, text=txt,
                             command=lambda txt=txt: self.addChar(txt))
                btn.grid(row=row, column=col, padx=1, pady=1)
                btn.configure(background="white")
            col = col + 1
            i = i + 1
        menubar()
        root.mainloop()

    def clearall(self):
        self.string.set("")

    def equals(self):
        try:
            result = eval(self.string.get())
            self.string.set(result)
        except:
            result = "无效输入"
        self.string.set(result)

    def addChar(self, char):
        i = ['log', 'sqrt', 'pi', 'sin', 'cos', 'tan', 'e', "gcd", "radians", "degrees", "ceil", "hypot"]
        if char in i:
            self.string.set(self.string.get() + 'math.' + (str(char)))
        else:
            self.string.set(self.string.get() + (str(char)))

    def delete(self):
        self.string.set(self.string.get()[0:-1])

calculator()