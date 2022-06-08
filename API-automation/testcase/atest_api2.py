import re

from commons.request_util import RequestUtil
from commons.yaml_util import read_extract_yaml, write_extract_yaml


class TestApi2:

    def test_phpwind(self, base_url):
        url = base_url + 'phpwind'
        res = RequestUtil().all_send_request('get', url=url)
        result = res.text
        extract_valur = {"csrf_token": re.search('name="csrf_token" value="(.*?)"', result).group(1)}  # 正则提取
        write_extract_yaml(extract_valur)
        # assert
        print(extract_valur)

    # 登陆
    def test_login(self, base_url):
        url = base_url + 'phpwind/index.php?m=u&c=login&a=dorun'
        data = {
            "username": "linzhaojian",
            "password": "Aa112211",
            "csrf_token": read_extract_yaml("csrf_token"),
            "backurl": "http://47.107.116.139/phpwind/",
            "invite": ""
        }
        headers = {"Accept": "application/json,text/javascript,/;q=0.01", "X-Requested-with": "XMLHTTPRequest"}
        res = RequestUtil().all_send_request('post', url=url, data=data, headers=headers)
        print(res.text)
