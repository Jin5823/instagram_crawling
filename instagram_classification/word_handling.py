import re
import time
import random
import collections
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
    next_max_id = dict_string['next_max_id']
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

    while cnt < 101:
        api.getUserFeed(u_input, next_max_id)
        time.sleep(random.uniform(1.1, 2.1))
        dict_string = api.LastJson
        try:
            next_max_id = dict_string['next_max_id']
        except:
            return cnt
        items = dict_string['items']
        for i in range(len(items)):
            x = '-'
            try:
                x = items[i]['caption']['text']
                cnt += 1
            except:
                print('no text')
            data.append(x)
            if cnt == 100:
                return cnt


def word_handling(user_input):
    text = []
    x = get_feed(user_input, text)
    if x != 100:
        print(x)
        return 0

    token = []
    tokening(text, token)

    all_token = []
    for to in token:
        for t in to:
            if len(t) > 1:
                all_token.append(t)

    all_data = []
    cnt = collections.Counter(all_token)
    for c in cnt.most_common():
        all_data.append(c)

    user_input = {"influencer_pk": int(user_input), "influencer_id": 'no need to know', "category": "-", "all_feed_word_cnt": all_data}

    return user_input
