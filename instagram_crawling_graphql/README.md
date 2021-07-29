## 상세페이지
### 구조

인스타그램의 [퍼블릭 graphql api](https://carloshenriquereis-17318.medium.com/how-to-get-data-from-a-public-instagram-profile-edc6704c9b45)에 요청을 보내기위해 헤더와 같은 정보와 
각기 다른 요청을 객체의 함수로 정의하고, multiprocessing 방식으로 요청을 보내고 정보를 저장한다.

### 요소

|파일명|설명|
|:-|:-|
|`InstagramWEBAPI.py`|Api의 요청과 헤더 정보를 객체의 형태로 프로그래밍|
|`data_multiprocessing.py`|멀티 프로세싱방식으로 요청하여 리턴해서 받은 Json정보를 파싱하여 저장|
|`function.py`|객체를 활용한 요청로직을 만든다. 파싱관련된 함수를 만든다|

### 결과 분석

멀티프로세싱 방식과 프록시서버를 활용하여 대기를 최소화하여 조회 테스트도 해본결과 현존하는 인스타그램 API중에서 가장 안정적이고 제약이 없는 것 같다. 
