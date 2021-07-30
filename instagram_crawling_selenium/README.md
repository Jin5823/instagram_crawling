# Instagram crawling selenium

### 구조

웹사이트를 자동으로 순차적으로 방문하고, 해당 페이지에서 필요한 정보를 스크래핑한다.  
개발방식은 함수들로 구성된 순차지향 프로그래밍방식으로, 기능을 담당하는 함수를 작성하고, `main.py`에서 필요한 함수를 호출하는 방식으로 원하는 결과를 저장한다.  
Selenium 패키지를 사용하고, 패키지의 사용법에 맞게 반복해서 호출가능한 함수를 `function.py`에 작성한다. `main.py`에서는 함수를 순차적으로 호출한다.  

### 요소

|함수명|파일|목적|
|:-|:-|:-|
|`driver_setting`|`function.py`|Selenium의 크롬 드라이버 기본설정 세팅|
|`login`|`function.py`|인스타그램 페이지 로그인|
|`basics_info`|`function.py`|방문한 대상의 기본 정보저장|
|`first_post_click`|`function.py`|첫번째 게시물 클릭하여 이동|
|`next_post_click`|`function.py`|다음 게시물로 이동|
|`prev_post_click`|`function.py`|이전 게시물로 이동|
|`post_time`|`function.py`|게시물의 게시시간 저장|
|`post_comment`|`function.py`|게시물의 댓글 저장|
|`post_words`|`function.py`|게시물에 작성된 글 저장|
|`post_like`|`function.py`|게시물의 좋아요수 저장|
|`post_lmg`|`function.py`|게시물의 이미지 저장|


### 결과 분석

Selenium을 활용한 스크래핑은 단순한 로직으로 간단하게 웹페이지를 방문하고 원하는 데이터를 가지고 올 수 있다는 장점이 있다. 코드를 짜는 시간도 많이 단축되지만, 웹페이지의 변화에 취약하고, 결과를 얻기까지 시간이 많이 소요된다는 단점이 있다. 웹 스크래핑은 Api가 없을 경우 그리고 간단하게 사용할 때 유용하다. 
