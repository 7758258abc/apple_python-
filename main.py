from selenium.webdriver import Chrome
from selenium.common.exceptions import TimeoutException
import time

try:
    with open('账号密码填写处.txt','r') as f:
        data_ = f.read()
except:
    print('没有找到 "账号密码填写处.txt"  文件')
    input()
    exit()

# 在这修改自己的用户和密码,  账户和密码填在 '' 中, ''不可以删除掉
aplle_ID = '123456'
ID密码 = '123456'

data_ = data_.split('\n')
aplle_ID = data_[0]
ID密码 = data_[1]





# 第一次运行需要手动选择提货地址, 设置成 True,   如果设置过了以后就改成 False
第一次运行 = True


#############################################################
# 下面的代码一定不要动
#############################################################

# 1 创建浏览器对象
浏览器对象 = Chrome()

# 2 请求超时5秒
浏览器对象.set_page_load_timeout(5)

url = 'https://secure4.www.apple.com.cn/shop/signIn?c=aHR0cHM6Ly93d3cuYXBwbGUuY29tLmNuL3Nob3AvYmFnfDFhb3MxNTA1MmI1NzVhNTE4ZmUxZjA4NjRjYTE0MzM2MDMxN2I4NWIxNjA1&o=O01MVEUz&r=SXYD4UDAPXU7P7KXF&s=aHR0cHM6Ly9zZWN1cmU0Lnd3dy5hcHBsZS5jb20uY24vc2hvcC9jaGVja291dC9zdGFydD9wbHRuPUMzNUJDQ0EzfDFhb3NmYzAxZGJiYTM3YzZkNDFlYTQ4YjJmNzkzZDVmYjRkOTc0ZmM0NWQ1&t=SXYD4UDAPXU7P7KXF&up=t'

# 3 捕获超时异常
try:
    # 4发起请求
    浏览器对象.get(url)
    print('成功获取请求')
except TimeoutException:
    print('页面渲染超时')
    # 多等3秒
    time.sleep(3)

for i in range(10):
    try:
        # 登录
        xpath_ = '//*[@id="signIn.customerLogin.appleId"]'
        用户 = 浏览器对象.find_element_by_xpath(xpath_)
        用户.click()
        time.sleep(0.2)
        用户.send_keys(aplle_ID)
        time.sleep(0.2)
        break
    except:
        time.sleep(2)

time.sleep(1.5)
for i in range(10):
    try:
        # 密码
        xpath_ = '//*[@id="signIn.customerLogin.password"]'
        密码 = 浏览器对象.find_element_by_xpath(xpath_)
        密码.click()
        time.sleep(0.2)
        密码.send_keys(ID密码)
        time.sleep(0.3)

        xpath_ = '//*[@id="signin-submit-button"]'
        确定 = 浏览器对象.find_element_by_xpath(xpath_)
        确定.click()
        time.sleep(3)
    except:
        break


for i in range(10):
    try:
        # 确定
        xpath_ = '//*[@id="checkout-container"]/div/div[6]/div[1]/div[2]/div/div/div[1]/div/div/div/fieldset/div[1]/div[2]/label'
        取货 = 浏览器对象.find_element_by_xpath(xpath_)
        取货.click()
        time.sleep(0.5)
        break
    except:
        time.sleep(0.3)

if  第一次运行:
    input('程序第一次运行, 在弹出的网页中请手动选择地址并刷新网页, 完成后点击该句子后回车!!!')
else:
    print('程序继续运行')

time.sleep(0.5)
浏览器对象.refresh()

for i in range(999):
    aaa = 999
    for i in range(aaa):
        try:
            xpath_ = '//*[@id="rs-fulfillment-storelocator-error"]/div/div'
            无货 = 浏览器对象.find_element_by_xpath(xpath_)
            print('当前无货')
            time.sleep(1.5)
            # 刷新
            浏览器对象.refresh()
        except:
            break

    print('有货了!!!')
    浏览器对象.maximize_window()


    res = input('继续监视请点击该句子后, 再按下回车:')
    if res == 'q':
        break

time.sleep(999)
