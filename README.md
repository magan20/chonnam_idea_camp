# 전남 아이디어 캠프

## 개발 환경 통일

### 기본 라이브러리 설치

- mysql 라이브러리
```bash
apt-get update
apt-get install python3-dev libmysqlclient-dev gcc
```

### Python
---
#### Python version

- Python 3.8.10

#### venv

- python3.8-venv

```bash
sudo apt install python3.8-venv
```

- 사용법

```bash
# 프로젝트 폴더에서
python3 -m venv {가상환경 명칭}

# e.g.
python3 -m venv venv

# activate 방법
source {path_to_venv}/bin/activate

# e.g.
source ./venv/bin/activate

# deactivate 방법
deactivate
```

- requirements 관련

```bash
# requirements 만들기 (가상환경 activate 상태라고 가정)
pip freeze > requirements.txt

# requirements 설치하기 (가상환경 activate 상태라고 가정)
pip install -r requirements.txt
```

#### django version
- 장고 버전 확인

```bash
$ python -m django --version # (가상환경 activate 상태라고 가정)
4.0.6
```

---
#### Linter

* vscode 사용 안하면 설정 할 필요 없음
- flake8

```bash
pip3 install flake8
```

1. (MAC) command + sift + p, (win) ctrl + sift + p 누른 후 **Python: Select Linter** 선택

2. **flake8** 선택

3. 이후 vscode에 **.vscode/setting.json** 파일이 생성되면서 다음과 같은 내용이 추가된다.

```json
{
  "python.linting.flake8Enabled": true,
  "python.linting.enabled": true
}
```
---
#### Formatter
* vscode 사용 안하면 설정할 필요 없음.
- black

```bash
pip3 install black
```

1. **flake8** 설정 시 생성된 **.vscode/settings.json** 내부에 두개의 값을 추가 시켜준다.

```json
"editor.formatOnSave": true,
"python.formatting.provider": "black"
```

---
#### pip3 오류 발생 시

```bash
sudo apt install python3-pip
```


### 환경 설정
 
#### .env
- .env 파일 생성
* **manage.py** 파일 위치에서 실행

```bash
touch .env
```

- .env 파일 양식
1. 아래 내용 **.env** 파일로 복사

```
# django SECRET_KEY
SECRET_KEY="your_django_secret_key" # 장고 settings.py 참고

# django DEBUG
DEBUG=True

# ALLOWED_HOSTS
TEST_HOST='your_test_host'

# DB settings
DATABASE_NAME=culture_circle
DATABASE_USER='database_user'
DATABASE_PASSWORD='database_password'
DATABASE_HOST='database_host' # ex) localhost
DATABASE_PORT='database_port'
```
2. 각 key 값에 해당하는 value 값 작성

* key=value 에서 공백이 들어가면 안됨.

#### mysql
- mysql 설치

```bash
# apt 업데이트
apt update

# mysql server 설치
sudo apt install -y mysql-server

# 서버 초기화
sudo mysql_secure_installation

```
- database 생성

```bash
mysql -u {USER} -p < createtable.sql
python manage.py migrate

# e.g.
mysql -u root -p < createtabel.sql
python manage.py migrate
```