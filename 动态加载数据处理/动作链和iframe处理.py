from selenium import webdriver
from time import  sleep
#导入动作链对应的类
from selenium.webdriver import ActionChains
bro = webdriver.Chrome(executable_path='./chromedriver.exe')
bro.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
#如果定位的标签是存在于iframe之中的则必须通过如下操作定位
bro.switch_to.frame('iframeResult')
div = bro.find_element_by_id('draggable')
#创建动作链实例
action = ActionChains(bro)
action.click_and_hold(div)
for i in range(5):
    #perform()表示动作立即执行,move_by_offset(x,y),水平和竖直方向
    action.move_by_offset(17,0).perform()
    sleep(0.3)
#释放动作链
action.release()
bro.quit()

