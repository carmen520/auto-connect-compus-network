# auto-connect-compus-network
disconnection detection, automatic connection, remote control of campus computers

# 一、基于锐捷客户端实现的MentoHUST工具

查看了一下这个工具应该只适用于通过锐捷客户端登陆校园网的方式，而我们的校园网是通过网页端登陆的

客户端可参照该教程：https://blog.csdn.net/u013546553/article/details/120433030

# 二、基于网页登陆实现自动连接的方法（无脑就用，直接看下面第4点）

## 1.查看登陆页面的请求方式(此步骤仅影响后续学号和密码的填写位置)


在登陆界面上F12切换到“网络”栏，后点击登录，查看“请求方式”
![image](https://github.com/carmen520/auto-connect-compus-network/assets/52569696/fd579633-4ec9-469a-9f95-f705be5d54ce)

通常有两种请求方式，GET和POST


请求方式大部分为POST，后文内容均基于POST方式撰写，GET方式更简单，可看文末的参考教程，自行修改代码尝试。

## 2.整体思路
（1）使用程序操纵浏览器打开网页


（2）通过查看**成功联网页面**的HTML代码，找到登录成功的“标志性”“元素”作为判断器

这里的思路有两条

a：直接调出HTML后台，看代码中有哪些标志性元素  此思路代表了下文的方法1，对应auto_connect1.py代码的内容


b：观察页面设计，先从页面设计中找到标志性文字，再调出HTML后台，通过”在页面中选择一个元素以进行检查“功能，找到对应页面位置的HTML代码的对应元素   此思路代表了下文的方法2，对应auto_connect2.py代码的内容


（3）设置定时的死循环，判断器作为条件，当判断器的输出非标志性元素时，跳转到**登录页面**，执行登录操作


## 3.方法二为例，详细描述实现上述过程
（1）使用 Python 的 selenium 库来操作网页元素;

（2）通过网页寻找登录成功的标志性元素作为判断器内容


查找标志元素html后台对应的变量名称
（按F12键来打开，来查找和检查元素。如果你想要找到一个特定的元素，比如ID为"userMessage"的元素）

按照以下步骤操作：


a：打开开发者工具：在浏览器页面上按F12键。在开发者工具的"Elements"（元素）面板中，你可以看到网页的HTML结构。


b：在"Elements"面板中，点击左上角的箭头图标（或按快捷键Ctrl+Shift+C）进入选择元素模式。


c：在网页上选择需要查看的元素，开发者工具会在"Elements"面板中定位到该元素的HTML代码。


d：在这个HTML代码中，你可以看到元素的ID，比如id="userMessage"。如果你想要通过JavaScript来获取这个元素，你可以使用document.getElementById("userMessage")。这个方法会返回一个表示ID属性与"userMessage"相匹配的元素的Element对象

这里我们用上述方法找到登录成功时网页的标志性语言"您已成功连接校园网！"这句话对应的html变量id=“userMessage”

![捕获](https://github.com/carmen520/auto-connect-compus-network/assets/52569696/51008192-a67f-4aa5-80b9-90031a6e5973)

![image](https://github.com/carmen520/auto-connect-compus-network/assets/52569696/fcc71ef6-52b8-4d79-a6ca-d33ba90e3285)

（3）设置每10分钟检测一次的无限循环检测器，利用上面的判断器

检测“登录成功页面”，如果判断器的输出非false则表示连接正常


检测“登录成功页面”，如果判断其的输出为false表示连接断开，跳到登录页面URL

之后找到“用户名”“请输入密码”“登录”这三个按钮在html后台对应的元素
（按F12键来打开，来查找和检查元素。）

按照以下步骤操作：


a：打开开发者工具：在浏览器页面上按F12键。在开发者工具的"Elements"（元素）面板中，你可以看到网页的HTML结构。


b：在"Elements"面板中，点击左上角的箭头图标（或按快捷键Ctrl+Shift+C）进入选择元素模式。


c：在网页上选择需要查看的元素，开发者工具会在"Elements"面板中定位到该元素的HTML代码。


d：在这个HTML代码中，你可以看到对应的元素名称。

使用 CSS 选择器来指挥浏览器查找指定元素，并填入程序中提供的对应信息（send_keys）

![image](https://github.com/carmen520/auto-connect-compus-network/assets/52569696/4506c5c9-fa58-4ff9-ba59-1bec7096903c)

## 4.安装依赖

（1）安装运行需要的依赖库，`requirements.txt`。
   ***这里selenium库需要更新到最新，否则后面会出现程序报错***
   
   pip install --upgrade selenium


（2） 浏览器驱动，如edge、Chrome等。
   
   原理教程：https://learn.microsoft.com/zh-cn/microsoft-edge/webdriver-chromium/?tabs=c-sharp


   a：***对应好自己的版本号，否则可能失败。***

   
   b：存放位置在浏览器安装目录或者要运行的项目内。
   
   本项目文件夹中的驱动文件版本如图所示，请下载符合自己浏览器版本的驱动，并替换。

   
   c：将存放驱动的位置添加到环境变量中

   下文代码中使用的是`edge`浏览器和edge驱动

   ![edge版本号](https://learn.microsoft.com/zh-cn/microsoft-edge/webdriver-chromium/media/microsoft-edge-version.msft.png)

   驱动下载[地址](https://developer.microsoft.com/en-us/microsoft-edge/)

## 5.修改`auto_connect1.py`或者`auto_connect2.py`


1. 修改校园网账号、密码。
2. 其他学校需要修改判断器，DMU不需要修改
3. 测试url_login地址————》校园网登录页面地址
4. 测试url_check地址————》校园网成功登录页面地址


## 6.打包+后台运行

在项目目录打开终端，输入`pyinstaller -F auto_connect1.py`

添加-w 参数，这表示当我们执行打包好的.exe 程序时不会有黑框框出来，它会在后台运行

运行打包命令后，项目文件夹内会生成一个dist文件夹存放exe文件
![image](https://github.com/carmen520/auto-connect-compus-network/assets/52569696/bae4a86f-aac2-4b84-819d-62dffde7a481)


## 7.开机启动

目标：设置打包好的软件开机启动与每日早上6点启动。

具体图解查看教程：https://zhuanlan.zhihu.com/p/370801224

（1）右键此电脑然后点击管理

（2）选择左侧“系统工具”下的“任务计划程序”

（3）“创建基本任务”

（4）“触发器”的位置勾选“计算机启动时”，添加触发器，设置一个每天六点自动运行

（5）“操作”的位置勾选“启动程序”

（6）“启动程序”的位置“浏览”添加上面dist文件夹中的exe文件

（7）“完成”的位置，勾选“当单击完成时，打开此任务属性的对话框。当单机完成时，新任务将被创建并添加到windos计划中”

。。。。。
## 8.主机通电自动启动

设置被控电脑断电后再次来电时自启动。

惠普的电脑看以下教程：

https://h30471.www3.hp.com/t5/tai-shi-ji-zhi-shi-ku/jie-jue-fang-an-hui-pu-dian-nao-ru-he-she-zhi-tong-dian-zi-dong-kai-ji/ta-p/1221447

联想的电脑看以下教程：

通电启动[链接](https://jingyan.baidu.com/article/c1a3101efb30129e646deb7b.html)

## 三、测试结果

开机自动联网 get！

断电，来电后，电脑自启动 get！

来电后，电脑自启动+自动联网 get！

很完美～

# 四、合作者
感谢实验室的刘星师弟分享的auto_connect2.py文件的源码，基于他的思路和框架，做了微调和补充了auto_connect1.py代码

感谢https://zhuanlan.zhihu.com/p/370801224 这位作者的分享






