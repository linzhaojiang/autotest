import time

import allure
import pytest
from commons.request_util import RequestUtil
from commons.yaml_util import read_extract_yaml, write_extract_yaml


class TestApi1:

    # 获取token值
    @allure.feature( "获取token")
    @pytest.mark.run(order=1)
    def test_get_token(self):
        url = 'https://api.weixin.qq.com/cgi-bin/token'
        data = {
            "grant_type": "client_credential",
            "appid": "wx6b11b3efd1cdc290",
            "secret": "106a9c6157c4db5f6029918738f9529d"}
        res = RequestUtil().all_send_request("get", url=url, params=data)
        result = res.json()
        extract_value = {"access_token": result["access_token"]}  # 把需要的token值写入到extrac_value字典里
        write_extract_yaml(extract_value)  # 用yaml方法写入extrac_value字典的值

    # 使用token值变量解析
    def test_get_token_hq(self):
        url = "https://api.weixin.qq.com/cgi-bin/tags/get"
        data = {"access_token": read_extract_yaml("access_token")}
        res = RequestUtil().all_send_request('get', url=url, params=data)
        print(res.json())

    # post请求，以及传参数变量用法。
    def test_edit_flag(self):
        url = 'https://api.weixin.qq.com/cgi-bin/tags/update?'
        pa = {"access_token": read_extract_yaml("access_token")}  # 调用yaml的token变量
        data = {"tag": {"id": 10154, "name": "testxiaojiejie" + str(int(time.time()))}}  # str这个是时间搓。
        res = RequestUtil().all_send_request('post', url=url, json=data, params=pa)  # params是传参数。传token鉴权
        print(res)

    # 上传接口用法
    def test_file_upload(self):
        url = 'https://api.weixin.qq.com/cgi-bin/media/uploadimg?access token=' + read_extract_yaml("access_token")
        data = {
            "media": open(r"/Users/baofu/Documents/案例.png", "rb")
        }
        res = RequestUtil().all_send_request("post", url=url, files=data)
        print(res.json())
