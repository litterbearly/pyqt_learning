> 本文由 [简悦 SimpRead](http://ksria.com/simpread/) 转码， 原文地址 https://blog.csdn.net/Dreamhai/article/details/82701063

Qt Designer 用于像 VC++ 的 MFC 一样拖放、设计控件

PyUIC 用于将 Qt Designer 生成的. ui 文件转换成. py 文件

Qt Designer 和 PyUIC 都包含在 PyQt5 中，所以我们只需要安装 PyQt5 塻块然后再指定 Qt Designer 和 PyUIC 即可

为了避免篇幅过长，本文只讲安装配置，使用可查看 “[PyCharm+QTDesigner+PyUIC 使用教程](https://www.cnblogs.com/lsdb/p/9122425.html)”

### 一、安装 PyQt5

Qt Designer 包含在 PyQt5 中，而 PyQt5 就是一个 python 模块，所以我们可以直接通过 “pip3 install PyQt5” 安装

但是我们这里使用 PyCharm 集成开发环境，所以直接通过 PyCharm 安装

打开 PyCharm，新建一个项目

![](https://images2018.cnblogs.com/blog/1116722/201806/1116722-20180601144541980-1770598007.png)

![](https://images2018.cnblogs.com/blog/1116722/201806/1116722-20180601144751056-232178231.png)

![](https://images2018.cnblogs.com/blog/1116722/201806/1116722-20180601144833913-761507535.png)

![](https://images2018.cnblogs.com/blog/1116722/201806/1116722-20180601144931950-1272981278.png)

### 二、指定 Qt Designer 和 PyUIC

![](https://images2018.cnblogs.com/blog/1116722/201806/1116722-20180601150258845-574171932.png)

 Name-- 输入最后工具在菜单中的想呈现名称，比如我这里命名为 QTDesigner

Program--designer.exe 程序的位置，位于当前所用解析器的 Lib\site-packages\pyqt5-tools\designer.exe

Working directory--designer.exe 工作路径，设置为 $ProjectFileDir$

 ![](https://images2018.cnblogs.com/blog/1116722/201806/1116722-20180601151605421-493411367.png)

类似地添加 PyUIC，

name----PyUIC

Program----PyUIC 位于当前解析器的 Scripts\pyuic5.exe

Arguments----$FileName$ -o $FileNameWithoutExtension$.py

Working dirctory----$ProjectFileDir$

![](https://images2018.cnblogs.com/blog/1116722/201806/1116722-20180601151811593-1976053363.png)

![](https://images2018.cnblogs.com/blog/1116722/201806/1116722-20180601152334463-1268558762.png)

回到主界面 “Tools”--“External Tools” 即可看到我们添加的 QTDesigner 和 PyUIC

![](https://images2018.cnblogs.com/blog/1116722/201806/1116722-20180601153447463-557288994.png)