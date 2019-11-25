import os
import csv
import get_feed

with open('./sample_user/sample_user.txt', 'r') as f:
    id_list = [x.strip() for x in f.readlines()]

with open('./sample_user/sample_user_pk.txt', 'r') as f:
    pk_list = [int(x.strip()) for x in f.readlines()]

for i in range(len(pk_list)):
    data = get_feed.word_handling(pk_list[i])
    cnt = data.pop(-1)
    columns = ['아이디', 'PK', '단어']
    info = [id_list[i], pk_list[i], cnt]
    try:
        os.mkdir('./sample_user/%s/' % pk_list[i])
    except:
        pass
    w_csv = open('./sample_user/%s/%s_all_word.csv' % (pk_list[i], pk_list[i]), 'a', encoding='utf-8-sig', newline='')
    writer = csv.writer(w_csv)
    writer.writerow(columns)
    writer.writerow(info)
    for d in data:
        writer.writerow([' ', ' ', d])
    w_csv.close()
