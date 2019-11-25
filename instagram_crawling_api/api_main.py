import api_function
from InstagramAPI import InstagramAPI

api = InstagramAPI("id", "pw")
api.login()
# 로그인

api.getUserFeed(211106501)
dict_string = api.LastJson
print(dict_string)


api.getMediaLikers('2103052416961245595_211106501')
dict_string = api.LastJson
korea = 0
priv = 0
print(dict_string)
for i in range(len(dict_string['users'])):
    x = dict_string['users'][i]['pk']
    # print(dict_string)
    try:
        api.getUserFeed(x)
        new_string = api.LastJson
        for j in range(len(new_string['items'])):
            if api_function.is_Korea(new_string['items'], j):
                korea += 1
                break
    except:
        priv += 1
        pass

print(korea)
print(priv)
# 좋아요를 누른 사람이 한국 국적인지 출력

# print(dict_string['next_max_id'])
