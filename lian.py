import tkinter as tk
import tkinter.messagebox

window=tk.Tk()
window.title('deelianOnline')
sw = window.winfo_screenwidth()
#得到屏幕宽度
sh = window.winfo_screenheight()*0.9
#得到屏幕高度
ww = 500
wh = 300
#窗口宽高为100
x = (sw-ww) / 2
y = (sh-wh) / 2
window.geometry("%dx%d+%d+%d" %(ww,wh,x,y))
window.resizable(0,0)

# 第4步，在图形界面上创建一个标签用以显示内容并放置
l = tk.Label(window, text='      ', bg='green')
l.pack()

#newPage
# Url_input = tk.Toplevel(window)
# Url_input.geometry('300x200')
# Url_input.title('Url Info')

Url = tk.StringVar()
tk.Label(window, text="目标Url:").place(x=70, y=40)
tk.Entry(window, textvariable=Url, width=39).place(x=130, y=40)

# checkType
requestType = ''
var = tk.StringVar()
tk.Label(window, text="请求方式:").place(x=70, y=70)
tk.Radiobutton(window, text='GET', variable=var, value='GET').place(x=130,y=70)
tk.Radiobutton(window, text='POST', variable=var, value='POST').place(x=230,y=70)

# endTime
EndTime = tk.StringVar()
tk.Label(window, text='持续时间:').place(x=70, y=100)
tk.Entry(window, textvariable=EndTime).place(x=130, y=100)

# controlButton
tk.Button(window, text='  Start  ').place(x=80, y=200)
tk.Button(window, text='  Stop  ').place(x=150, y=200)
tk.Button(window, text='  Reset  ').place(x=230, y=200)

# 第10步，定义一个函数功能，用来代表菜单选项的功能，这里为了操作简单，定义的功能比较简单
counter = 0
def do_job():
    global counter
    l.config(text='do ' + str(counter))
    counter += 1
def do_about():
    tkinter.messagebox.showinfo('About deelianOnline', 'Author: deelian\nEmail: deelian@qq.com\nVersion: 2.0.3')
def do_update():
    pass

# 第5步，创建一个菜单栏，这里我们可以把他理解成一个容器，在窗口的上方
menubar = tk.Menu(window)
# 第6步，创建一个File菜单项（默认不下拉，下拉内容包括New，Open，Save，Exit功能项）
filemenu = tk.Menu(menubar, tearoff=0)
# 将上面定义的空菜单命名为File，放在菜单栏中，就是装入那个容器中
menubar.add_cascade(label='File', menu=filemenu)
# 在File中加入New、Open、Save等小菜单，即我们平时看到的下拉菜单，每一个小菜单对应命令操作。
filemenu.add_command(label='New', command=do_job)
filemenu.add_command(label='Open', command=do_job)
filemenu.add_command(label='Save', command=do_job)
filemenu.add_separator()  # 添加一条分隔线
filemenu.add_command(label='Exit', command=window.quit)  # 用tkinter里面自带的quit()函数
# 第7步，创建一个Edit菜单项（默认不下拉，下拉内容包括Cut，Copy，Paste功能项）
editmenu = tk.Menu(menubar, tearoff=0)
# 将上面定义的空菜单命名为 Edit，放在菜单栏中，就是装入那个容器中
menubar.add_cascade(label='Help', menu=editmenu)
# 同样的在 Edit 中加入Cut、Copy、Paste等小命令功能单元，如果点击这些单元, 就会触发do_job的功能
editmenu.add_command(label='About', command=do_about)
editmenu.add_command(label='Check for Update', command=do_update)
# 第8步，创建第二级菜单，即菜单项里面的菜单
submenu = tk.Menu(filemenu)  # 和上面定义菜单一样，不过此处实在File上创建一个空的菜单
filemenu.add_cascade(label='Import', menu=submenu, underline=0)  # 给放入的菜单submenu命名为Import
# 第9步，创建第三级菜单命令，即菜单项里面的菜单项里面的菜单命令（有点拗口，笑~~~）
submenu.add_command(label='Submenu_1', command=do_job)  # 这里和上面创建原理也一样，在Import菜单项中加入一个小菜单命令Submenu_1
# 第11步，创建菜单栏完成后，配置让菜单栏menubar显示出来
window.config(menu=menubar)

window.mainloop()