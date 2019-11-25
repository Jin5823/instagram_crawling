import csv
import time
import random
from InstagramAPI import InstagramAPI


with open('./ID.txt', 'r', encoding='utf-8') as f:
    influencer_id = [x.strip() for x in f.readlines()]
api = InstagramAPI("id", "pw")
api.login()
# data 가져 오고 로그인


columns = ['influencer_id', 'influencer_pk', 'the_count', 'following_influencer']
w_csv = open('./insa_of_insa.csv', 'a', encoding='utf-8-sig', newline='')
writer = csv.writer(w_csv)
writer.writerow(columns)
# csv 파일 작성


pk_id_dict = {}
data_before = []
wrong_id = []
for in_id in influencer_id:
    api.searchUsername(in_id)
    if api.LastJson['status'] == 'fail':
        wrong_id.append(in_id)
        continue
    influencer_pk = api.LastJson['user']['pk']
    print(influencer_pk)
    time.sleep(random.uniform(1.1, 2.1))
    # id를 pk 로 바꿔 주고
    pk_id_dict[influencer_pk] = in_id

    following = []
    next_max_id = True
    while next_max_id:
        print(next_max_id)
        if next_max_id is True:
            next_max_id = ''
        api.getUserFollowings(influencer_pk, maxid=next_max_id)
        following.extend(api.LastJson.get('users', []))
        next_max_id = api.LastJson.get('next_max_id', '')
        time.sleep(random.uniform(1.1, 2.1))
    # 팔로잉 유저 정보를 가져온다

    pk_list_following = [f['pk'] for f in following]
    data_before.append([influencer_pk, pk_list_following])


data_after = []
for data_b in data_before:
    search = data_b[0]
    data_after.append([search, []])
    for data_b_2 in data_before:
        if search in set(data_b_2[1]):
            data_after[-1][-1].append(data_b_2[0])
# 얼마나 매칭 되는지 확인하는데, set 으로 변경하여 in을 사용하고, 평균 O(1), 최악 O(n)의 시간복잡도를 갖고 있다


for data_a in data_after:
    temp = []
    for d in data_a[-1]:
        temp.append(pk_id_dict[d])
    writer.writerow([pk_id_dict[data_a[0]], data_a[0], len(data_a[-1])] + temp)
writer.writerow(wrong_id)
w_csv.close()
# 파일 저장

print(wrong_id)
