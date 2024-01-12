# auto-connect-compus-network
disconnection detection, automatic connection, remote control of campus computers

# 一、基于锐捷客户端实现的MentoHUST工具

查看了一下这个工具应该只适用于通过锐捷客户端登陆校园网的方式，而我们的校园网是通过网页端登陆的

客户端可参照该教程：https://blog.csdn.net/u013546553/article/details/120433030

# 二、基于网页登陆实现自动连接的方法

## 1.查看登陆页面的请求方式

在登陆界面上F12切换到“网络”栏，后点击登录，查看“请求方式”
![image](https://github.com/carmen520/auto-connect-compus-network/assets/52569696/fd579633-4ec9-469a-9f95-f705be5d54ce)

我的请求方式为POST

通常有两种请求方式，GET和POST

























![image](https://github.com/carmen520/auto-connect-compus-network/assets/52569696/fcc71ef6-52b8-4d79-a6ca-d33ba90e3285)



















![image](https://github.com/carmen520/auto-connect-compus-network/assets/52569696/4506c5c9-fa58-4ff9-ba59-1bec7096903c)
