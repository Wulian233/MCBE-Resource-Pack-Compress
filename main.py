import os
import zipfile
from tkinter import filedialog,messagebox
import tkinter.ttk
from webbrowser import open as web
import json
#我就要用中文命名变量，哼~
def 选文件():
    num=stater.get()
    路径 = filedialog.askopenfilename(filetypes=[("资源包", "*.mcpack")])
    前缀 = os.path.basename(路径).split('.')[0]
    os.rename(路径, 路径 + ".zip")
    路径2 = 路径 + ".zip"
    def json压缩():
        json数,结构数,材质 = 0,0,0
        files = os.listdir(前缀)
        for root,dirs , files in os.walk(前缀):
            for file in files:
                if file.endswith(".json"):
                    json数 += 1
                    print("path == ",file)
                    with open(os.path.join(root,file),'r') as load_f:
                        load_dict = json.load(load_f)
                    你好=len(load_dict)
                    for i in range (0,你好):#批量打开文件，将其中的空格替换为空
                        if load_dict == ' ':
                            load_dict = ''
                        with open(os.path.join(root,file),'w') as dump_f:
                            json.dump(load_dict, dump_f)
                elif file.endswith(".mcstructure"):
                    结构数 += 1
                    os.remove(os.path.join(root, file))
                elif file.endswith(".material"):
                    材质 += 1
                    print("path == ",file)
                    with open(os.path.join(root,file),'r') as load_f:
                        load_dict = json.load(load_f)
                    你好=len(load_dict)
                    for i in range (0,你好):
                        if load_dict == ' ':
                            load_dict = ''
                        with open(os.path.join(root,file),'w') as dump_f:
                            json.dump(load_dict, dump_f)
        if(json数 & 结构数== 0):
            messagebox.showinfo("提示","当前资源包已经被压缩或\n所选纹理包不存在任何json和mcstructure文件，压缩效果不明显！")
        else:
            messagebox.showinfo('提示','{}'.format(前缀)+'压缩成功！\n共压缩了{}个json文件'.format(json数)+'\n共压缩了{}个material文件'.format(材质)+'\n共删除了共{}个mcstructure文件'.format(结构数))
    with zipfile.ZipFile(路径2, 'r') as zip_ref:
        zip_ref.extractall(前缀)
        zip_ref.close()
        os.remove(路径2)
        def zip(模式):            #压缩全部文件
            with zipfile.ZipFile(前缀+".mcpack", 'w',模式) as zip_ref:
                for root, dirs, files in os.walk(前缀):
                    for file in files:
                        zip_ref.write(os.path.join(root, file))
            zip_ref.close()
            return 模式
    json压缩()
    if num==1:
        zip(zipfile.ZIP_DEFLATED)
    elif num==2:
        zip(zipfile.ZIP_LZMA)  
    os.system("rd /s /q " + 前缀)# 删除解压的文件夹
def 更新():
    messagebox.showinfo("更新内容","支持.material压缩，现在一些光影什么的压缩率更高；\n现在压缩成功后会显示文件的名字；\n代码优化，应该提高了点兼容性。")
def git():
    web('https://github.com/Wulian233/MCBE-Resource-Pack-Compress',new=1,autoraise=True)
def B站():
    web('https://space.bilibili.com/449728222',new=1,autoraise=True)
def 石():
    messagebox.askquestion("↑ 没事可以咬个打火石 ↓","少年，我看你才华横溢，仪表不凡，是个咬打火石的好苗子！确定咬吗？")
    web('https://minecraft.fandom.com/zh/wiki/打火石',new=1,autoraise=True)
def 啥():
    messagebox.showinfo("有什么区别？","一般地，LZMA压缩率高，但慢。默认是最好且最稳定的选择。")
def 原理():
    messagebox.showinfo("原理是什么 ？","这个方法很简单 ，我用了三种方法压缩：\n1. 将资源包解压再压缩；\n2. 将所有json和material内的空格替换为空；\n3. 对于投影资源包，删除所有.mcstructure文件。")
窗 = tkinter.Tk()
窗.title("基岩版通用资源包压缩工具")
窗.geometry("380x350")
窗.resizable(0,0)
tkinter.ttk.Label(窗,text="请选择一种压缩算法模式，推荐默认",font=("微软雅黑",11)).pack()
stater=tkinter.IntVar()
菜单 = tkinter.Menu(窗)
窗.config(menu = 菜单)
关于 = tkinter.Menu(菜单, tearoff=False)
关于.add_command(label="前往Github",font=("微软雅黑",10),command=git)
关于.add_command(label="作者B站",font=("微软雅黑",10),command=B站)
菜单.add_cascade(label="关于",font=("微软雅黑",11), menu=关于)
菜单.add_cascade(label="压缩原理",font=("微软雅黑",11), command=原理)
tkinter.ttk.Radiobutton(窗,text="默认",variable=stater,value=1,command=选文件).place(x=40,y=50)
tkinter.ttk.Radiobutton(窗,text="LZMA",variable=stater,value=2,command=选文件).place(x=120,y=50)
tkinter.ttk.Button(窗,text="？",command=啥,width=2).place(x=240,y=40)
tkinter.ttk.Button(窗,text="更新内容",command=更新,width=7).place(x=290,y=40)
tkinter.ttk.Button(窗,text="机",command=石).place(x=372,y=330)
tkinter.ttk.Label(窗,text="这个工具由捂脸（Wulian233）制作。\n对于投影可以压缩为原本的百分之一，原体\n积越大压缩率越大；UI、红石辅助类等资源包，\n也可以有效压缩。",font=("微软雅黑",11)).place(x=5,y=120)
tkinter.ttk.Label(窗,text="俗话说的好，不压缩浪费群友流量的都是耍流氓（bushi",font=("微软雅黑",9)).place(x=5,y=315)
窗.mainloop()