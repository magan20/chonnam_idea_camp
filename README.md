# is119_homepage

## 개발 환경 통일

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
---
#### Linter

- flake8

```bash
pip3 install flake8
```

1. command + sift + p 누른 후 **Python: Select Linter** 선택

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
#### Django
- 장고 설치

```bash
pip install django
```

- 장고 버전 확인

```python
$ python -m django --version
4.0.6
```

---
#### pip3 오류 발생 시

```bash
sudo apt install python3-pip
```

### Docker / Docker-compose

---

#### Docker 설치 (Ubuntu 기준)

**root 계정이 아닌 user 계정에서 작업할 것**

```bash
sudo apt update
sudo apt install apt-transport-https ca-certificates curl gnupg-agent software-properties-common -y
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository \
"deb [arch=amd64] https://download.docker.com/linux/ubuntu \
$(lsb_release -cs) \
stable"
sudo apt update && sudo apt install docker-ce docker-ce-cli containerd.io -y
sudo docker -v
sudo systemctl enable docker
sudo systemctl status docker

sudo usermod -aG docker $USER
```

#### Docker-compose 설치

**root 계정이 아닌 user 계정에서 작업할 것**<br>
**docker를 먼저 설치하고 docker-compose 설치할 것**

```bash
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
sudo docker-compose -version
```