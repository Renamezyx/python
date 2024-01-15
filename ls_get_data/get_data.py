import os
import re
import xlwt

import config
from xls_tools import XLSTools


def get_data(content, rules):
    res = {}
    for key, value in rules.items():
        if value:
            res[key] = re.findall(value, content)[0]
        else:
            res[key] = ""
    return res


if __name__ == '__main__':
    datas = []
    files_dirpath = config.data_file_dirpath
    for file_dirpath in os.listdir(files_dirpath):
        file_path = os.path.join(files_dirpath, file_dirpath, "data.txt")
        if os.path.exists(path=file_path):
            with open(file_path, mode="r", encoding="utf-8") as f:
                content = f.readlines()
                content = "".join(content)
                data = get_data(content, config.rules)
                datas.append(data)
    xls_tools = XLSTools("data.xls")
    xls_tools.write_row(datas)
