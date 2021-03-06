# 인스타그램 인플루언서 정보 크롤링(스크래핑)
> Instagram crawling(scraping), Instagram爬虫

## 요약
- 배경과 가치

스마트폰의 보급과 영상 인터넷 기술이 발전하면서, SNS가 주는 영향력이 TV를 넘어서기 시작했다. SNS에서 가장 많은 영향력을 갖고 있는 인플루언서들은 자신의 생각, 가치, 패션, 소비 등 여러 방면에서 홍보를 하고 영향을 주는데, 이 영향력을 활용한 소셜커머스도 등장하면서, 인플루언서의 시장은 점점 커지고 있는 추세이다.

하지만 커지고 있는 몸집에 비해, 정교함은 다소 부족하다. 예를 들어 개인 판매를 하는 인플루언서들의 소비자들의 소비가 보호 되지 않는 문제, 허위광고의 문제, 신뢰할 수 없는 정보의 문제 등이 있다. SNS는 소통의 가면을 쓰고 있다고 생각을 한다, 겉으로는 양방향적인 소통 같지만, 인플루언서는 수많은 댓글과 메시지에 모두 소통하는 건 불가능한 일이다. 때문에 중재자 역할을 할 수 있는지, 어떻게 하는지에 대한 조사로 프로젝트가 시작되었다.

- 목적과 목표

크롤링 작업의 주목적은 조사 업무의 편리성을 제공하는 것이다. 분석과 조사를 하는 기획자들은 인플루언서 목록을 받으면, 조사를 위해 아이디를 일일이 웹사이트에 입력하고 게시물 하나하나를 클릭하여 열람하고, 스크롤을 하는 불편함을 갖고 있다. 기획에 몰두하기 보단 단순하고 불필요한 작업으로 집중력과 창의력을 잃을 수 있다. 

때문에 기획자가 원하는 인스타그램 데이터 정보를 빠르게 전달 할 수 있어야한다. 핵심이 되는 정보로는 사진, bio, 게시글, 댓글 등이 있다. 기획자가 요청한 리스트를 받으면 작업을 거쳐 정보를 전달한다. 또한 데이터 분석에도 도움을 줄 수 있다. 기획자는 데이터를 기반으로 가설을 세우고, 해당 가설을 데이터를 통해 입증을 한다. 요청하는 특징을 데이터 분석을 통해 찾는다.

## 개발단계의 변화
### [1단계 Selenium](https://github.com/Jin5823/instagram_crawling/tree/master/instagram_crawling_selenium)
- 요약

기획자의 단순 서칭 작업을 자동하는 하는 의도로 시작하였으며, 데이터 수집은 서비스의 주목적이 아니기 때문에, 성능보다는 데이터 전달에 더 집중을 했다. 때문에 가장 간편하고, 빠르게 접근할 수 있는 selenium을 통해 웹페이지의 정보를 파싱하여 저장했다.

- 주요기능표

|명칭|설명|
|:-|:-|
|로그인|많은 게시물을 열람하기 위해서는 로그인이필요하며, selenium을 통해 로그인 세션을 유지한다.|
|기본정보|bio, link, 스토리 그리고 팔로잉 팔로워와 같은 기본정보를 찾아서 저장한다.|
|게시글정보|게시물을 하나하나식 열람하여, 작성된 글과 사진 그리고 좋아요 댓글과 같은 정보를 저장한다.|

- 결과물

<img src="https://raw.githubusercontent.com/Jin5823/Git-Test/master/src/img_1.png" />

### [2단계 Api](https://github.com/Jin5823/instagram_crawling/tree/master/instagram_crawling_api)
- 요약

