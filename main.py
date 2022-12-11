import zipfile,os,json,sys,threading,sv_ttk,tkinter as tk
from tkinter import filedialog,scrolledtext,ttk,messagebox as 弹窗
from webbrowser import open as web
#我就要用中文命名变量，哼~

def 更新():
    弹窗.showinfo("更新内容","新增美化主题，页面变漂亮了！\n未选择文件会提示，不会报错。\n压缩成功后的弹窗代码层面用f-string，精简代码\nprint重定向到文本框，展示压缩文件及更多信息！")
def git():
    web('https://github.com/Wulian233/MCBE-Resource-Pack-Compress',new=1,autoraise=True)
def B站():
    web('https://space.bilibili.com/449728222',new=1,autoraise=True)
def 石():
    弹窗.showwarning("↑ 没事可以咬个打火石 ↓","少年，我看你才华横溢，仪表不凡，是个咬打火石的好苗子！")
    web('https://minecraft.fandom.com/zh/wiki/打火石',new=1,autoraise=True)
def 啥():
    弹窗.showinfo("有什么区别？","一般地，LZMA压缩率高，但慢。默认是最好且最稳定的选择。")
def 原理():
    弹窗.showinfo("原理是什么 ？","这个方法很简单 ，我用了三种方法压缩：\n1. 将资源包解压再压缩；\n2. 将所有json和material内的空格替换为空；\n3. 对于投影资源包，删除所有.mcstructure文件。")

def 选文件():
    算法=模式.get()
    路径 = filedialog.askopenfilename(filetypes=[("资源包", "*.mcpack")])
    前缀 = os.path.basename(路径).split('.')[0]
    try:
        os.rename(路径, 路径 + ".zip")
    except OSError as 原因:
        print('程序异常！因为你未选择任何文件！\n'+str(原因))
    else:
        os.rename(路径, 路径 + ".zip")
    路径2 = 路径 + ".zip"
    def 各种压缩():
        json数, 结构数, 材质 = 0, 0, 0
        files = os.listdir(前缀)
        for root,dirs , files in os.walk(前缀):
            for file in files:
                if file.endswith(".json"):
                    json数 += 1
                    print(f'path={file}')
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
                    print(f'path={file}')
                    with open(os.path.join(root,file),'r') as load_f:
                        load_dict = json.load(load_f)
                    你好=len(load_dict)
                    for i in range (0,你好):
                        if load_dict == ' ':
                            load_dict = ''
                        with open(os.path.join(root,file),'w') as dump_f:
                            json.dump(load_dict, dump_f)
        if(json数 & 结构数== 0):
            弹窗.showinfo("提示","当前资源包已经被压缩或\n所选纹理包不存在任何json和mcstructure文件，压缩效果不明显！")
            print("当前资源包已经被压缩或\n所选纹理包不存在任何json和mcstructure文件，压缩效果不明显！")
        else:
            弹窗.showinfo('提示',f'{前缀}压缩成功！\n共压缩了{json数}个json文件\n共压缩了{材质}个material文件\n共删除了共{结构数}个mcstructure文件')
            print(f'{前缀}压缩成功！\n共压缩了{json数}个json文件\n共压缩了{材质}个material文件\n共删除了共{结构数}个mcstructure文件')
    try:
       with zipfile.ZipFile(路径2, 'r') as zip_ref:
            zip_ref.extractall(前缀)
            zip_ref.close()
            os.remove(路径2)
            def zip(模式):#压缩全部文件
                with zipfile.ZipFile(前缀+".mcpack", 'w',模式) as zip_ref:
                    for root, dirs, files in os.walk(前缀):
                        for file in files:
                            zip_ref.write(os.path.join(root, file))
                zip_ref.close()
                return 模式
    except OSError as 原因:
        print(str(原因))
    else:
        with zipfile.ZipFile(路径2, 'r') as zip_ref:
            zip_ref.extractall(前缀)
            zip_ref.close()
            os.remove(路径2)
            def zip(模式):#压缩全部文件
                with zipfile.ZipFile(前缀+".mcpack", 'w',模式) as zip_ref:
                    for root, dirs, files in os.walk(前缀):
                        for file in files:
                            zip_ref.write(os.path.join(root, file))
                zip_ref.close()
                return 模式
    各种压缩()
    # 多线程 = threading.Thread(target=各种压缩)
    # 多线程.start()
    if 算法==1:
        zip(zipfile.ZIP_DEFLATED)
    elif 算法==2:
        zip(zipfile.ZIP_LZMA)  
    os.system("rd /s /q " + 前缀)#删除解压的文件夹


class StdoutRedirector(object):# 重定向输出类
    def __init__(self,text_widget):# 将其备份
        self.text_space = text_widget
        self.stdoutbak = sys.stdout
        self.stderrbak = sys.stderr
    def write(self, str):
        self.text_space.insert(tk.END, str)
        self.text_space.see(tk.END)
        self.text_space.update()
    def restoreStd(self):# 恢复标准输出
        sys.stdout = self.stdoutbak
        sys.stderr = self.stderrbak
    def flush(self):
        pass

窗 = tk.Tk()
sv_ttk.use_light_theme()
窗.title("基岩版通用资源包压缩工具")
窗.geometry("780x350+950+340")
窗.resizable(0,0)
输出框 = scrolledtext.ScrolledText(窗, relief="solid", width=36, height=13)
输出框.place(x=400, y=10)
输出框.insert('1.0','日志输出和压缩进度将在此显示\n')
sys.stdout = StdoutRedirector(输出框)
tk.Label(窗,text="请选择一种压缩算法模式，推荐默认",font=("微软雅黑",11)).place(x=50,y=5)
模式=tk.IntVar()
菜单 = tk.Menu(窗)
窗.config(menu = 菜单)
关于 = tk.Menu(菜单, tearoff=False)
关于.add_command(label="前往Github",font=("微软雅黑",10),command=git)
关于.add_command(label="作者B站",font=("微软雅黑",10),command=B站)
菜单.add_cascade(label="关于",font=("微软雅黑",11), menu=关于)
菜单.add_cascade(label="压缩原理",font=("微软雅黑",11), command=原理)
tk.ttk.Radiobutton(窗,text="默认",variable=模式,value=1,command=选文件).place(x=40,y=50)
tk.ttk.Radiobutton(窗,text="LZMA",variable=模式,value=2,command=选文件).place(x=120,y=50)
tk.ttk.Button(窗,text="？",command=啥,width=2).place(x=240,y=40)
tk.ttk.Button(窗,text="更新内容",command=更新,width=8).place(x=290,y=40)
tk.ttk.Button(窗,text="机",command=石).place(x=-1,y=342)
tk.Label(窗,text="这个工具由捂脸（Wulian233）制作。\n对于投影可以压缩为原本的百分之一，原体\n积越大压缩率越大；UI、红石辅助类等资源包，\n也可以有效压缩。",font=("微软雅黑",11)).place(x=5,y=120)
窗.mainloop()