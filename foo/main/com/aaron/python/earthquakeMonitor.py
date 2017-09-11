#!/usr/bin/python
# coding=utf-8

import requests
import json
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import time
import sys

reload(sys)
sys.setdefaultencoding('utf8')  # Function
# Get earthquake data by start time.
def getEarthquakeData(startTime):
    url = "http://api.dizhensubao.igexin.com/api.htm"
    action = "requestMonitorDataAction"
    dataSource = "CEIC"

    headers = {'Host': 'api.dizhensubao.igexin.com',
               'Content-Type': 'application/json',
               'Connection': 'keep-alive',
               'Accept': '*/*',
               'User-Agent': 'Earthquake/18 CFNetwork/811.4.18 Darwin/16.5.0',
               'Accept-Language': 'zh-cn',
               'Accept-Encoding': 'gzip, deflate',
               'Content-Length': 204}

    postData = {'action': action,
                'dataSource': dataSource,
                'startTime': startTime}
    postData = json.dumps(postData)

    res = requests.post(url, data=postData, headers=headers)

    return res.text


# print getEarthquakeData(153265449)

# Function
# Send email
def sendEmail(toEmail, subject, content):
    # Server info
    smtpHost = "smtp.qq.com"
    smtpPort = 465
    # Account info
    account = "793514146@qq.com"
    pwd = "ccwpryjtypbbga"
    fromEmail = "793514146@qq.com"
    fromName = "震长"

    try:
        smtpObj = smtplib.SMTP_SSL()
        smtpObj.connect(smtpHost, smtpPort)
        smtpObj.login(account, pwd)

        message = MIMEText(content, 'plain', 'utf-8')
        message['Subject'] = Header(subject, 'utf-8')
        message['From'] = Header(fromName + '<' + fromEmail + '>', 'utf-8')
        message['To'] = Header('<' + toEmail + '>', 'utf-8')
        smtpObj.sendmail(fromEmail, toEmail, message.as_string())
    # print "邮件发送成功"
    except smtplib.SMTPException:
        print("[ERROR]邮件发送失败：" + subject)


# sendEmail("676111404@qq.com", "测试", "这是内容")

# Function
# JSON value to message string
def valueToMsgstr(value):
    msg = "=====================\n"
    msg += "时间：" + dateLongToStr(value['time']) + "\n"
    msg += "地点：" + value['loc_name'] + "\n"
    msg += "震级：" + str(value['mag']) + "\n"
    msg += "深度：" + str(value['depth']) + "米\n"
    msg += "经度：" + str(value['longitude']) + "\n"
    msg += "纬度：" + str(value['latitude']) + "\n"
    return msg


# Function
# Format long date to string
def dateLongToStr(l):
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(l / 1000))


# Function
# Run function
def scanner(startTime):
    res = getEarthquakeData(startTime)
    res = json.loads(res)
    result = res["result"]
    if result == "OK":
        values = res["values"]
        tempTime = startTime
        for value in values:
            msg = valueToMsgstr(value)
            title = "地震信息：" + str(value['loc_name']) + str(value['mag']) + "级地震"
            time = value['time']
            if (time > tempTime):
                tempTime = time
                sendEmail("457623735@qq.com", title, msg)
        return tempTime


# Main
# 循环时间间隔(秒)
interval = 5
startTime = 1502643084000
while (1):
    tempTime = scanner(startTime)
    if (tempTime > startTime):
        print(tempTime)
    startTime = tempTime
    time.sleep(interval)
