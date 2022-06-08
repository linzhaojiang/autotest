#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/19 3:58 下午
# @Name    : peilun
# @File    : runcase_data.py
# @Software: PyCharm
import sys
sys.path.append("..")
from comment.readexcel import *
import pytest
import allure
from comment.request_send import *
import requests

htpqes = HttpRequests()



@pytest.mark.parametrize("data", read_exce())
def test(data):
    '''
    使用 parametrize 数据驱动
    :param data:
    :return:
    '''

    # 转换测试数据类型格式为json
    dicher = eval(data['Headers'])
    diccase = eval(data['Case_Param'])

    describe = data['Describe']
    title = data['Moudle']
    title_case = data['Moudle']+"_"+describe

    # allure.dynamic 动态标题
    allure.dynamic.title(title_case)     # 用例标题
    allure.dynamic.feature(title)   # 模块功能
    allure.dynamic.story(title)     # 功能点
    allure.dynamic.description(describe)    # 动态描述
    allure.attach(f"这是测试用例传的参数{diccase}")

    if sys.argv[2] == data['Leve']:
        if data['Url'] != "/api/user/login":
            # 将登录后获取的token写入 headers请求
            headers_token = {"Content-Type": "application/json", "Authorization": userinfo.token}
            if data['Method'] in ['post','put']:
                log.info("使用的请求方式为：%s" % data['Method'])
                # 使用post请求 非登录
                resp = htpqes.send_request(data['Method'], url=data['Url'], headers=headers_token, data=diccase)
                assert resp.json()['code'] == data['Assert']
            elif data['Method'] == 'get':
                # 使用get请求
                if data['Case_PerProcessor'] == 'user_id':
                    resp = htpqes.send_request(data['Method'], url=data['Url']+str(userinfo.userid), headers=headers_token)
                    assert resp.json()['code'] == data['Assert']
                else:
                    resp = htpqes.send_request(data['Method'], url=data['Url'], headers=headers_token)
                    assert resp.json()['code'] == data['Assert']
            elif data['Method'] == 'delete':
                # 使用delete请求
                resp = htpqes.send_request(data['Method'], url=data['Url'], headers=headers_token)
                assert resp.json()['code'] == data['Assert']
            else:
                raise Exception("用例请求方式错误！！！仅支持[get, post, put, delete']请求")  # 手动抛出异常
        else:
            # 使用post请求 登录
            resp = htpqes.send_request(data['Method'], url=data['Url'], headers=dicher, data=diccase)
            assert resp.json()['code'] == data['Assert']
            if resp.json()['code'] == 200:
                userinfo.token = resp.headers['Authorization']
                userinfo.userid = resp.json()['data']['id']
                log.info("登录后获取的Token为:【%s】" % userinfo.token)
                log.info("登录后获取的用户id:【%s】" % userinfo.userid)

    elif sys.argv[2] != data['Leve']:
        pytest.skip("控制台输入等级与用例等级不符，该用例不执行！")
    elif sys.argv[2] not in ['P0','P1','P2']:
        raise Exception("输入的用例等级不存在！仅支持['P0','P1','P2']输入")  # 手动抛出异常