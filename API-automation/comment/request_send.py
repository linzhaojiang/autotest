#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/28 3:16 下午
# @Name    : peilun
# @File    : request_send.py
# @Software: PyCharm
import requests
import json
from comment.log import *
from comment.readconfig import *
from comment.consts import *


class HttpRequests:
    '''
    request 请求封装
    '''

    def __init__(self):
        self.session = requests.Session()
        self.host = con.host

    def send_request(self,method, url, headers=None, data=None, **kwargs):
        log.info("请求方式:【%s】,请求host:【%s】,请求地址:【%s】,请求Headers:【%s】,请求参数Body:【%s】"
                         % (method, self.host, url, headers, data))


        method = method.upper()
        if 'POST' == method:
            response = self.session.request(method=method, url=self.host+url,headers=headers,
                                            data=json.dumps(data), stream=True, verify=False,**kwargs)
            log.info(response.json())

        elif 'GET' == method:
            response = self.session.request(method=method, url=self.host+url, headers=headers, stream=True,
                                            verify=False, **kwargs)
            log.info(response.json())
        elif 'PUT' == method:
            response = self.session.request(method=method, url=self.host+url,headers=headers,
                                            data=json.dumps(data), stream=True, verify=False,**kwargs)
            log.info(response.json())
        elif 'DELETE' == method:
            response = self.session.request(method=method, url=self.host+url,headers=headers,
                                            stream=True, verify=False,**kwargs)
            log.info(response.json())

        else:
            raise ValueError('request method "{}" error ! please check'.format(method))
        return response
