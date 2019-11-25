import csv
import collections


# 일상과 전문에 대한 조건 함수
def classify_final(match_data):
    x = match_data[0]
    x_n = [" ", " "]
    if x[0] == '육아':
        x_n = match_data[1]
        if x[1] > 29:
            if x_n[0] == '인테리어':
                return '-'
            if x_n[0] == '펫':
                return '펫 육아'
            if x_n[0] == '푸드':
                return '푸드 육아'
            if x_n[0] == '뷰티' and x_n[1] > 20 and x[1] - x_n[1] < 21:
                return '뷰티 육아'
        if x[1] < 30:
            x_n = match_data[1]
        else:
            return x[0]
    if x[0] == '헬스':
        if x[1] < 25:
            x_n = match_data[1]
        else:
            return x[0]
    # 일상과 전문이 에매한 카테고리이며, 기준이 엄격하다

    if x[0] == '펫' or x[0] == '인테리어':
        if x[1] < 10:
            x_n = match_data[1]
        else:
            return x[0]
    # 전문 카테고리, 반드시 1순위 등장

    if x[0] == '뷰티':
        if x[1] < 30:
            x_n = match_data[1]
        else:
            return x[0]
    if x_n[0] == '뷰티':
        if int(x_n[0]) > 30:
            return x_n[0]

    if x[0] == '패션' or x[0] == '푸드' or x[0] == '여행':
        if x[1] < 8:
            x = '-'
            return x
        else:
            return x[0]

    if x_n[0] == '패션' or x_n[0] == '푸드' or x_n[0] == '여행':
        if int(x_n[1]) < 8:
            x_n = '-'
            return x_n
        else:
            return x_n[0]
    x = '-'
    return x


columns = ['아이디', '총 단어의 수', '매칭된 단어', '카테고리 분류 결과', '카테고리 최종 결과']

with open('./category/all_dist_norm.csv', 'r', encoding='utf-8-sig') as fi:
    file_1w7 = [line for line in csv.reader(fi)]
file_1w7.pop(0)

dict_1w7 = dict()
for f in file_1w7:
    for i in range(1, 9):
        f[i] = float(f[i].replace("%", ""))
    f[10] = float(f[10].replace("%", ""))
    dict_1w7[f[0]] = tuple(f[1:])

with open('./sample_user/sample_user_pk.txt', 'r') as f:
    pk_list = [int(x.strip()) for x in f.readlines()]

with open('./sample_user/sample_user.txt', 'r') as f:
    id_list = [x.strip() for x in f.readlines()]

w_csv = open('./match_category.csv', 'a', encoding='utf-8-sig', newline='')
writer = csv.writer(w_csv)
writer.writerow(columns)

for pk in pk_list:
    try:
        with open('./sample_user/%d/%d_all_word.csv' % (pk, pk), 'r', encoding='utf-8-sig') as f:
            word = [line for line in csv.reader(f)]
    except:
        continue

    word_cnt = word[1][2]
    name_id = word[1][0]
    word.pop(0)
    word.pop(0)

    word_set = []
    for w in word:
        word_set.append(w[2])
    word_set = list(set(word_set))
    # 중복 제거

    data = []
    match_word = []
    for w in word_set:
        try:
            x = dict_1w7[w]
            if float(x[9]) > 0.5:
                if float(x[0]) > 10.0 or float(x[1]) > 10.0 or float(x[2]) > 10.0 or float(x[3]) > 10.0 or\
                        float(x[4]) > 10.0 or float(x[5]) > 10.0 or float(x[6]) > 10.0 or float(x[7]) > 10.0:
                    data.append(x)
                    match_word.append(w)
                    continue

            if float(x[9]) > 0.5:
                data.append(x)
                match_word.append(w)
                continue

            if float(x[0]) > 70.0 or float(x[1]) > 70.0 or float(x[2]) > 70.0 or float(x[3]) > 70.0 or\
                    float(x[4]) > 70.0 or float(x[5]) > 70.0 or float(x[6]) > 70.0 or float(x[7]) > 70.0:
                if float(x[9]) > 0.4:
                    data.append(x)
                    match_word.append(w)
        except:
            pass

    match_class = []
    for i in data:
        match_class.append(i[8])

    all_data = []
    match_cnt = collections.Counter(match_class)
    for c in match_cnt.most_common():
        all_data.append(c)
    # 핵심 결과
    try:
        x = classify_final(all_data)
    except:
        print('no match')
        x = '-'
    writer.writerow([name_id, word_cnt, match_word, all_data, x])
    print('done', pk)

w_csv.close()
