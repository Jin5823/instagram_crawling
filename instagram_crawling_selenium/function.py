import time
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


# 드라이버 세팅
def driver_setting(headless):
    options = webdriver.ChromeOptions()
    if headless is True:
        options.add_argument('headless')
    options.add_argument("--start-maximized")
    options.add_argument("--disable-cache")
    options.add_argument("--lang=ko_KR")

    # options.add_experimental_option("prefs", {"profile.default_content_settings.cookies": 2})
    prefs = {"profile.managed_default_content_settings.images": 2}
    options.add_experimental_option("prefs", prefs)
    options.add_argument(
        "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36")
    # headless 로 사용할 경우 user-agent 를 바꿔 줘야한다.
    options.add_argument("--keep-alive")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.execute_script("Object.defineProperty(navigator, 'languages', {get: function() {return ['ko-KR', 'ko']}})")
    driver.implicitly_wait(0.1)

    return driver


# 로그인 함수
def login(user_driver):
    user_driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/span/a[1]').click()
    time.sleep(0.1)
    user_driver.find_element_by_name('username').send_keys('*username')
    ele = user_driver.find_element_by_name('password')
    ele.send_keys('*password')
    ele.send_keys(Keys.ENTER)
    time.sleep(3)


# 기본 정보 함수
def basics_info(user_driver):
    base_info_data = []
    x = user_driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/h1')
    base_info_data.append('ID %s' % x.get_attribute('textContent'))

    for i in range(1, 4):
        if i == 1:
            base_info_data.append(user_driver.find_element_by_xpath(
                '//*[@id="react-root"]/section/main/div/header/section/ul/li[%d]/span' % i).get_attribute(
                'textContent'))
        else:
            base_info_data.append(user_driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header'
                                                                    '/section/ul/li[%d]/a' % i).get_attribute(
                'textContent'))

    try:
        x = user_driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[2]/h1')
        base_info_data.append('nickname %s' % x.get_attribute('textContent'))
    except:
        pass
    try:
        x = user_driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[2]/span')
        base_info_data.append('bio %s' % x.get_attribute('textContent'))
    except:
        pass
    # bio 추가

    try:
        x = user_driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[2]/a')
        base_info_data.append('link %s' % x.get_attribute('textContent'))
    except:
        pass
    # link 추가

    for i in range(1, 8):
        try:
            time.sleep(0.5)
            x = user_driver.find_element_by_xpath(
                '//*[@id="react-root"]/section/main/div/div[1]/div/div/div/div/ul/li[%d]' % i)
            base_info_data.append('공지된 스토리%d %s' % (i, x.get_attribute('textContent')))
        except:
            pass
    # 공지된 스토리 추가

    try:
        base_info_data[1] = base_info_data[1].replace(",", "")
    except:
        pass

    return base_info_data


# 첫번째 게시글 클릭 함수
def first_post_click(user_driver):
    try:
        user_driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]').click()
    except:
        user_driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[2]/article/'
                                          'div[1]/div/div[1]/div[1]/a/div[1]/div[2]').click()


# 다음 게시글 클릭 함수
def next_post_click(user_driver):
    try:
        user_driver.find_element_by_xpath('/html/body/div[3]/div[1]/div/div/a[2]').click()
    except:
        user_driver.find_element_by_xpath('/html/body/div[3]/div[1]/div/div/a').click()


# 그전 게시글 클릭 함수
def prev_post_click(user_driver):
    user_driver.find_element_by_xpath('/html/body/div[3]/div[1]/div/div/a[1]').click()


# 게시글 시간 함수
def post_time(user_driver):
    try:
        p_time = user_driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/div[2]/div[2]/a/'
                                                   'time').get_attribute('datetime')
    except:
        p_time = user_driver.find_element_by_xpath(
            '/html/body/div[3]/div[2]/div/article/div[2]/div/a/time').get_attribute(
            'datetime')

    return p_time


