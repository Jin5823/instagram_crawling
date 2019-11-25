import json
from InstagramAPI import InstagramAPI

api = InstagramAPI("id", "pw")
api.login()

print(api.LastJson)
challenge_message = api.s.get(api.API_URL + api.LastJson['challenge']['api_path'][1:])
print(json.loads(challenge_message.text))

challenge_choice = api.s.post(api.API_URL + api.LastJson['challenge']['api_path'][1:], data={'choice': '1'})
print(json.loads(challenge_choice.text))

input_code = input('enter code')
print(input_code)

a = api.s.post(api.API_URL + api.LastJson['challenge']['api_path'][1:], data={'security_code': int(input_code)})
print(json.loads(a.text))

api.login()


# api 를 사용하여 요청을 일정 횟수 이상하면, Request problem 이 생긴다.
# ip를 바꿀 경우 인증 번호를 요청하며, 요청이 막히기도 한다.
