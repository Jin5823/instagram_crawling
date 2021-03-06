# Instagram crawling api
### 구조

[Api](https://instagram.api-docs.io/)는 오픈소스 [패키지](https://pypi.org/project/InstagramAPI/)를 사용한다. 패키지는 객체지향 프로그래밍방식으로 구성되어 있다.  
객체가 호출할 수 있는 함수중에 필요한 함수는 `api_guide.py`에서 다루고, 필요한 함수를 호출하여 원하는 결과를 받고 저장한다. 

### 요소

|파일명|설명|
|:-|:-|
|`api_bio.py`|유저의 기본정보를 조회하고 csv형태로 저장한다|
|`api_function.py`|한국인 계정여부를 확인한다|
|`api_guide.py`|패키지의 객체에서 사용할 함수 목록|
|`api_main.py`|좋아요를 누른 유저중 한국 계정의 수 확인|
|`challenge_required.py`|어뷰징 해제를 위한 사용자인증|
|`insa_of_insa.py`|인플루언서의 팔로워중 인플루언서가 몇 명 있는지 확인|

### 결과 분석

기능을 중심으로 패키지를 활용하였고, api 요청은 웹 스크래핑보다 가볍기에 더 빠르고 많은 데이터를 저장할 수 있었다.
