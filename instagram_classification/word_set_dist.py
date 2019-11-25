import csv
import numpy as np


def second_largest(numbers):
    count = 0
    m1 = m2 = float('-inf')
    for n in numbers:
        count += 1
        if float(n) > m2:
            if float(n) >= m1:
                m1, m2 = float(n), m1
            else:
                m2 = float(n)
    return m2 if count >= 2 else None


def min_max_scaler(data_x):
    numerator = data_x - np.min(data_x, 0)
    denominator = np.max(data_x, 0) - np.min(data_x, 0)
    # noise term prevents the zero division
    return numerator / (denominator + 1e-7)


category_list = ['beauty', 'fashion', 'food', 'health', 'interior', 'moms', 'pet', 'travel']
columns = ['워드', '뷰티', '패션', '푸드', '헬스', '인테리어', '육아', '펫', '여행', '카테고리', '격차']

keyword_list = []
for category in category_list:
    with open('./category/%s/%s_all_word_cnt.csv' % (category, category), 'r', encoding='utf-8') as csvFile:
        for x in csv.reader(csvFile):
            if x[4] == 'words_count':
                continue
            if x[3] == '':
                continue
            keyword_list.append(x[3])

keyword_list = list(set(keyword_list))
# 분포를 확인할 키워드들
print(len(keyword_list))

w_csv = open('./category/all_dist_norm.csv', 'a', encoding='utf-8-sig', newline='')
writer = csv.writer(w_csv)
writer.writerow(columns)

with open('./category/%s/%s_all_word_cnt.csv' % (category_list[0], category_list[0]), 'r', encoding='utf-8') as csvFile:
    all_word = [x for x in csv.reader(csvFile)]
# 분포를 갖고 있는 첫 카테고리

data = []
for word in all_word:
    for keyword in keyword_list:
        if word[3] == keyword:
            data.append([word[3], ("%.2f%%" % (int(word[4]) / int(all_word[1][4]) * 100.0))])

for d in data:
    if len(d) != 2:
        d.append("0.0%")

for cl in range(1, len(category_list)):
    with open('./category/%s/%s_all_word_cnt.csv' % (category_list[cl], category_list[cl]), 'r',
              encoding='utf-8') as csvFile:
        all_word = [x for x in csv.reader(csvFile)]
    # 분포를 갖고 있는 다음 카테고리
    le_d = len(data[0]) + 1
    for word in all_word:
        for d in data:
            if word[3] == d[0]:
                d.append(("%.2f%%" % (int(word[4]) / int(all_word[1][4]) * 100.0)))

    for d in data:
        if len(d) != le_d:
            d.append("0.0%")

    print('done', cl)

for d in data:
    x = [float(x.replace("%", "")) for x in d[1:]]
    d.append(columns[x.index(max(x)) + 1])
    x = min_max_scaler(np.array(x))
    d.append(np.max(x) - second_largest(x))
    writer.writerow(d)

w_csv.close()
