import pytest


# 读取yaml用例
from commons.yaml_util import clear_extract_yaml


def read_yaml():
    return ['微微', '小白', '小林', '小黑']  # 列表数据库


# fixture的类前使用方法
@pytest.fixture(scope="module", autouse=False, params=read_yaml())
def execute_sql(request):
    print("执行数据库查询")
    yield request.param
    print("关闭数据库链接")


@pytest.fixture(scope="function")
def test_fixture():
    print("testlzjlzjlzjlzj")


@pytest.fixture(scope="session", autouse=True)
def clear_yaml():
    clear_extract_yaml()
