# fmgmt
가계부 만들기

------ chatGPT -------
my_budget_django_project: Django 프로젝트 디렉토리입니다. 여기에는 Django 프로젝트 설정 파일(settings.py, urls.py 등)과 Django 애플리케이션을 관리합니다.

my_budget_app: Django 애플리케이션 디렉토리입니다. 여기에는 데이터 모델, 뷰 함수, 템플릿, 정적 파일 및 테스트 코드를 포함합니다.

manage.py: Django 프로젝트 관리 명령어 스크립트입니다. 서버 실행, 데이터베이스 마이그레이션 및 기타 관리 작업을 수행할 때 사용합니다.

requirements.txt: Python 패키지 종속성 목록 파일입니다. 필요한 패키지와 버전을 정의합니다.

database: 구글 스프레드시트 데이터 파일을 저장하는 디렉토리입니다. 이 디렉토리는 필요에 따라 만들고 사용할 수 있습니다.

docs: 프로젝트 문서와 설명서를 저장하는 디렉토리입니다. 프로젝트 관련 문서를 작성하여 보관합니다.

README.md: 프로젝트에 대한 간략한 설명 및 사용법을 기록하는 마크다운 파일입니다.

-------------------------

my_budget_django_project/
├── my_budget_app/            # Django 애플리케이션
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   │   ├── __init__.py
│   ├── models.py             # 데이터 모델 정의
│   ├── views.py              # 뷰 함수
│   ├── templates/            # HTML 템플릿 파일
│   ├── static/               # CSS 및 JavaScript 파일
│   └── tests/                # 테스트 코드
├── my_budget_project/        # Django 프로젝트 설정
│   ├── __init__.py
│   ├── settings.py           # 설정 파일
│   ├── urls.py               # URL 라우팅
│   ├── asgi.py
│   ├── wsgi.py
├── manage.py                 # Django 관리 명령어 스크립트
├── requirements.txt          # Python 패키지 종속성
├── database/                 # 구글 스프레드시트 데이터 파일 (옵션)
├── docs/                     # 문서 및 설명서
├── README.md                 # 프로젝트 설명 및 사용법 문서






