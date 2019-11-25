import time
import random
import pandas as pd
from datetime import datetime
from InstagramAPI import InstagramAPI

api = InstagramAPI("id", "pw")
api.login()
# 로그인


with open('./new_influencer.txt', 'r') as f:
    influencer_id = [x.strip() for x in f.readlines()]
# 리스트 로드

now = datetime.now()
now = '%s-%s-%s %s:%s:%s' % (now.year, now.month, now.day, now.hour, now.minute, now.second)

pd_columns = ['influencer_cd', 'user_cd', 'sns_type', 'influencer_pk', 'influencer_id', 'full_name', 'profile_url', 'is_verified',
              'external_url', 'category', 'biography', 'media_count', 'usertags_count', 'total_igtv_videos',
              'follower_count', 'following_count', 'refresh_date', 'reg_date', 'is_seller']
pd_data = pd.DataFrame(columns=pd_columns)

point = 12562
influencer_pk_list = []
list_max = len(influencer_id)
for i in range(list_max):
    try:
        time.sleep(random.uniform(0.2, 0.5))
        api.searchUsername(influencer_id[i])
        dict_string = api.LastJson['user']['pk']
        print(influencer_id[i], dict_string, point-12562, list_max)
        point += 1
        influencer_pk_list.append(dict_string)
        time.sleep(random.uniform(0.2, 0.5))

        api.getUsernameInfo(dict_string)
        dict_string = api.LastJson['user']
        data = [point, None, 1, dict_string['pk'], dict_string['username'], dict_string['full_name'],
                dict_string['profile_pic_url'], dict_string['is_verified'], dict_string['external_url']]
        try:
            data.append(dict_string['category'])
        except:
            data.append(None)
        data.append(dict_string['biography'])
        data.append(dict_string['media_count'])
        data.append(dict_string['usertags_count'])
        data.append(dict_string['total_igtv_videos'])
        data.append(dict_string['follower_count'])
        data.append(dict_string['following_count'])
        data.append(now)
        data.append(now)
        data.append(None)

        d = pd.DataFrame(data=[data], columns=pd_columns)
        pd_data = pd_data.append(d)
    except:
        print('change name', influencer_id[i])
        pass

with open('./new_influencer_pk.txt', 'w') as f:
    for pk in influencer_pk_list:
        f.write("%s\n" % pk)
pd_data.to_csv("./new_influencer.csv", encoding='utf-8-sig')
