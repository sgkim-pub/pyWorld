# [웹 개발 새로고침](https://github.com/sgkim-pub/pyBook)

![입체_웹개발새로고침_766x766_72DPI](https://github.com/sgkim-pub/pyWorld/assets/77865135/8500678b-5ed5-415d-bcc8-ca9e88d35f52)

책의 2장 전반부 '웹 프로그램 기본 구조와 작동 원리'의 예제 코드들을 살펴보실 수 있습니다.

책의 2장 후반부의 'HTML, JavaScript' 예제 코드들은 아래 위치에서 찾으실 수 있습니다.

[2장 후반부 - HTML, JavaScript](https://github.com/sgkim-pub/html_js)

책의 3장, 4장에 해당하는 예제 코드들은 아래 위치에서 찾으실 수 있습니다.

[3장, 4장 - 웹 프로그램 기본 기능 만들기, 중고 서적 거래 서비스 만들기](https://github.com/sgkim-pub/pyBook)

---

안녕하세요? 아래와 같은 오류로 파이썬 플라스크를 사용하는 예제의 백엔드 코드가 실행되지 않는 경우가 있습니다.

```
...
ImportError: cannot import name 'url_quote' from 'werkzeug.urls' (.../lib/python3.10/site-packages/werkzeug/urls.py)
...
```

Werkzeug는 파이썬 플라스크가 사용하는 라이브러리입니다. 이 Werkzeug의 버전이 플라스크 버전과 맞지 않아서 생기는 문제입니다.

A) 최신 버전의 플라스크를 설치해서 사용하시거나, B) 플라스크 이전 버전과 호환되는 Werkzeug 라이브러리를 재설치하시면 오류를 해결하실 수 있습니다.

A) 최신 버전의 플라스크를 설치해서 사용
```
(venv) $> pip3 install Flask
```

B) 플라스크 이전 버전(예, 2.2.2)과 호환되는 Werkzeug 라이브러리를 재설치
```
(venv) $> pip3 list
...
Flask  2.2.2
... 
Werkzeug	3.0.0
...
(venv) $> pip3 uninstall Werkzeug
(venv) $> pip3 install Werkzeug==2.2.2
(venv) $> pip3 list
...
Flask  2.2.2
...
Werkzeug	2.2.2
...
```
