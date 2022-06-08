
import pytest

from commons.request_util import RequestUtil
from commons.yaml_util import read_testcase_yaml


class TestApi3:

    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("args_name", read_testcase_yaml("/testcase/get_token.yaml"))
    def test_get_token(self, args_name):
        url = args_name["request"]["url"]
        data = args_name["request"]["params"]
        methods = args_name["request"]["method"]
        res = RequestUtil().all_send_request(method=methods, url=url, params=data)
        result = res.json()
        print(result)




