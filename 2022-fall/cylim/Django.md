## Django 실행 및 구조

1. 메인 project와 app은 따로 존재하며 보통 작업은 app에서 진행된다. project에서 중요한 부분은 settings.py와 urls.py이다.
2. urls.py는 app의 html에 주소를 부여해주는 역할을 한다.
3. models.py에서 모델 모양을 만들고 views.py에서 model을 불러오고 html과 통합하는 기능을 하는데 사실 models를 views.py에서 불러오고 거기서 다 해도 된다.
4. (appname)/templates/(appname)/xxx.html또는 views.py을 urls.py에서 연결해 위치를 지정 가능하다.
5. 

## 주의점

1. from .abc import (함수)
2. settings.py    INSTALLED_APPS    ex) polls.apps.PollsConfig, fold.apps.FoldConfig 
3. settings.py   Allowed host에 ALLOWED_HOSTS = ['localhost', '163.152.25.210']
4. Model에 추가한 다음에는    python manage.py makemigrations, python manage.py migrate
5. (appname)/templates/(appname)/xxx.html
6. 
