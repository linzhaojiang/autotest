import requests


class RequestUtil:
    session = requests.session()
    #统一发送请求的方法
    def all_send_request(self,method,url,**kwargs):
        res = RequestUtil.session.request(method,url,**kwargs)
        return res

