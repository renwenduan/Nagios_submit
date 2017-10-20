# coding=utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Firefox()


class Mosic_submit(object):
    def __init__(self):
        self.start_url = 'https://mosaic.app.corp/maximo/webclient/login/login.jsp?appservauth=true'
        self.base_node = '/html/body/form/table[2]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td/div/table/tbody/tr/td/div/table/tbody/tr/td/table/tbody/tr/td/div/table/tbody/tr[2]/td[2]/div[4]/table/tbody/tr[2]/td/div/table/tbody/tr[1]/td/div[2]/table/tbody/tr[5]/td[1]/a'
        self.schedule_node = '//*[@id="m356798d1-tab_anchor"]'
        self.context = 'i have done this process'

    def start_firefox(self):
        browser.get(self.start_url)
        uname = browser.find_element_by_id('j_username')  # 选取账号
        upasswd = browser.find_element_by_id('j_password')
        uname.send_keys('1duanrev')  # 输入账号
        upasswd.send_keys('Shanghai123')  # 输入密码
        browser.implicitly_wait(20)  # wait 10s
        browser.find_element_by_id('loginbutton').click()  # choose the click button and submit the data

    def choose_request(self):
        # 执行选择操作
        time.sleep(20)
        browser.find_element_by_xpath(self.base_node).click()  # 这里是临时性的,后期应该改成自动列表读取
        time.sleep(10)
        # 选择schedule 标签
        browser.find_element_by_xpath(self.schedule_node).click()
        time.sleep(8)
        # 选择状态标签

    def choose_status(self, item):
        browser.find_element_by_xpath(item).click()  # 弹出状态
        time.sleep(8)
        # 这是弹出后需要选择的状态
        browser.find_element_by_xpath('//*[@id="m8846c35-tb"]')  # 找到下拉框
        new_status = browser.find_element_by_xpath('//*[@id="m8846c35-tb"]')  # 状态框
        Memo = browser.find_element_by_xpath('//*[@id="me68a0d19-co2_1_vl"]')  # 内容框
        ok_button = browser.find_element_by_xpath('//*[@id="m9bd19aef-pb"]')  # ok 按钮
        cancle_button = browser.find_element_by_xpath('//*[@id="m2d8cb55-pb"]')  # cancle 按钮
        new_status.click()  # 点击状态框
        ActionChains(browser).move_to_element_with_offset(new_status, 10, 50).click().perform()  # 选择状态
        time.sleep(1)
        print '执行输入操作和取消操作'
        ActionChains(browser).move_to_element(Memo).click().send_keys(self.context).perform()
        time.sleep(1)
        ActionChains(browser).move_to_element(cancle_button).click().perform()
        time.sleep(5)

    def complete_status(self):
        lable_list = ['//*[@id="mbb442a0c_tdrow_[C:14]_hyperlink-lb[R:0]"]',
                      '//*[@id="mbb442a0c_tdrow_[C:14]_hyperlink-lb[R:1]"]',
                      '//*[@id="mbb442a0c_tdrow_[C:14]_hyperlink-lb[R:2]"]',
                      '//*[@id="mbb442a0c_tdrow_[C:14]_hyperlink-lb[R:3]"]',
                      '//*[@id="mbb442a0c_tdrow_[C:14]_hyperlink-lb[R:4]"]', ]
        for item in lable_list:
            self.choose_status(item)
        print '状态选择完毕,退出程序'
        self.finish_process()

    def finish_process(self):
        browser.close()


if __name__ == '__main__':
    web_click = Mosic_submit()
    web_click.start_firefox()
    web_click.choose_request()
    web_click.complete_status()
