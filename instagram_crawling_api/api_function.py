import re


def is_Korea(dict_string, i):
    try:
        x = dict_string[i]['caption']['text']
        hangul = re.compile('[^ \u3131-\u3163\uac00-\ud7a3]+')
        result = hangul.sub('', x).strip()
        if result != "":
            return True
    except:
        pass
    # 본문 내용에 한글이 등장하면 한국인

    try:
        x = dict_string[i]['location']['name']
        hangul = re.compile('[^ \u3131-\u3163\uac00-\ud7a3]+')
        result = hangul.sub('', x).strip()
        if result != "":
            return True
        try:
            if 'Korea' in x.split(',')[-1].strip():
                return True
        except:
            if 'Korea' in x.strip():
                return True
    except:
        pass
    # 지역 정보에 한국이 등장하면 한국인
    return False


'''먼저 한글 여부인지 확인 하고
한글이 아닐  경우 ,으로 스플릿 하여 마지막에 단어가Korea 혹은 South Korea 인지 확인
for i in range(len(dict_string['items'])):
    if api_function.is_Korea(dict_string['items'], i):
        print('is_korea')'''
