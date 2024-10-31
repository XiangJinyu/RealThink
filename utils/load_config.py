import yaml


def load():
    # 读取上一级目录中的 YAML 配置文件
    with open('../config.yaml', 'r') as file:
        config = yaml.safe_load(file)

    return config
