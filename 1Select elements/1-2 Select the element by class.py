#http://cdn1.python3.vip/files/selenium/sample1.html
'''
    <body>
        
        <div class="plant"><span>土豆</span></div>
        <div class="plant"><span>洋葱</span></div>
        <div class="plant"><span>白菜</span></div>

        <div class="animal"><span>狮子</span></div>
        <div class="animal"><span>老虎</span></div>
        <div class="animal"><span>山羊</span></div>

    </body>
'''

from selenium import webdriver
wd.get('http://cdn1.python3.vip/files/selenium/sample1.html')

# 根据 class name 选择元素
elements = wd.find_elements_by_class_name('animal')

#结果是一个列表
#打印出 element 对应 网页元素的 文本
for element in elements:
    print(element.text)
    
