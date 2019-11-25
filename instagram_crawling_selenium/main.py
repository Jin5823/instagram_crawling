import os
import time
import function


name = 'chaenniiii'
driver = function.driver_setting(headless=True)
driver.get('https://www.instagram.com/%s/?hl=ko' % name)
function.login(driver)
# 로그인


pic_cnt = 1
try:
    os.mkdir("./%s/" % name)
    os.mkdir("./%s/pic" % name)
    os.mkdir("./%s/data" % name)
except:
    pass
# 디렉토리 생성


basic_info = list(function.basics_info(driver))
posts_num = [int(s) for s in basic_info[1].split() if s.isdigit()][0]


with open('./%s/data/%s_basic_info.txt' % (name, name), 'w', encoding='utf-8-sig') as f:
    for item in basic_info:
        f.write("%s\n" % item)
# bio 저장


function.first_post_click(driver)
posts = [[function.post_time(driver), function.post_words(driver), function.post_like(driver)]]
comments = [[function.post_comment(driver)]]
pic_cnt = function.post_lmg(driver, name, pic_cnt)
while True:
    posts_num = posts_num - 1
    if posts_num == 0:
        break
    try:
        function.next_post_click(driver)
        posts.append([function.post_time(driver), function.post_words(driver), function.post_like(driver)])
        comments.append(function.post_comment(driver))
        pic_cnt = function.post_lmg(driver, name, pic_cnt)
    except:
        time.sleep(60)
        function.prev_post_click(driver)
        posts_num += 1
        time.sleep(60)
# 게시글 저장

with open('./%s/data/%s_posts.txt' % (name, name), 'w', encoding='utf-8-sig') as f:
    for item in posts:
        f.write("%s\n" % item)

with open('./%s/data/%s_comments.txt' % (name, name), 'w', encoding='utf-8-sig') as f:
    for item in comments:
        f.write("%s\n" % item)