# 게시글 댓글 함수
def post_comment(user_driver):
    comment = []
    true_i = 1
    while True:
        true_i = true_i + 8
        try:
            user_driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/div[2]/div[1]/ul/li/div').click()
            x = user_driver.find_elements_by_xpath('/html/body/div[3]/div[2]/div/article/div[2]/div[1]/ul/'
                                                   'ul[%d]' % true_i)
            if len(x) == 0:
                break
            time.sleep(0.5)
        except:
            break
    user_driver.implicitly_wait(0.001)
    cnt_i = 1
    while True:
        try:
            y = user_driver.find_elements_by_xpath('/html/body/div[3]/div[2]/div/article/div[2]/div[1]/ul/ul[%d]/'
                                                   'div/li/div/div[1]/div[2]/span' % cnt_i)
            cnt_i += 1
            comment.append(y[0].get_attribute('textContent'))
        except:
            comment.append(cnt_i - 2)
            break

    return comment


# 게시글 본문 함수
def post_words(user_driver):
    try:
        x = user_driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/div[2]/div[1]/ul/div/li/'
                                              'div/div/div[2]/span')
        post = x.get_attribute('textContent')
    except:
        post = '_'
        pass

    return post


# 게시글 좋아요 함수
def post_like(user_driver):
    x = user_driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/div[2]/section[2]/div')
    post = x.get_attribute('textContent')

    return post


# 게시글 이미지 함수
def post_lmg(user_driver, name, pic):
    try:
        try:
            x = user_driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/div[1]/'
                                                  'div/div/div/div[1]/div/div/img')
        except:
            x = user_driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/div[1]/div/div/div[1]/img')
        src = x.get_attribute('src')
        urllib.request.urlretrieve(src, './%s/pic/%s_%d.png' % (name, name, pic))
        pic += 1
        return pic
    except:
        pass

    try:
        try:
            x = user_driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/div[1]/div/div/div/div[1]/'
                                                  'div/img')
        except:
            x = user_driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/div[1]/div/div/div[1]/'
                                                  'div[1]/img')
        src = x.get_attribute('src')
        urllib.request.urlretrieve(src, './%s/pic/%s_%d.png' % (name, name, pic))
        pic += 1
        return pic
    except:
        pass

    try:
        try:
            x = user_driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/div[1]/div/div/div/div[2]/'
                                                  'div/div/div/ul/li[1]/div/div/div/div/div[1]/div/div/img')
        except:
            x = user_driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/div[1]/div/div/div/div[2]/'
                                                  'div/div/div/ul/li[1]/div/div/div/div[1]/img')
        src = x.get_attribute('src')
        urllib.request.urlretrieve(src, './%s/pic/%s_%d.png' % (name, name, pic))
        pic += 1
        user_driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/div[1]/div/div/div/div[2]/'
                                          'button').click()
    except:
        try:
            x = user_driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/div[1]/div/div/div/div[2]/'
                                                  'div/div/div/ul/li[1]/div/div/div/div/div[1]/div/img')
        except:
            x = user_driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/div[1]/div/div/div/div[2]/'
                                                  'div/div/div/ul/li[1]/div/div/div/div[1]/div[1]/img')
        src = x.get_attribute('src')
        urllib.request.urlretrieve(src, './%s/pic/%s_%d.png' % (name, name, pic))
        pic += 1
        user_driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/div[1]/div/div/div/div[2]/'
                                          'button').click()

    i = 2
    while True:
        try:
            try:
                x = user_driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/div[1]/div/div/div/div[2]/'
                                                      'div/div/div/ul/li[%d]/div/div/div/div/div[1]/div/div/img' % i)
            except:
                x = user_driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/div[1]/div/div/div/div[2]/'
                                                      'div/div/div/ul/li[%d]/div/div/div/div/div[1]/img' % i)
            src = x.get_attribute('src')
            urllib.request.urlretrieve(src, './%s/pic/%s_%d.png' % (name, name, pic))
            pic += 1
            i += 1
            user_driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/div[1]/div/div/div/div[2]/'
                                              'button[2]').click()
        except:
            return pic
