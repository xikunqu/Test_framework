#coding:utf-8
'''
说明：对页面元素进行高亮显示
'''
import time

def highlight(element):
    driver = element._parent
    #设置元素的style属性
    def apply_style(s):
        driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                              element, s)
    original_style = element.get_attribute('style')
    apply_style("background: yellow; border: 2px solid red;")
    time.sleep(3)
    apply_style(original_style)
