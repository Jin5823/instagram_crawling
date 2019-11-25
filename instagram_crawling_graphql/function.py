import time
import timeit
import random


TODAY_100 = int(time.time()) - (100*60*60*24)
TODAY_30 = int(time.time()) - (30*60*60*24)
TODAY_7 = int(time.time()) - (7*60*60*24)


def get_30_feed_api(api, pk):
    page = 0
    maxid = ''
    start = timeit.default_timer()
    while True:
        time.sleep(random.uniform(0.01, 0.03))
        api.getUserFeed(pk, maxid=maxid)
        if api.LastJson['status'] == 'fail':
            return 'err %d' % pk
        if api.LastJson['status'] != 'fail':
            page += 1
            if 'next_max_id' not in api.LastJson:
                stop = timeit.default_timer()
                return 'page: %d, cost_time: %f, average: %f' % (page, stop - start, (stop - start) / page)
            maxid = api.LastJson['next_max_id']
            for item in api.LastJson['items']:
                if item['taken_at'] < TODAY_30:
                    stop = timeit.default_timer()
                    return 'page: %d, cost_time: %f, average: %f' % (page, stop-start, (stop-start)/page)


def get_30_feed_webapi(webapi, pk):
    page = 0
    end_cursor = ''
    start = timeit.default_timer()
    while True:
        json_text = webapi.get_user_feed(pk, end_cursor)
        if json_text['status'] != 'ok' or json_text['data']['user'] is None:
            return 'err %d' % pk
        if json_text['status'] == 'ok':
            page += 1
            if 'end_cursor' not in json_text['data']['user']['edge_owner_to_timeline_media']['page_info']:
                stop = timeit.default_timer()
                return 'page: %d, cost_time: %f, average: %f' % (page, stop - start, (stop - start) / page)
            end_cursor = json_text['data']['user']['edge_owner_to_timeline_media']['page_info']['end_cursor']
            for item in json_text['data']['user']['edge_owner_to_timeline_media']['edges']:
                if item['node']['taken_at_timestamp'] < TODAY_30:
                    stop = timeit.default_timer()
                    return 'page: %d, cost_time: %f, average: %f' % (page, stop-start, (stop-start)/page)


def get_feed_webapi(webapi, pk, day):
    end_cursor = ''
    data_all = []
    timestamp_day = int(time.time()) - (int(day) * 60 * 60 * 24)
    while True:
        json_text = webapi.get_user_feed(pk, end_cursor)
        if json_text['status'] != 'ok' or json_text['data']['user'] is None:
            return {'pk': pk, 'access': 'err'}
        if len(json_text['data']['user']['edge_owner_to_timeline_media']['edges']) < 1:
            return {'pk': pk, 'access': 'None'}
        if json_text['status'] == 'ok':
            end_cursor = json_text['data']['user']['edge_owner_to_timeline_media']['page_info']['end_cursor']
            for item in json_text['data']['user']['edge_owner_to_timeline_media']['edges']:

                data = dict()
                data['post_id'] = item['node']['id']
                data['pk'] = item['node']['owner']['id']
                data['shortcode'] = item['node']['shortcode']
                data['id'] = item['node']['owner']['username']
                data['__typename'] = item['node']['__typename']
                data['tracking_token'] = item['node']['tracking_token']
                data['comments_disabled'] = item['node']['comments_disabled']
                data['taken_at_timestamp'] = item['node']['taken_at_timestamp']
                data['thumbnail_src'] = item['node']['display_resources'][-1]['src']
                data['like_count'] = item['node']['edge_media_preview_like']['count']
                data['comment_count'] = item['node']['edge_media_to_comment']['count']
                data['tagged_user_count'] = len(item['node']['edge_media_to_tagged_user']['edges'])
                if item['node']['edge_media_to_caption']['edges']:
                    data['text'] = item['node']['edge_media_to_caption']['edges'][0]['node']['text']
                if not item['node']['edge_media_to_caption']['edges']:
                    data['text'] = None
                if data['__typename'] == 'GraphSidecar':
                    data['img_count'] = len(item['node']['edge_sidecar_to_children']['edges'])
                if data['__typename'] != 'GraphSidecar':
                    data['img_count'] = 1
                if data['__typename'] == 'GraphVideo':
                    data['video_view_count'] = item['node']['video_view_count']
                    data['video_url'] = item['node']['video_url']
                if data['__typename'] != 'GraphVideo':
                    data['video_view_count'] = None
                    data['video_url'] = None
                if item['node']['location']:
                    data['location_name'] = item['node']['location']['name']
                    data['location_id'] = item['node']['location']['id']
                if not item['node']['location']:
                    data['location_name'] = None
                    data['location_id'] = None

                data_all.append(data)
                if data['taken_at_timestamp'] < timestamp_day:
                    return data_all
            if not end_cursor:
                return data_all


def get_feed_test(webapi, pk, day):
    end_cursor = ''
    data_all = []
    timestamp_day = int(time.time()) - (int(day) * 60 * 60 * 24)
    while True:
        json_text = webapi.get_user_feed(pk, end_cursor)
        if json_text['status'] != 'ok' or json_text['data']['user'] is None:
            print(json_text)
            return {'pk': pk, 'access': 'err'}
        if len(json_text['data']['user']['edge_owner_to_timeline_media']['edges']) < 1:
            print(json_text)
            return {'pk': pk, 'access': 'None'}
        if json_text['status'] == 'ok':
            end_cursor = json_text['data']['user']['edge_owner_to_timeline_media']['page_info']['end_cursor']
            for item in json_text['data']['user']['edge_owner_to_timeline_media']['edges']:

                data = dict()

                try:
                    data['gating_info'] = item['node']['gating_info']
                    if data['gating_info']:
                        print('gating_info', item['node']['shortcode'])
                except:
                    pass

                try:
                    data['fact_check_overall_rating'] = item['node']['fact_check_overall_rating']
                    if data['fact_check_overall_rating']:
                        print('fact_check_overall_rating', item['node']['shortcode'])
                except:
                    pass

                try:
                    data['fact_check_information'] = item['node']['fact_check_information']
                    if data['fact_check_information']:
                        print('fact_check_information', item['node']['shortcode'])
                except:
                    pass

                data['taken_at_timestamp'] = item['node']['taken_at_timestamp']
                data_all.append(data)
                if data['taken_at_timestamp'] < timestamp_day:
                    return len(data_all)
            if not end_cursor:
                return len(data_all)
