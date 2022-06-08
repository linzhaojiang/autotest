import time
# 定义一个构造函数 每次执行前先获取

import jenkins
from py import log


def __init__(self):
    self.errorMsg = ""
    self.tile = time.strftime("%Y-%m-%d %H:%M:%S")
    try:
        """捕获链接异常或读取异常信息 """
        self.jenkins_url = 'http://127.0.0.1:10240/'  # jenkins地址 我这里是封装在配置文件当中
        self.server = jenkins.Jenkins(self.jenkins_url, username='admin', password='123456')  # 连接jenkins服务

        # 获取jenkins_url
        self.job_name = "job/autotest/"  # 拼接job名称
        self.job_url = self.jenkins_url + self.job_name  # job的url地址
        # 获取最后一次构建
        self.job_last_number = self.server.get_info(self.job_name)['lastBuild']['number']
        # #获取报告地址
        self.report_url = self.job_url + str(self.job_last_number) + '/allure'  # 报告地址
        log.debug("http://127.0.0.1:10240/：%s" % self.report_url)
    except Exception as e:
        self.errorMsg = str(e)
        log.info("jenkins连接异常 %s" % e)