웹사이트를 통해 스크래핑하는 1단계 방식은 많은 양의 인플루언서 리스트 데이터를 소화해내지 못했고, 한계가 명확했었다. 비효율적인 로직과, 헤비한 로딩으로인해 10만번 이상 접근하는 것에 무리가 있었다. 그래서 찾은 대안으로 인스타그램의 [1.0 버전의 Api](https://instagram.api-docs.io/)를 사용했다. 웹사이트가 아닌 모바일기기를 위한 Api이며, 관련된 오픈프로젝트를 사용했다. [오픈프로젝트](https://pypi.org/project/InstagramAPI/)는 모바일 기기정보를 생성하여 헤더값으로 사용하고, 인스타그램의 API를 통해 데이터를 받았다. 

- 주요기능표

|명칭|설명|
|:-|:-|
|로그인|Api를 통해 로그인하고 토큰을 받는다.|
|기본정보|bio, link, 스토리 그리고 팔로잉 팔로워 등 Api에서 제공하는 데이터를 받는다. 스크래핑하는 1단계 방식보다 더 많은 데이터를 얻는다.|
|게시글정보|게시글의 정보가 Json 형태로 리스트에 담겨서 제공되기에, 더 빠르고 더 다양한 정보를 받을 수 있다.|
|PK정보|웹 스크래핑하는 1단계에서는 인플루언서의 ID정보를 기록했지만, 인스타그램 내부에서 사용하는 변하지 않는 고유식별번호인 PK정보를 사용할수 있다.|
|사용자인증|API사용중 서버측에서 어뷰징으로 판단될 경우 해제할 수 있다.|

- 결과물

> 인플루언서의 기본정보
<img src="https://raw.githubusercontent.com/Jin5823/Git-Test/master/src/img_2.JPG" />

> 인플루언서간의 영향력
<img src="https://raw.githubusercontent.com/Jin5823/Git-Test/master/src/img_4.JPG" />

### [3단계 Graphql Api](https://github.com/Jin5823/instagram_crawling/tree/master/instagram_crawling_graphql)
- 요약

인스타그램의 [1.0 버전의 Api](https://instagram.api-docs.io/)를 사용하던 중 인스타그램은 어뷰징과 봇에 대해 [업데이트](https://www.i-boss.co.kr/ab-6141-40833)를 하였고 계정별로 계정지수가 생겨 과도한 Api 요청을 못하게 막았다. 그로인해 여러계정을 사용해도 100만번 이상의 조회는 힘들어졌다, Api 일시정지를 받은 계정이 모바일기기에서는 페이지가 로딩되지 않지만, 웹에서는 로딩이되는 현상을 우연히 발견하게 되고, 브라우저의 개발자도구를 통해 인스타그램 웹페이지를 살피는 중 인스타그램이 제공하는 [퍼블릭 graphql api](https://carloshenriquereis-17318.medium.com/how-to-get-data-from-a-public-instagram-profile-edc6704c9b45)를 발견했다. Get 요청을 보내면 Json 형태로 응답을 해주는 간단한 Api이며, [파싱](https://medium.com/dataseries/easy-way-to-crawl-instagram-using-instalooter-20846d55cc64)을 통해 필요한 데이터를 DB, 엑셀에 저장하고 관리했다.

- 주요기능표

|명칭|설명|
|:-|:-|
|기본정보|bio, link, 스토리 그리고 팔로잉 팔로워 등 Api에서 제공하는 데이터를 받는다.|
|게시글정보|Json 형태로 제공된 게시글의 정보를 받는다.|
|PK정보|1.0 버전의 Api과 동일한 pk 정보를 사용한다.|

- 결과물

<img src="https://raw.githubusercontent.com/Jin5823/Git-Test/master/src/img_3.png" />

## 결론 및 토론

수백만 개의 [인스타그램 계정](https://github.com/Jin5823/instagram_in_store) 중에 인플루언서를 찾아내고, 그중에 기획자의 의도에 적합한 그리고 서비스에 적합한 인플루언서를 찾기 위해서 데이터를 크롤링하고 분석하는 작업은 필수적이라 느꼈다. 

분석 작업으로 인플루언서의 팔로워중 인플루언서가 몇 명 있는지를 통해 [인플루언서간의 영향력점수](https://github.com/Jin5823/instagram_crawling/tree/master/instagram_crawling_api)를 매기기도 하고, 인스타그램 계정의 게시글과 유저의 정보를 토대로 [한국계정](https://github.com/Jin5823/instagram_crawling/tree/master/instagram_crawling_api)인지 확인하면서 인플루언서의 팔로워 중에 한국계정이 몇 있는지도 확인했다. 또한 [인플루언서의 카테고리](https://github.com/Jin5823/instagram_crawling/tree/master/instagram_classification)를 알고리즘을 통해 자동으로 나누어 기획자의 의도에 적합한 인플루언서 정보를 얻을 수 있었다. 데이터 수집은 서비스의 주목적이 아니기 때문에, 성능보다는 데이터 전달과 분석에 더 집중하여 시간을 절약할 수 있었다. 
