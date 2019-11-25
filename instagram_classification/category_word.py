import csv
import collections
import pandas as pd


category_list = ['beauty', 'fashion', 'food', 'health', 'interior', 'moms', 'pet', 'travel']

for category in category_list:
    pd_columns = ['category', 'how_many_influencer', 'words', 'words_count']
    pd_data = pd.DataFrame(columns=pd_columns)
    influencer_cnt = 0

    with open('./category/%s/%s_feed_word.csv' % (category, category), 'r', encoding='utf-8-sig') as f:
        file = [line for line in csv.reader(f)]

    data = []
    cnt = 0
    for i in range(len(file)):
        if file[i][2] == category:
            data.append(file[i][3])
            influencer_cnt += 1
        if file[i][2] == '':
            data.append(file[i][3])
        if file[i][3] == '':
            cnt += 1
        if cnt == 100:
            break

    try:
        with open('./category/%s/%s_feed_word2.csv' % (category, category), 'r', encoding='utf-8-sig') as f:
            file = [line for line in csv.reader(f)]
        for i in range(len(file)):
            if file[i][2] == category:
                data.append(file[i][3])
                influencer_cnt += 1
            if file[i][2] == '':
                data.append(file[i][3])

    except:
        pass

    all_data = []
    cnt = collections.Counter(data)
    for c in cnt.most_common():
        all_data.append(c)

    for i in range(len(all_data)):
        data = ['', '', all_data[i][0], all_data[i][1]]
        if i == 0:
            data[0] = category
            data[1] = influencer_cnt
        d = pd.DataFrame(data=[data], columns=pd_columns)
        pd_data = pd_data.append(d)

    pd_data.to_csv('./category/%s/%s_all_word_cnt.csv' % (category, category), encoding="utf-8-sig")
    print('done %s' % category)
