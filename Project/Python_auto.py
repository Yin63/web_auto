

def start(driver, url):
    driver.get(url)
    driver.maximize_window()
    return True


def login(driver, username, password):
    driver.find_element_by_id('username').send_keys(username)

    driver.find_element_by_id('password').send_keys(password)

    driver.find_element_by_id('btnSubmit').click()
    return True

def find_data(driver, num):
    driver.find_element_by_xpath('//a[@title="零售出库"]//span').click()

    data = driver.find_element_by_xpath('//a[@title="零售出库"]').get_attribute('data-tab-id')

    data = data + '-frame'

    driver.switch_to.frame(data)

    driver.find_element_by_id('searchNumber').send_keys(num)

    driver.find_element_by_xpath('//a[@id="searchBtn"]//span[text()="查询"]').click()
    return True

def begin_run(driver, url, username, password, num):
    start_over = start(driver, url)
    if start_over:
        login_over = login(driver, username, password)
        if login_over:
            find_data_over = find_data(driver, num)
            if find_data_over:
                return '程序运行完成!'
            else:
                return '查询模块错误!'
        else:
            return '登录模块错误!'
    else:
        return '浏览器打开错误！'

