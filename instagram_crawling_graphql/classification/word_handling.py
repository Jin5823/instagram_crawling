import re
import collections
import InstagramWEBAPI
from konlpy.tag import Okt

twitter = Okt()
api = InstagramWEBAPI.InstagramWEBAPI()


def demojify(string):
    return string.encode('ms949', 'ignore').decode('ms949')


def cleasing(text):
    pattern = '([ㄱ-ㅎㅏ-ㅣ]+)'
    # 한글 자음, 모음 제거
    text = re.sub(pattern=pattern, repl='', string=text)
    pattern = '<[^>]*>'  # HTML 태그 제거
    text = re.sub(pattern=pattern, repl='', string=text)
    pattern = '[^\w\s]'
    # 특수기호제거
    text = re.sub(pattern=pattern, repl='', string=text)
    return text


def tokening(text, token):
    for i in range(len(text)):
        if text[i] is None:
            text[i] = 'None'
        try:
            text[i] = text[i].replace("\\n", "").replace("\\", "")
        except:
            pass

    data = []
    for i in text:
        x = cleasing(i)
        data.append(x)
    # 특수 문자 삭제

    corpus = []
    for i in data:
        x = demojify(i)
        corpus.append(x)
    # 이모티콘 삭제

    for i in corpus:
        x = twitter.nouns(i)
        token.append(x)


def get_feed(pk, data_list):
    """pk = ''
    info = api.get_user_info(name)
    if 'graphql' in info:
        if 'user' in info['graphql']:
            pk = info['graphql']['user']['id']
    if not pk:
        print('err_info', info)
        return pk"""

    end_cursor = ''
    # 한 페이지당 50 개
    for i in range(2):
        data = api.get_user_feed(pk, end_cursor)
        if 'data' in data:
            if 'user' in data['data']:
                if 'edge_owner_to_timeline_media' in data['data']['user']:
                    if 'edges' in data['data']['user']['edge_owner_to_timeline_media']:
                        for media_edges in data['data']['user']['edge_owner_to_timeline_media']['edges']:
                            for text_edges in media_edges['node']['edge_media_to_caption']['edges']:
                                text = text_edges['node']['text']
                                data_list.append(text)
                            for comment_edges in media_edges['node']['edge_media_to_comment']['edges']:
                                if int(comment_edges['node']['owner']['id']) == int(pk):
                                    comment = comment_edges['node']['text']
                                    data_list.append(comment)

                    if data['data']['user']['edge_owner_to_timeline_media']['page_info']['has_next_page']:
                        end_cursor = data['data']['user']['edge_owner_to_timeline_media']['page_info']['end_cursor']
                    else:
                        break
        else:
            print('err_data', data)
    return pk


def word_handling(user_input):
    text = []
    pk = get_feed(user_input, text)
    if not pk:
        print(pk)
        return 0

    token = []
    tokening(text, token)

    all_token = []
    for to in token:
        for t in to:
            all_token.append(t)

    all_data = []
    cnt = collections.Counter(all_token)
    for c in cnt.most_common():
        if len(c[0]) > 1:
            all_data.append(c)

    word_count = len(all_data)
    user_input = {"influencer_pk": pk, "influencer_id": user_input, "category": "-", "all_feed_word_cnt": all_data, "word_count": word_count}

    # user_input = json.dumps(user_input, ensure_ascii=False)
    return user_input
