from python_class import web_zidonghua_def #导入函数文件
from python_class import test_data  #导入测试数据文件
from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(10)

#调用参数 --1.先参数取出来 2. 传参到函数调用里
url = test_data.url['url']  #获取URL
uname = test_data.login_data[0]['user']  #获取登录用户名
pwd = test_data.login_data[1]['password']  #获取登录密码
s_key = test_data.s_key['s_key']  #获取搜索的关键字

result = web_zidonghua_def.search_key(driver=driver,url=url,user=uname,password=pwd,s_key=s_key)

if s_key in result:
    print('查询结果是正确的')
else:
    print('用例测试不通过')
