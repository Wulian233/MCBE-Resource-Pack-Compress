 ### 基岩版资源包压缩工具
  
 ![请联网查看图片](http://horrion.top/saomu/1.png)
[![Github All Releases](https://img.shields.io/github/downloads/Wulian233/MCBE-Resource-Pack-Compress/total.svg)]()
 ## 怎么使用？
 
 这里有两种使用方式：**下载EXE程序**，方便快捷，但是体积大；**.py源代码**，需要安装Python环境，比第一种较复杂，但一劳永逸。请自行斟酌使用。

 1. EXE方法：前往本项目的[Releases](https://github.com/Wulian233/MCBE-Resource-Pack-Compress/releases/)页面下载exe文件，解压使用。
 2. 源代码方法：前往本项目的[Releases](https://github.com/Wulian233/MCBE-Resource-Pack-Compress/releases/)页面下载源代码zip并解压。之后安装Python解释器，win10及以上安装[最新版](https://www.python.org/downloads/release/python-3105/)即可。win7最高支持[3.8.6](https://www.python.org/downloads/release/python-386/)版本，请一定安装正确的版本。最后双击main.py文件即可。
 
 ## 压缩原理是什么？
 
 我一共用了三种压缩方式，以下是具体原理：
 1. 将资源包解压再压缩；
 2. 将所有json文件中的空格替换为空；
 3. 删除所有.mcstructure的无用文件。
 
 ## 功能提议＆问题反馈
 发现问题？功能提议？可以通过我的QQ：`1055917385`或者邮件`1055917385@qq.com`联系我！B站私信[捂脸祖](https://m.bilibili.com/space/449728222/)也可
 
 不过有没有发现[问题追踪器](https://github.com/Wulian233/MCBE-Resource-Pack-Compress/issues)呢？在这儿提交问题，功能提议也可以。以上方式我都会看并回复的！
  
 ## 附程序exe构建方法
 - 既然看到这里，默认你有python基础，细节将略过。
 1. 安装pyinstaller模块；
 2. 进入main.py的根目录，在终端中输入`pyinstaller main.spec`；
 3. 构建完成后，在dist文件夹中既为你构建的exe程序。
