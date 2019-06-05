from appium import webdriver


def init_driver():
    desired_caps = dict()
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    desired_caps['deviceName'] = '192.168.56.101:5555'
    desired_caps['appPackage'] = 'com.yunmall.lc'
    desired_caps['appActivity'] = 'com.yunmall.ymctoc.ui.activity.MainActivity'
    desired_caps['noReset'] = False
    desired_caps['automationName'] = 'Uiautomator2'


    return webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

#此项目的github地址https://github.com/JINSENIANHUALIJIE/aotlet_APP_2.git