## Django 실행 및 구조

1. 메인 project와 app은 따로 존재하며 보통 작업은 app에서 진행된다. project에서 중요한 부분은 settings.py와 urls.py이다.
2. urls.py는 app의 html에 주소를 부여해주는 역할을 한다. 

## 주의점

1. django의 
2. settings.py에서 app을 INSTALLED_APPS에 추가해 주어야 한다. ex) polls.apps.PollsConfig, fold.apps.FoldConfig 
3. settings.py에서 Allowed host에 ALLOWED_HOSTS = ['localhost', '163.152.25.210'] 이렇게 추가해주어야 한다.
4. Model에 추가한 다음에는 python manage.py makemigrations, python manage.py migrate 해서 model을 migration 해주기
5. 'Templates' 폴더 안에 app이름으로 폴더 하나 더 만들고 그 안에 html 작성?
6. 
