import json
import time
import random
import requests


class InstagramWEBAPI:
    """
    past hash
    472f257a40c653c64c666ce877d59d2b
    f045d723b6f7f8cc299d62b57abd500a
    2c5d4d8b70cad329c4a6ebe3abb6eedd
    """

    def __init__(self, query_hash='2c5d4d8b70cad329c4a6ebe3abb6eedd'):
        self.time_min = 0.04
        self.time_max = 0.06
        self.proxy_url = 'http://unblockthatsite.net/browse.php?u=%s&b=0&f=norefer'
        self.proxy_feed_url = 'https%3A%2F%2Fwww.instagram.com%2Fgraphql%2Fquery%2F%3Fquery_hash%3D{0}%26variables%3D%7B%2522id%2522%3A%2522{1}%2522%2C%2522first%2522%3A50%2C%2522after%2522%3A%2522{2}%2522%7D'
        self.feed_url = 'https://www.instagram.com/graphql/query/?query_hash=%s&variables=%s'
        self.user_url = 'https://www.instagram.com/%s/?__a=1'
        self.variables = '{"id":"%s","first":50,"after":"%s"}'
        self.query_hash = query_hash
        self.last_id = ''

    def headers_update(self, re_url):
        path_url = ''
        if 'graphql' in re_url:
            path_url = re_url[25:]
        headers = {
            'authority': 'www.instagram.com',
            'method': 'GET',
            'path': path_url,
            'scheme': 'https',
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'ko,en-US;q=0.9,en;q=0.8,zh-TW;q=0.7,zh;q=0.6',
            'referer': 'https://www.instagram.com/%s/?hl=ko' % self.last_id,
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'
        }
        return headers

    def set_query(self, pk, end_cursor=''):
        re_url = self.feed_url % (self.query_hash, self.variables % (str(pk), str(end_cursor)))
        return re_url

    def send_request(self, re_url):
        headers = self.headers_update(re_url)
        except_time_wait = 10
        while True:
            try:
                time.sleep(random.uniform(self.time_min, self.time_max))
                req = requests.get(url=re_url, headers=headers)
                json_text = json.loads(req.text)
                break
            except Exception as e:
                print('Except on SendRequest (wait %d sec and resend): ' % except_time_wait + str(e))
                time.sleep(except_time_wait)
                except_time_wait -= -10

        if req.ok and 'graphql' in re_url:
            if json_text['data']['user'] and json_text['data']['user']['edge_owner_to_timeline_media']['edges']:
                self.last_id = json_text['data']['user']['edge_owner_to_timeline_media']['edges'][0]['node']['owner']['username']
            return json_text

        if req.ok and 'graphql' not in re_url:
            if json_text['graphql']['user'] and not json_text['graphql']['user']['is_private']:
                self.last_id = json_text['graphql']['user']['id']
            return json_text

        if req.status_code == 429:
            ru = random.uniform(180.3, 300.18)
            print(req.text, 'sleep', ru)
            time.sleep(ru)
            return self.send_request(re_url)
            # 429 {"message": "rate limited", "status": "fail"}

        else:
            print(req.status_code, req.text)
            return json_text

    def send_request_p(self, re_url):

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'ko,en-US;q=0.9,en;q=0.8,zh-TW;q=0.7,zh;q=0.6',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Cookie': '__cfduid=d81ec1fad5d2e81faed269821fb79d1c81574217219; __utmz=19144188.1574219048.2.2.utmcsr=kproxyx.xyz|utmccn=(referral)|utmcmd=referral|utmcct=/; s=52agmeq0lm93vm4ebl6hghe2a7; __utma=19144188.57535444.1574217220.1574219048.1574241065.3; __utmc=19144188; __utmt=1; __atuvc=7%7C47; __atuvs=5dd503285d7c2e80002; __utmb=19144188.3.10.1574241065',
            'Host': 'unblockthatsite.net',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
        }

        except_time_wait = 30
        while True:
            try:
                time.sleep(random.uniform(self.time_min, self.time_max))
                req = requests.get(url=re_url, headers=headers)
                json_text = json.loads(req.text)
                break
            except Exception as e:
                print('Except on SendRequest (wait %d sec and resend): ' % except_time_wait + str(e))
                time.sleep(except_time_wait)

        if req.ok and 'graphql' in re_url:
            if json_text['data']['user'] and json_text['data']['user']['edge_owner_to_timeline_media']['edges']:
                self.last_id = json_text['data']['user']['edge_owner_to_timeline_media']['edges'][0]['node']['owner'][
                    'username']
            return json_text

        if req.ok and 'graphql' not in re_url:
            if json_text['graphql']['user'] and not json_text['graphql']['user']['is_private']:
                self.last_id = json_text['graphql']['user']['id']
            return json_text

        if req.status_code == 429:
            ru = random.uniform(180.3, 300.18)
            print(req.text, 'sleep', ru)
            time.sleep(ru)
            self.send_request_p(re_url)
            # 429 {"message": "rate limited", "status": "fail"}

        else:
            print(req.status_code, req.text)
            return json_text

    def get_user_feed_p(self, pk, end_cursor=''):
        query = self.proxy_url % (self.proxy_feed_url.format(self.query_hash, pk, end_cursor))
        return self.send_request_p(query)

    def get_user_feed_mix(self, switch, pk, end_cursor=''):
        # switch 1 for proxy
        feed_url = self.feed_url % (self.query_hash, self.variables % (str(pk), str(end_cursor)))
        proxy_url = self.proxy_url % (self.proxy_feed_url.format(self.query_hash, pk, end_cursor))
        if switch == 1:
            headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'ko,en-US;q=0.9,en;q=0.8,zh-TW;q=0.7,zh;q=0.6',
                'Cache-Control': 'max-age=0',
                'Connection': 'keep-alive',
                'Cookie': '__cfduid=d81ec1fad5d2e81faed269821fb79d1c81574217219; s=r3rb25n1j74eh5oiumdgua0ft7; __utma=19144188.57535444.1574217220.1574217220.1574217220.1; __utmc=19144188; __utmz=19144188.1574217220.1.1.utmcsr=kproxyx.xyz|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmb=19144188.2.10.1574217220; __atuvc=2%7C47; __atuvs=5dd4a60315fd6536001',
                'Host': 'unblockthatsite.net',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
            }
            try:
                time.sleep(random.uniform(self.time_min, self.time_max))
                req = requests.get(url=proxy_url, headers=headers)
                json_text = json.loads(req.text)
            except:
                print('get err switch', switch-1)
                return False
            if req.ok:
                return json_text
            if req.status_code == 429:
                print(req.text, 'err switch', switch-1)
                return False
            else:
                print(req.status_code, req.text, switch-1)
                return False

        if switch == 0:
            headers = self.headers_update(feed_url)
            try:
                time.sleep(random.uniform(self.time_min, self.time_max))
                req = requests.get(url=feed_url, headers=headers)
                json_text = json.loads(req.text)
            except:
                print('get err switch', switch+1)
                return False
            if req.ok:
                if json_text['data']['user'] and json_text['data']['user']['edge_owner_to_timeline_media']['edges']:
                    self.last_id = json_text['data']['user']['edge_owner_to_timeline_media']['edges'][0]['node']['owner']['username']
                return json_text
            if req.status_code == 429:
                print(req.text, 'err switch', switch+1)
                return False
            else:
                print(req.status_code, req.text, switch+1)
                return False

    def get_user_feed(self, pk, end_cursor=''):
        query = self.set_query(str(pk), end_cursor)
        return self.send_request(query)

    def get_user_info(self, user_id):
        query = self.user_url % user_id
        return self.send_request(query)
