from selenium import webdriver
# 创建 WebDriver 对象，指明使用chrome浏览器驱动
wb=webdriver.Chrome(r'd:\webdrivers\chromedriver.exe')

# 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
wd.get('https://www.baidu.com')

# 根据id选择元素，返回的就是该元素对应的WebElement对象
# 目标：搜索框
element=wd.find_element_by_id('kw')

# 输入字符串到这个输入框里
element.send_keys('白月黑羽\n')
