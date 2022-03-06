from seleniumwire import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from python_rucaptcha import ReCaptchaV3, ImageCaptcha, ReCaptchaV2
import peewee
import time 
import requests


RUCAPTCHA_KEY = ""
proxy_options = {
    'proxy': {
        'https': f'https://login:password@ip:port'
    }
}

url = 'https://www.google.com/'
search = 'https://www.google.com/search?q=карандаши+ручки&newwindow=1&start=100'
search2 = 'https://yandex.ru/search/?lr=11152&text=%D1%80%D1%83%D1%87%D0%BA%D0%B8'

def browser(url):


    chrome_options = Options()
    chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0')

    driver = webdriver.Chrome(executable_path='./chromedriver.exe', chrome_options=chrome_options)#, seleniumwire_options=proxy_options)
    driver.get(url)
    time.sleep(2)

    re = driver.find_element_by_xpath('//div[@data-value="reCAPTCHA"]').click()
    #№for le in range(0, 10):
        #driver.refresh()
        #time.sleep(2)

    time.sleep(1000)
    # output = driver.find_elements_by_xpath('.//div[@class="ZINbbc xpd O9g5cc uUPGi"]')
    # for out in output:
    #   print(out.get_attribute('outerHTML'))


#browser("https://rucaptcha.com/auth/login")

def ReCaptcha():
    SITE_KEY = "6LfwuyUTAAAAAOAmoS0fdqijC2PbbdH4kjq62Y1b"
    PAGE_URL = "https://www.google.com/sorry/index?continue=https://www.google.com/search%3Fq%3D%25D1%2584%25D1%258B%25D0%25B2%25D1%258B%25D1%2584%26oq%3D%25D1%2584%25D1%258B%25D0%25B2%25D1%258B%25D1%2584%26aqs%3Dchrome..69i57j69i60l2.362j0j15%26sourceid%3Dchrome%26ie%3DUTF-8&q=EgROVTCTGMu4uIMGIhkA8aeDS-I_ion1QFBAgjbXWf6Gm_94NyYLMgFy"
    DATA = "UDF6iXbyzUmwgkmY_9sik6u3xRyhknIm2NHch99WO1C7v10Hc9UEjE6dLKz7VmYu6EHzL6NwkikHaxboUreY-8S8WftnQWbsppkyPLxhdU99fOvyFaUO8ReE0bBOBxEzrOkmaDu0TAgqRupj6xpRPU_M1d42rDsuh41Swj5QXO_SBvWlfOuUJ9gYoYwJTLNt3sn4MPeoA7ZhGO674yc7Y4AoNNGu9TCm6BiduKdBPgFRVcIGwxohBLU"
    ACTION = 'index'
    MIN_SCORE = 0.4
    user_answer = ReCaptchaV3.ReCaptchaV3(
                                        rucaptcha_key=RUCAPTCHA_KEY, 
                                        action = ACTION, 
                                        min_score = MIN_SCORE).captcha_handler(
                                                    site_key=SITE_KEY,
                                                    page_url=PAGE_URL,
                                                    data_s = DATA
                                                )

    if not user_answer['error']:
        # решение капчи
        print(user_answer['captchaSolve'])
        print(user_answer['taskId'])
        print(user_answer['user_check'])
        print(user_answer['user_score'])
    elif user_answer['error']:
        # Тело ошибки, если есть
        print(user_answer ['errorBody'])
        print(user_answer ['errorBody'])

#ReCaptcha_V3()


img = "https://yandex.ru/captchaimg?aHR0cHM6Ly9leHQuY2FwdGNoYS55YW5kZXgubmV0L2ltYWdlP2tleT0wMEFBaW9TY0VTMGdTNmpuSGhEVlA5eUNBMHVoUTJOVyZzZXJ2aWNlPXdlYg,,_3/1617830488/c5eb23bc18753b03f233e5644a77b5e9_cbe4a6b9208b4dfdaeb763413c618dfd"



def YaImg(url):
    # Ссылка на изображения для расшифровки
    image_link = url
    # Возвращается JSON содержащий информацию для решения капчи
    user_answer = ImageCaptcha.ImageCaptcha(rucaptcha_key=RUCAPTCHA_KEY).captcha_handler(captcha_link=image_link)

    if not user_answer['error']:
        print(user_answer['captchaSolve'])
        print(user_answer['taskId'])
        return user_answer['captchaSolve']

    elif user_answer['error']:
        print(user_answer ['errorBody'])
        print(user_answer ['errorBody'])
        return False



#YaImg(img)


def ReCaptcha_V2():

    # G-ReCaptcha ключ сайта
    SITE_KEY = "6LfziTEUAAAAABWy62k8A5vnElP7wISs9z_v_HMH"
    # Ссылка на страницу с капчёй
    PAGE_URL = "https://rucaptcha.com/auth/login"
    # Возвращается JSON содержащий информацию для решения капчи
    user_answer = ReCaptchaV2.ReCaptchaV2(rucaptcha_key=RUCAPTCHA_KEY).captcha_handler(site_key=SITE_KEY,
                                                                                       page_url=PAGE_URL)

    if not user_answer['error']:
        print(user_answer['captchaSolve'])
        print(user_answer['taskId'])
    elif user_answer['error']:
        print(user_answer ['errorBody'])
        print(user_answer ['errorBody'])








ReCaptcha_V2()