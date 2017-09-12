from selenium import webdriver
import datetime
import time

driver=webdriver.Chrome(executable_path='chromedriver.exe')

def login(uname,pwd):
    driver.get('http://www.jd.com')
    if driver.find_element_by_link_text("您好,请登录"):
        driver.find_element_by_link_text("您好,请登录").click()
    if driver.find_element_by_link_text("账户登录"):
        driver.find_element_by_link_text("账户登录").click()
    if driver.find_element_by_name("loginname"):
        driver.find_element_by_name("loginname").send_keys(uname)
    if driver.find_element_by_name("nloginpwd"):
        driver.find_element_by_name("nloginpwd").send_keys(pwd)
    if driver.find_element_by_id("loginsubmit"):
        driver.find_element_by_id("loginsumit").click()
    time.sleep(1)
    driver.get("https://cart.jd.com/cart.action")
    if driver.find_element_by_link_text("去结算"):
        driver.find_element_by_link_text("去结算").click()
    now=datetime.datetime.now()
    print("login success:",now.strptime("%Y-%m-%d %H:%M:%S"))

def buy_on_time(buytime):
    while True:
        now=datetime.datetime.now()
        if now.strptime("%Y-%m-%d %H:%M:%S")==buytime:
            while True:
                try:
                    driver.find_element_by_id("order-submit").click()
                except:
                    time.sleep(0.1)
        time.sleep(0.1)

login("280705132@qq.com","2017qixi")
buy_on_time('2017-09-19 10:00:01')

