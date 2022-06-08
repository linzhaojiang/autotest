#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/19 4:05 下午
# @Name    : peilun
# @File    : readconfig.py
# @Software: PyCharm
import os
import yaml

#获取配置文件
path = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
conpath = path+'/config'+'/config.yaml'

with open(conpath,'r',encoding='utf-8') as f:
    temp = yaml.load(f.read(), Loader=yaml.FullLoader)
    # print(temp)


class git_function():

    def __init__(self):
        self.env = temp['env']
        self.project = temp['project']
        self.language = temp['language']
        self.host = temp[self.env + "_" + self.project + "_"+"host"]
        self.system = temp[self.env + "_" +"system"]
        self.db_host = temp[self.env + "_"+"db"+"_"+"host"]
        self.db_port = temp[self.env + "_" + "db" + "_" + "port"]
        self.db_name = temp[self.env + "_" + "db" + "_" + "name"]
        self.db_pass = temp[self.env + "_" + "db" + "_" + "pass"]
        self.jenkins_name = temp['Jenkins_name']
        self.jenkins_passwd = temp['Jenkins_passwd']
        self.allure_path = temp['allure_path']
        self.jenkins_url = temp['jenkin_url']
        self.fly = temp['Fly']


con = git_function()

