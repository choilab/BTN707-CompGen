1. readme.md 보완

- File requirement
- How to use?

- Upload input file (PDB format) to server through internet
- Running foldseek on server
- Make top ranked similarity protein list, and access link to PDB files

2. 사용 프로그램/언어

- Programs
  - Foldseek : for protein structure similarity comparision
  - Django : to connect backend server (foldseek) and frontend web (html)
- Language
  - Python 3
  - HTML
  - Javascript?


## 2. 진행단계

2-1. Backend 단계
<br/>

- Pipeline
  - Input file을 읽고, Foldseek program을 돌리고, output을 저장하고, glob 함수를 통해 해당하는 PDB 파일을 DB에서 복사
  - 파일이 저장된 이후부터 웹으로 전달하기 전까지의, backend 파이프라인 구축 완료
<br/>

2-2. Django 단계
<br/>
- 업로드된 파일을 저장하고, pipeline의 output을 웹페이지에 올려줘야 함
- html 파일을 서버에서 호스팅할 수 있게 파이썬 코드를 통해 구현

- html 파일 호스팅 및 편집
  - 튜토리얼을 통해 장고의 구조 이해
  - 명령어 및 구조 
    - django-admin startproject (이름)을 통해 프로젝트 생성
    - python managy.py runserver (IP주소)를 통해 서버 구동
    - python manage.py startapp (앱이름) 통해 앱 생성하고 프로젝트 폴더의 apps.py에 앱 추가 후 migration으로 통합
    - app의 template 폴더에서 html을 주로 호스팅하고, 이를 url.py와 view.py를 통해 백엔드와 연결

- pipeline input
  - 
