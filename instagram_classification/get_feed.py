import re
import time
import random
from konlpy.tag import Okt
from InstagramAPI import InstagramAPI


api = InstagramAPI("id", "pw")
twitter = Okt()
api.login()


def tokening(text, token):
    for i in range(len(text)):
        if text[i] is None:
            text[i] = 'None'
        try:
            text[i] = text[i].replace("\\n", "").replace("\\", "")
        except:
            pass

    for i in text:
        x = twitter.nouns(i)
        token.append(x)


def get_feed(u_input, data):
    cnt = 0
    api.getUserFeed(u_input)
    time.sleep(random.uniform(1.1, 2.1))
    dict_string = api.LastJson
    if dict_string['status'] == 'fail':
        return print(u_input)
    try:
        next_max_id = dict_string['next_max_id']
    except:
        next_max_id = 'None'
    items = dict_string['items']
    for i in range(len(items)):
        x = '-'
        try:
            x = items[i]['caption']['text']
            cnt += 1
        except:
            print('no text')
        data.append(x)
    print(u_input)
    if next_max_id == 'None':
        return print(cnt, u_input)
    while cnt < 51:
        api.getUserFeed(u_input, next_max_id)
        time.sleep(random.uniform(1.1, 2.1))
        dict_string = api.LastJson
        try:
            next_max_id = dict_string['next_max_id']
        except:
            return print(cnt)
        items = dict_string['items']
        for i in range(len(items)):
            x = '-'
            try:
                x = items[i]['caption']['text']
                cnt += 1
            except:
                print('no text')
            data.append(x)
            if cnt == 50:
                return print(cnt)


def word_handling(user_input):
    text = []
    get_feed(user_input, text)

    token = []
    tokening(text, token)

    all_token = []
    for to in token:
        for t in to:
            all_token.append(t)

    all_token.append(len(all_token))

    return all_token
