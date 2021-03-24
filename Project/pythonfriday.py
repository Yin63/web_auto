
str1 = "123456789"

list1 = list(str1)

print(list1)

sum1 = 0

for i in range(10, 30):
    sum1 += i
print(sum1)


def judge(ttr):

    if type(ttr) == list or type(ttr) == str or type(ttr) == dict:
        if len(ttr) > 5:
            return True, 'nice!'
        else:
            print('error')
            return False
    else:
        print('error2')
        return False

results = judge(12)

print(results)

from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(8)

driver.get('http://erp.lemfix.com/login.html')

driver.maximize_window()

driver.find_element_by_id('username').send_keys('test123')

driver.find_element_by_id('password').send_keys('123456')

driver.find_element_by_id('btnSubmit').click()

driver.find_element_by_xpath('//a[@title="零售出库"]//span').click()

data = driver.find_element_by_xpath('//a[@title="零售出库"]').get_attribute('data-tab-id')

data = data + '-frame'

driver.switch_to.frame(data)

driver.find_element_by_id('searchNumber').send_keys('LSCK00000004448')

driver.find_element_by_xpath('//a[@id="searchBtn"]//span[text()="查询"]').click()



