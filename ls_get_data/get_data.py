import os
import re

from config import rule, data_file_dirpath
from xls_tools import XlsTool


def get_data(content, rule):
    res = {}
    for key, value in rule.items():
        key = re.sub("[\u4e00-\u9fa5]", "", key)
        key = key.replace("_","")
        if value:
            res[key] = re.findall(value, content)[0]
        else:
            res[key] = ""
    return res


if __name__ == '__main__':
    datas = []
    files_dirpath = data_file_dirpath
    for file_dirpath in os.listdir(files_dirpath):
        file_path = os.path.join(files_dirpath, file_dirpath, "data.txt")
        if os.path.exists(path=file_path):
            with open(file_path, mode="r", encoding="utf-8") as f:
                content = f.readlines()
                content = "".join(content)
                data = get_data(content, rule)
                datas.append(data)
    xls_tools = XlsTool("data.xls")
    xls_tools.write_header(rule.keys())
    xls_tools.insert_data(datas)
    xls_tools.save()
