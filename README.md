# broccoli
## Description
- api 연습하라고 보안같은 거 안따지고 대충 만든거
- **이거 그대로 어플 만들면 절대 안 됨.**
- https://broccoli-practice.herokuapp.com/api/user/ 에 api보내면 됨.

## REST API
- 로그인, 회원가입 말고는 전부 로그인해야만 사용가능하고 다른 사용자가 등록한 데이터 볼 수 없음
- GET /api/모델명/ -> result에는 사용자가 입력했던 데이터 최대 15개. 총 갯수는 count, 이전/다음페이지는 prev, next
- GET /api/모델명/ {검색할 내용만} -> result에는 사용자가 입력했던 데이터 중 검색결과 최대 15개. 총 갯수는 count, 이전/다음페이지는 prev, next
- POST /api/모델명/ {데이터} -> 데이터 추가
- PATCH /api/모델명/데이터id/ {수정할 내용만} -> 수정
- DELETE /api/모델명/데이터id/ -> 삭제

---
### 사용자
#### 구글로그인/가입
/oauth2/google/login/ 팝업창 열기
#### 일반로그인
```
POST /auth/login/ {"username":아이디, "password":비번}
```
#### 30일간 자동로그인
```
POST /auth/login/ {"username":아이디, "password":비번, "auto_login":true}
```
#### 로그아웃
```
GET /auth/logout/
```
#### 회원가입
```
POST /api/user/ {"username":아이디, "password":비번}
```
#### 수정
```
PATCH /api/user/사용자id/ {"username":아이디, "password":비번}
```
#### 탈퇴
```
DELETE /api/user/사용자id/
```

---
### 아기
#### 목록
```
GET /api/baby/
```
#### 등록
```
POST /api/baby/ {"name":이름, "birth":생일(YYYY-MM-DD)}
```
#### 수정
```
PATCH /api/baby/아기id/ {"name":이름, "birth":생일(YYYY-MM-DD)}
```
#### 삭제
```
DELETE /api/baby/아기id/
```

---
### 메모
#### 목록
```
GET /api/memo/
```
```
GET /api/memo/ {"content":검색어}
```
#### 등록
```
POST /api/memo/ {"content":내용}
```
#### 수정
```
PATCH /api/memo/메모id/ {"content":내용}
```
#### 삭제
```
DELETE /api/memo/메모id/
```

---
### 팁
#### 목록
```
GET /api/tip/
```
```
GET /api/tip/ {"content":검색어}
```
#### 등록
```
POST /api/tip/ {"content":내용}
```
#### 수정
```
PATCH /api/tip/팁id/ {"content":내용}
```
#### 삭제
```
DELETE /api/tip/팁id/
```

---
### 식단
#### 목록
```
GET /api/calendar/
```
```
GET /api/calendar/ {"baby":아기id, "food":음식id, "year":먹일년도, "month":먹일달, "date":먹일날짜, "reaction":반응}
```
#### 등록
##### 하루
```
POST /api/calendar/ {
  "baby":아기id,
  "datetime":먹일시간(YYYY-MM-DD HH:mm:ss),
  "recipe":[
    {"ingredient":"재료1", "grams":12},
    {"ingredient":"재료2", "grams":34}
  ],
}
```
##### 여러날 한번에
```
POST /api/calendar/ {
  "baby":3,
  "datetime":먹일시간(YYYY-MM-DD HH:mm:ss),
  "recipe":[
    {"ingredient":"재료1", "grams":12},
    {"ingredient":"재료2", "grams":34}
  ],
  "days":3 # 먹일 날짜 수
}
```
#### 수정
```
PATCH /api/calendar/식단id/ {
  "baby":아기id,
  "datetime":먹일시간(YYYY-MM-DD HH:mm:ss),
  "recipe":[
    {"ingredient":"재료1", "grams":12},
    {"ingredient":"재료2", "grams":34}
  ],
  "reaction":반응
}
```
