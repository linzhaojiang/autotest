# 读取allure报告文件中"prometheusData.txt"文件，循环遍历获取需要的值。
import sys
import jenkins
from comment.readconfig import *
from comment.log import *
import requests
import json

sys.path.append("..")
def dd_test_group():
    # 获取当前日期
    tile = time.strftime("%Y-%m-%d %H:%M:%S")

    d = {}
    # proDir = "http://localhost:63342"	# 项目路径
    f = open('/Users/baofu/Documents/API-automation/reports/export/prometheusData.txt', 'r')	# prometheusData 全路径
    for lines in f:
        for c in lines:
            launch_name = lines.strip('\n').split(' ')[0]
            num = lines.strip('\n').split(' ')[1]
            d.update({launch_name: num})
    f.close()
    retries_run = d.get('launch_retries_run')  # 运行总数
    status_passed = d.get('launch_status_passed')  # 通过数量
    status_failed = d.get('launch_status_failed')  # 不通过数量
    status_broken = d.get('launch_status_broken')  # 异常数量

    url = "https://oapi.dingtalk.com/robot/send"
    querystring = {"access_token": "f1a28767e16c5640acb60c2fac1cba149a422a564e72fb7a1784b51bc279b5c8"}
    data = {

            "msgtype": "markdown",
            "markdown": {
                "title": "项目接口测试报告",
                "text": "<font color=\'#FFA500\'>[通知] </font>项目接口测试报告 \n\n --- \n\n"+
                        "项目名称：接口数据报告 \n\n "+
                        # "报告链接：%s" % 'http://127.0.0.1:63342/API-automation/reports/index.html?' +"\n\n"+
                        "监测分支：测试环境 \n\n"+"\n\n" +
                        "运行总数：%s" % retries_run +"\n\n"+
                        "通过数量：%s" % status_passed +"\n\n"+
                        "异常数量：%s" % status_broken + "\n\n"
                        "不通过数量：%s" % status_failed +"\n\n"+
                        "相关人员： @18676893330" +"\n\n"+
                        "</font> \n\n --- \n\n  **运行时间：** %s" %tile

            },
            "at": {
                "atMobiles": [
                    "18676893330"
                ],
                "isAtAll": False
            }
        }


    json_str = json.dumps(data)

    headers = {
        'content-type': "application/json"
            }
    response = requests.request("POST", url, data=json_str, headers=headers, params=querystring)
    print(response.text)

# if __name__ == '__main__':
#     dd_test_group()
