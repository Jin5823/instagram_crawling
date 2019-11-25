import csv
import InstagramWEBAPI
from tqdm import tqdm
from multiprocessing import Process

api = InstagramWEBAPI.InstagramWEBAPI()


def get_feed(name, data_list):
    pk = ''
    info = api.get_user_info(name)
    if 'graphql' in info:
        if 'user' in info['graphql']:
            pk = info['graphql']['user']['id']
    if not pk:
        print('err_info', info)
        return pk
    del info

    end_cursor = ''
    # 한 페이지당 50 개
    for i in range(20):
        data = api.get_user_feed(pk, end_cursor)
        '''while True:
            data = api.get_user_feed_mix(switch, pk, end_cursor)
            if data:
                break
            if switch == 0:
                switch = 1
            else:
                switch = 0'''
        if 'data' in data:
            if 'user' in data['data']:
                if 'edge_owner_to_timeline_media' in data['data']['user']:
                    if 'edges' in data['data']['user']['edge_owner_to_timeline_media']:
                        for media_edges in data['data']['user']['edge_owner_to_timeline_media']['edges']:
                            for text_edges in media_edges['node']['edge_media_to_caption']['edges']:
                                text = text_edges['node']['text']
                                data_list.append(text.replace("\n", " "))
                            '''for comment_edges in media_edges['node']['edge_media_to_comment']['edges']:
                                if int(comment_edges['node']['owner']['id']) == int(pk):
                                    comment = comment_edges['node']['text']
                                    data_list.append(comment)'''

                    if data['data']['user']['edge_owner_to_timeline_media']['page_info']['has_next_page']:
                        end_cursor = data['data']['user']['edge_owner_to_timeline_media']['page_info']['end_cursor']
                    else:
                        break
        else:
            print('err_data', data)

    return pk


def get_insta():
    category_list = ['interior', 'parental', 'food', 'cafe']
    for category in category_list:
        csv_file = open('./result/%s_feed.csv' % category, 'a', encoding='utf-8-sig', newline='')
        writer = csv.writer(csv_file)

        with open('./for_classification/category/_list/%s.txt' % category, 'r') as f:
            pid_list = [x.strip() for x in f.readlines()]

        for pid in tqdm(range(len(pid_list))):

            user_pid = pid_list[pid]
            data_text = []
            user_pk = get_feed(user_pid, data_text)
            if not user_pk:
                print(user_pk)
                continue

            for dt in data_text:
                writer.writerow([dt, user_pk, user_pid, category])
        csv_file.close()


def start():
    proc = Process(target=get_insta, args=())
    proc.start()


if __name__ == "__main__":
    start()
