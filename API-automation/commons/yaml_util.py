import os
import yaml


# 关于读取测试用例yaml方法
def read_testcase_yaml(yaml_xpath):
    with open(os.getcwd() + yaml_xpath, encoding="utf-8", mode="r") as f:
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
        return value


# 将数据写入extract.yaml文件
def write_extract_yaml(data):
    with open(os.getcwd() + "/extract.yaml", encoding="utf-8", mode="a") as f:
        yaml.dump(data, stream=f, allow_unicode=True)


# 通过key读取extract.yaml文件
def read_extract_yaml(key):
    with open(os.getcwd() + "/extract.yaml", encoding="utf-8", mode="r") as f:
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
        return value[key]


# 清空extract.yaml文件
def clear_extract_yaml():
    with open(os.getcwd() + "/extract.yaml", encoding="utf-8", mode="w") as f:
        f.truncate()
