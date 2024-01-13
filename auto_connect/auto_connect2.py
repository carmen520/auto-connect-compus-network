from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# 查看是否已经登录校园网
def is_net_connected(url_check):
    driver_test = webdriver.Edge()#Selenium WebDriver 的一个方法，用于启动 Edge 浏览器。
    driver_test.implicitly_wait(3)
    """
    设置了隐式等待时间为 3 秒。隐式等待是 WebDriver 的一种功能，如果 WebDriver 试图在页面上查找元素，
    但是该元素并未立即出现，隐式等待就会等待一段时间再查找元素。
    在这个例子中，如果元素在 3 秒内未出现，WebDriver 就会抛出一个异常。这样可以提高测试的稳定性，
    因为有时候网络延迟或者其他原因可能会导致元素加载较慢。这个设置在 WebDriver 实例存在期间一直有效。
    
    """
    try:
        driver_test.get(url_check)#让 WebDriver 打开一个新的浏览器窗口并导航到 url_check 所指定的 URL
        # 查询网页状态
        """
        使用元素的 ID 来查找元素，"userMessage" 是元素的 ID
        """
        online_text = driver_test.find_element('id', "userMessage").text#查找页面上 ID 为 “userMessage” 的元素，并获取该元素的文本内容
        driver_test.quit()#关闭浏览器窗口并退出 WebDriver
    except Exception as e:
        try:
            driver_test.quit()#这段代码尝试关闭浏览器窗口并退出 WebDriver。如果这个操作失败（例如，因为浏览器窗口已经被关闭或者 WebDriver 已经退出），代码不会抛出错误，而是执行 pass 语句。
                                #pass 语句在 Python 中的作用是什么都不做，它通常用在需要语法上需要一条语句，但是代码逻辑上不需要做任何操作的地方。
        except:
            pass
        print(e)
        return False

    # 连接成功时

    """
    这段代码的作用是检查网页上某个元素的文本内容，如果内容是 “您已成功连接互联网!”，那么函数返回 True，
    否则，函数尝试关闭浏览器窗口并退出 WebDriver，然后返回 False。

    """

    if online_text == "您已成功连接校园网!":#online_text =页面上 ID 为 “userMessage” 的元素
    
        print('success')
        return True
    else:
        try:
            driver_test.quit()
        except:
            pass
        return False


def main(url_check, url_login, username, password):
    while True:#这是一个无限循环，除非程序被强制停止，否则这个循环会一直运行。
        if is_net_connected(url_check):#如果网络已连接，那么执行 if 语句块中的代码；否则，执行 else 语句块中的代码。
            print("online!  fine!")
            time.sleep(600)  # 十分钟查询一次，防止偶然下线   程序暂停 600 秒（即十分钟）
        else:
            print("offline!  sad!")
            driver = webdriver.Edge()#创建一个新的 Microsoft Edge 浏览器实例
            try:
                driver.get(url_login)  # 打开校园网登录网页  让 WebDriver 打开一个新的浏览器窗口并导航到 url_login 所指定的 URL。

                time.sleep(3)  # 等待浏览器加载其他元素
                
                """
                在网页中查找一个元素。By.CSS_SELECTOR 表示我们使用 CSS 选择器来查找元素，'input[name="username"]' 是 CSS 选择器，
                表示我们要查找的是 <input> 标签，并且这个标签的 name 属性值为 "username"。
                """
                # CSS选择器选择输入用户名、密码的输入框 并输入用户名、密码               
                driver.find_element(By.CSS_SELECTOR, 
                                    'input[name="username"]').send_keys(username)#查找页面上名为 “username” 的输入框，并输入用户名。
                driver.find_element(By.CSS_SELECTOR,
                                    'input[type="password"').send_keys(password)#查找页面上类型为 “password” 的输入框，并输入密码。
                driver.find_element(By.CSS_SELECTOR,'button[type="submit"]').click()#查找页面上类型为 “submit” 的按钮，并点击它。

                time.sleep(2)#让程序暂停 2 秒，然后关闭浏览器窗口并退出 WebDriver。
                driver.quit()

            except Exception as e:
                print(e)
                driver.quit()#如果 try 块中的代码运行出错，那么打印出错误信息，并关闭浏览器窗口并退出 WebDriver。
            

if __name__ == "__main__":
    # 校园网账户密码
    username = '填学号'
    password = '填登录密码'

    #校园网登录页面地址  下面的网址是DMU，其他学校的同理换到自己学校的网址
    url_login = 'https://id.dlmu.edu.cn/login?service=http:%2F%2F202.118.88.9%2Feportal%2Findex.jsp%3Fwlanuserip%3De07fb2fafc5894e7fc8bb58517fd9352%26wlanacname%3Dc20f646d18ec8420743bb59779d3aa5d%26ssid%3D%26nasip%3D321b8c06ed4b01461a74c22a11633718%26snmpagentip%3D%26mac%3Da167cede885b0fe1e35253c2717a0db6%26t%3Dwireless-v2%26url%3Dba89be7f1fb5bf76c7c21d5e78a4bb46db7404fdfae1ba7ecb96f7d8f9ef275bc2ea29441f0f9b828e33c91b499b916b2877795b9a17c8b4d5b8df94bcddf2fa%26apmac%3D%26nasid%3Dc20f646d18ec8420743bb59779d3aa5d%26vid%3D6121f950533a4bd1%26port%3D1f897c6a120b51aa%26nasportid%3Dc6abed3ee205e3f81369f2aee75d9658793233c2c2ba139ad6600e266c032f8d7f91717f7fc80086'
    #校园网成功登录页面  下面的网址是DMU，其他学校的同理换到自己学校的网址
    url_check = 'http://202.118.88.9/eportal/success.jsp?userIndex=33323162386330366564346230313436316137346332326131313633333731385f3137322e32372e37322e3135365f30313230323030303131'
    main(url_check, url_login, username, password)

