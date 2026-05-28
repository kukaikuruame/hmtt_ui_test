import os

BASE_PATH = os.path.dirname(__file__)

"""以下数据为自媒体、后台管理url"""
# 自媒体url
url_mp = "https://pc-toutiao-python.itheima.net/#/login"
# 后台管理url
url_mis = "https://pc-toutiao-python.itheima.net/#/mis/login"

"""以下为app应用配置信息"""
# 包名
appPackage = "com.itcast.toutiaoApp"
# 启动名
appActivity = ".MainActivity"
# Appium服务地址
appium_server = "http://127.0.0.1:4723"

"""以下为测试配置"""
# 默认超时时间
timeout = 30
# 轮询频率
poll_frequency = 0.5
