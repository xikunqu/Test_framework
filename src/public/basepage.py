#coding:utf-8
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from src.public.browser import Browser
from utils.log import logger


class BasePage(Browser):
    def __init__(self, page=None, browser_type='firefox'):
        if page:
            self.driver = page.driver
        else:
            super(BasePage, self).__init__(browser_type=browser_type)

    @property
    def current_window(self):
        return self.driver.current_window_handle

    @property
    def title(self):
        return self.driver.title

    @property
    def current_url(self):
        return self.driver.current_url

    def get_driver(self):
        return self.driver

    def wait(self, seconds=3):
        time.sleep(seconds)

    def execute(self, js, *args):
        self.driver.execute_script(js, *args)

    def move_to(self, element):
        ActionChains(self.driver).move_to_element(element).perform()

    def find_element(self,*loc):
        #return self.driver.find_element(*loc)
        try:
            #确保元素是可见的
            #注意：以下入参为元组的元素，需要加*
            WebDriverWait(self.browser,10).until(lambda driver:driver.find_element(*loc).is_displayed())
            return self.browser.find_element(*loc)
        except:
            print("%s页面中未能找到%s元素"%(self,loc))

            # 重写元素定位方法

    def find_elements(self, *loc):
        # return self.driver.find_elements(*loc)
        try:
            # 确保元素时可见的
            # 注意：以下入参为元组的元素，需要加*
            WebDriverWait(self.browser, 10).until(lambda driver: driver.find_element(*loc).is_displayed())
            return self.browser.find_elements(*loc)
        except:
            print("%s页面中未能找到%s元素" % (self, loc))

    def switch_to_window(self, partial_url='', partial_title=''):
        """切换窗口
            如果窗口数<3,不需要传入参数，切换到当前窗口外的窗口；
            如果窗口数>=3，则需要传入参数来确定要跳转到哪个窗口
        """
        all_windows = self.driver.window_handles
        if len(all_windows) == 1:
            logger.warning('只有1个window!')
        elif len(all_windows) == 2:
            other_window = all_windows[1 - all_windows.index(self.current_window)]
            self.driver.switch_to.window(other_window)
        else:
            for window in all_windows:
                self.driver.switch_to.window(window)
                if partial_url in self.driver.current_url or partial_title in self.driver.title:
                    break
        logger.debug(self.driver.current_url, self.driver.title)

    def switch_to_frame(self, param):
        self.driver.switch_to.frame(param)

    def switch_to_alert(self):
        return self.driver.switch_to.alert

    # 判断元素是否存在,如果没找到或者找到多个 ，就返回False
    def is_element_exist(self, *element):
        s = self.browser.find_elements(*element)

        if len(s) == 0:
            # print("元素未找到")
            return False
        elif len(s) == 1:
            # print("此元素存在")
            return True
        else:
            # print("找到%s个元素"%len(s))
            return False