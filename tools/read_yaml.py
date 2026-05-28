import yaml
import os
from config import BASE_PATH


def read_yaml(filename):
    file_path = os.path.join(BASE_PATH, "data", filename)
    arr = []
    with open(file_path, "r", encoding="utf-8") as f:
        for datas in yaml.safe_load(f).values():
            arr.append(tuple(datas.values()))
    return arr


if __name__ == '__main__':
    print(read_yaml("mp_login.yaml"))
