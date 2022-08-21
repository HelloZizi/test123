from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)

def login_page(user,password,driver):  #形参 -参数化---提高代码复用率
    driver.find_element(by=By.ID,value="username").send_keys('test123') #找到了有username这个ID的元素--点击，输入内容
    driver.find_element(by=By.NAME,value="password").send_keys('123456')
    driver.find_element(by=By.ID,value='btnSubmit').click()  #由于是要点击登录按钮，因此是click操作而不是send_keys

def open_url(url,driver):  #打开网页
    driver.get("http://erp.lemfix.com")
    driver.maximize_window()

def search_key(driver,url,user,password,s_key):
    open_url(url,driver)
    login_page(user,password,driver)
    driver.find_element(by=By.XPATH, value='//span[text()="零售出库"]').click()
    p_id = driver.find_element(by=By.XPATH, value='//div[text()="零售出库"]/..').get_attribute('id')
    F_id = p_id + "-frame"
    driver.switch_to.frame(1)
    driver.find_element(by=By.ID, value='searchNumber').send_keys(s_key)
    driver.find_element(by=By.ID, value='searchBtn').click()  # 点击查询按钮方法2
    time.sleep(2)
    danju_num = driver.find_element(by=By.XPATH, value="//tr[@id='datagrid-row-r1-2-0']//td[@field='number']//div").text
    return danju_num
