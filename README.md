# 黑马头条UI自动化测试项目

## 项目结构

```
hmtt_ui_test/
├── base/                    # 基础类
│   ├── base.py             # Web基础操作类
│   ├── web_base.py         # Web专属方法
│   └── app_base.py         # App基础操作类
├── page/                    # 页面对象层
│   ├── __init__.py         # 元素定位配置
│   ├── page_in.py          # 页面入口类
│   ├── page_mp_login.py    # 自媒体登录页面
│   ├── page_mp_article.py  # 自媒体文章页面
│   ├── page_mis_login.py   # 后台登录页面
│   ├── page_mis_audit.py   # 后台审核页面
│   ├── page_app_login.py   # APP登录页面
│   └── page_app_article.py # APP文章页面
├── scripts/                 # 测试用例
│   ├── test01_mp_login.py  # 自媒体登录测试
│   ├── test02_mp_article.py# 自媒体文章测试
│   ├── test03_mis_login.py # 后台登录测试
│   ├── test04_mis_audit.py # 后台审核测试
│   ├── test05_app_login.py # APP登录测试
│   └── test06_app_article.py# APP文章测试
├── tools/                   # 工具类
│   ├── get_driver.py       # 驱动管理
│   ├── get_log.py          # 日志工具
│   └── read_yaml.py        # YAML读取工具
├── data/                    # 测试数据
│   ├── mp_login.yaml       # 自媒体登录数据
│   ├── mp_article.yaml     # 文章数据
│   ├── mis_login.yaml      # 后台登录数据
│   ├── app_login.yaml      # APP登录数据
│   └── app_article.yaml    # APP文章数据
├── image/                   # 截图目录
├── logs/                    # 日志目录
├── reports/                 # 测试报告
├── config.py                # 项目配置
├── conftest.py              # pytest配置
├── pytest.ini               # pytest配置文件
├── run.py                   # 测试运行入口
└── requirements.txt         # 依赖包
```

## 环境要求

- Python 3.8+
- Chrome浏览器
- Android模拟器/真机（APP测试）
- Appium Server（APP测试）

## 安装依赖

```bash
pip install -r requirements.txt
```

## 运行测试

```bash
# 运行所有测试
python run.py

# 只运行Web端测试
python -c "from run import run_web_tests; run_web_tests()"

# 只运行APP端测试
python -c "from run import run_app_tests; run_app_tests()"

# 使用pytest直接运行
pytest -v

# 运行指定模块
pytest scripts/test01_mp_login.py

# 生成Allure报告
pytest --alluredir=./reports/allure
allure serve ./reports/allure
```

## 测试场景

1. **自媒体登录** - 手机号+验证码登录
2. **发布文章** - 自媒体平台发布文章
3. **后台登录** - 管理员账号密码登录
4. **文章审核** - 后台审核待发布文章
5. **APP登录** - 移动端登录
6. **APP文章** - 移动端查看文章

## 依赖版本

- selenium: 4.25.0
- appium-python-client: 3.2.1
- pytest: 8.3.3
- allure-pytest: 2.13.5
- PyYAML: 6.0.2
- pytest-html: 4.1.1

## 注意事项

1. 运行APP测试前需启动Appium Server
2. 确保Android设备已连接并开启USB调试
3. Chrome浏览器版本需与ChromeDriver匹配
4. 测试数据在data目录下的yaml文件中配置
