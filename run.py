from selenium import webdriver
from Project import Python_auto
from test_data import test_data
driver = webdriver.Chrome()
driver.implicitly_wait(8)

results = Python_auto.begin_run(driver, test_data.url['url'], test_data.userinfo['username'], test_data.userinfo['password'], test_data.num['num'])

print(results)
