import os
import csv
import random
import word_handling

category_list = ['fashion', 'food', 'health', 'interior', 'moms', 'pet', 'travel']

for category in category_list:
    try:
        os.mkdir('./category/%s' % category)
    except:
        pass

    columns = ['influencer_pk', 'influencer_id', 'influencer_category', 'all_feed_word', 'word_count']
    csvFile = open('./category/%s/%s_feed_word.csv' % (category, category), 'a', encoding='utf-8-sig', newline='')
    writer = csv.writer(csvFile)
    writer.writerow(columns)
    csv_max = 0
    temp = 2

    with open('./category/_list/%s.txt' % category, 'r') as f:
        pk_list = [int(x) for x in f.readlines()]
    pk_list = random.sample(pk_list, 120)
    # 120명 랜덤으로 고정

    p = 0
    pk_max = len(pk_list)
    for pk in range(pk_max):
        print(p, '/', pk_max)
        p += 1
        user_pk = pk_list[pk]
        try:
            url_string = word_handling.word_handling(user_pk)
            all_word = len(url_string['all_feed_word_cnt'])
        except:
            continue

        for i in range(all_word):
            data = ['', '', '', url_string['all_feed_word_cnt'][i][0], url_string['all_feed_word_cnt'][i][1]]
            if i == 0:
                data[0] = url_string['influencer_pk']
                data[1] = url_string['influencer_id']
                data[2] = category
            writer.writerow(data)
            csv_max += 1

        data = ['', '', '', '', '']
        writer.writerow(data)

        if csv_max > 940000:
            csvFile.close()
            columns = ['influencer_pk', 'influencer_id', 'influencer_category', 'all_feed_word', 'word_count']
            csvFile = open('./category/%s/%s_feed_word%d.csv' % (category, category, temp), 'a', encoding='utf-8-sig',
                           newline='')
            writer = csv.writer(csvFile)
            writer.writerow(columns)
            csv_max = 0
            temp += 1

    print('done %s' % category)
    csvFile.close()

