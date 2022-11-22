import requests
import yagmail   # 此模块用于发邮件
import schedule  # 此模块用于计划任务
from bs4 import BeautifulSoup
import re

ran = 0
url = 'https://tianqi.2345.com/xuancheng1d/58433.htm'  # 定义天气预报的url
loveurl = 'https://www.guaze.com/juzi/23389.html'  # 定义情话的url
def email():
    global ran      # 将ran变量声明为全局变量
    web = requests.get(url)
    # print(web.text)

    page = BeautifulSoup(web.text,"html.parser")

    # print(ran)

    # print(love[ran])

    weather = page.find("div",class_="real-today")
    # print(weather.text)

    web2 = requests.get(loveurl)
    web2.encoding = 'gb2312'
    page = BeautifulSoup(web2.text, "html.parser")

    div = page.find('div', class_="content")

    div = str(div.text)
    # print(div)
    grep = re.compile(r"\d+、(.*)")
    content = grep.findall(div)
    # print(content)


# email函数内的内容是爬取天气和情话的，具体的地址天气你可以更换url

    yag = yagmail.SMTP(
        host='smtp.qq.com', user='502643134@qq.com',   # 如过用的是qq邮箱就写smtp.qq.com，如果是163就写smtp.163.com
        password='nywcnfvkpkmfbjdj', smtp_ssl=True       # 授权码在qq邮箱里开启smtp就会生成一个
    )
    weather = [weather.text,"每日情话:",content[ran],    # 定义发送内容
               yagmail.inline(r"love.jpg")    # 附件图片，不发图片可以删掉
               ]
    yag.send(
        to=['502643134@qq.com'],
        subject='早鸭',           # 邮件主题
        contents=weather          # 发送的内容为上面定义的weather，其中weather.text是天气预报，content[ran]是情话
    )
    print("发送完成")
    ran += 1

schedule.every().day.at("05:21").do(email)      # 每天5点20分执行函数email0
schedule.every(30).seconds.do(email)  #每10秒执行一下函数email的内容，我这里用于测试
while True:
    schedule.run_pending()