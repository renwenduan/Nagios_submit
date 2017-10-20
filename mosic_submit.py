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
	# login handle
        browser.get(self.start_url)
        uname = browser.find_element_by_id('j_username')  # user name text area 
        upasswd = browser.find_element_by_id('j_password') # user password
        uname.send_keys('1duanrev')  # user nameè
        upasswd.send_keys('Shanghai123')  # user password
        browser.implicitly_wait(20)  # wait 10s
        browser.find_element_by_id('loginbutton').click()  # choose the click button and submit the data

    def choose_request(self):
	# pick the request you want to
        time.sleep(20)
        browser.find_element_by_xpath(self.base_node).click()  # click the reqest and jump to the detail pageè
        time.sleep(10)
	# jump to the schedule page
        browser.find_element_by_xpath(self.schedule_node).click()
        time.sleep(8)
	
    def choose_status(self, item):
        browser.find_element_by_xpath(item).click()  # click the process button
        time.sleep(8)
	# click the 'complete'
        browser.find_element_by_xpath('//*[@id="m8846c35-tb"]')  # æ‰¾åˆ°ä¸‹æ‹‰æ¡†
	# input the text you want this will modify to random chioce later 
        new_status = browser.find_element_by_xpath('//*[@id="m8846c35-tb"]')  # status area
        Memo = browser.find_element_by_xpath('//*[@id="me68a0d19-co2_1_vl"]')  # memo text areaå
        ok_button = browser.find_element_by_xpath('//*[@id="m9bd19aef-pb"]')  # ok button
        cancle_button = browser.find_element_by_xpath('//*[@id="m2d8cb55-pb"]')  # cancle button
        new_status.click()  # blank 
        ActionChains(browser).move_to_element_with_offset(new_status, 10, 50).click().perform()  # choose status
        time.sleep(1)
        print 'done this status'
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
        print 'Done and will close the window'
        self.finish_process()

    def finish_process(self):
        browser.close()


if __name__ == '__main__':
    web_click = Mosic_submit()
    web_click.start_firefox()
    web_click.choose_request()
    web_click.complete_status()
