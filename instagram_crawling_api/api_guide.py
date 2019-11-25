from InstagramAPI import InstagramAPI

api = InstagramAPI("id", "pw")
api.login()
# 로그인을 하는 부분

api.getUsernameInfo(4294967295)
print(api.LastJson)
# self.SendRequest('users/' + 347146908 + '/info/')
# pk 를 통해 바이오를 받아 온다.

api.getUserTags(2069272512, maxid='2093797698699401312')
dict_string = api.LastJson
print(dict_string)
print(dict_string['next_max_id'])
# pk 를 통해 tag 정보를 받아오고 마지막의 next_max_id를 통해 다음 정보를 받아 온다
# 시간 은 taken_at을 통해 조절하면 된다.

api.getUserFeed(2069272512, maxid='2096158334276135610_2069272512')
dict_string = api.LastJson
print(dict_string)
print(dict_string['next_max_id'])
# pk 를 통해 feed 정보를 받아오고 next_max_id 를 통해 다음 정보를 받아 온다.
# 시간 은 taken_at을 통해 조절하면 된다.

api.getMediaComments('2095435598763415538_2069272512')
dict_string = api.LastJson
print(dict_string)
next_max = dict_string['next_max_id']
api.getMediaComments('2095435598763415538_2069272512', max_id=next_max)
dict_string = api.LastJson
print(dict_string)
# pk 를 통해 게시글의 comments 정보를 받아오고 next_max_id 를 통해 다음 정보를 받아 온다.
# 추가적인 정보가 있는지 유무는 has_more_comments 를 통해 확인한다.

api.searchUsername('chachaworks')
if api.LastJson['status'] == 'fail':
    print('n')
print(api.LastJson)
if 'user' in api.LastJson:
    print('y')
# id를 통해 pk 정보를 받아 온다.

'''x = api.getHighlights(4294967295)
print(api.LastJson)'''
