# 가상머신에 ubuntu 18.04 server 설치하기

## 가상머신에 우분투 디스크 이미지 삽입
<img src="https://github.com/huvso/study/blob/master/VirtualBox/02%20install%20ubuntu/img/01_marked.png?raw=true" align="center" title="install ubuntu 01" alt="install ubuntu 01"></img>
```
1. Ubuntu를 설치하고자 하는 가상 머신에 마우스 우측 클릭
2. 설정 클릭
```
******************

<img src="https://github.com/huvso/study/blob/master/VirtualBox/02%20install%20ubuntu/img/02_marked.png?raw=true" align="center" title="install ubuntu 02" alt="install ubuntu 02"></img>
```
1. 저장소 클릭
```
******************

<img src="https://github.com/huvso/study/blob/master/VirtualBox/02%20install%20ubuntu/img/04_marked.png?raw=true" align="center" title="install ubuntu 03" alt="install ubuntu 03"></img>
```
1. 디스크 이미지 클릭
2. Choose a disk file 클릭
```
******************

<img src="https://github.com/huvso/study/blob/master/VirtualBox/02%20install%20ubuntu/img/05_marked.png?raw=true" align="center" title="install ubuntu 05" alt="install ubuntu 05"></img>
```
1. 다운받은 iso 파일 선택
2. 열기 버튼 클릭
```
******************

<img src="https://github.com/huvso/study/blob/master/VirtualBox/02%20install%20ubuntu/img/06_marked.png?raw=true" align="center" title="install ubuntu 06" alt="install ubuntu 06"></img>
```
1. 컨트롤러: IDE에 이미지 삽입 확인
2. 확인 버튼 클릭
```
******************

## 우분투 설치

<img src="https://github.com/huvso/study/blob/master/VirtualBox/02%20install%20ubuntu/img/00_marked.png?raw=true" align="center" title="install ubuntu 00" alt="install ubuntu 00"></img>
```
1. 가상머신 더블 클릭
```
******************

<img src="https://github.com/huvso/study/blob/master/VirtualBox/02%20install%20ubuntu/img/07.png?raw=true" align="center" title="install ubuntu 07" alt="install ubuntu 07"></img>
```
1. 기다리기
```
******************

<img src="https://github.com/huvso/study/blob/master/VirtualBox/02%20install%20ubuntu/img/08.png?raw=true" align="center" title="install ubuntu 08" alt="install ubuntu 08"></img>
```
1. English 선택 후 엔터
```
******************

<img src="https://github.com/huvso/study/blob/master/VirtualBox/02%20install%20ubuntu/img/09.png?raw=true" align="center" title="install ubuntu 09" alt="install ubuntu 09"></img>
```
1. Continue without updating 선택 후 엔터
```
******************

<img src="https://github.com/huvso/study/blob/master/VirtualBox/02%20install%20ubuntu/img/10.png?raw=true" align="center" title="install ubuntu 10" alt="install ubuntu 10"></img>
```
1. IP 설정 후 Done 엔터
```
******************

<img src="https://github.com/huvso/study/blob/master/VirtualBox/02%20install%20ubuntu/img/11.png?raw=true" align="center" title="install ubuntu 11" alt="install ubuntu 11"></img>
```
1. Proxy 설정 없이 Done 엔터
```
******************

<img src="https://github.com/huvso/study/blob/master/VirtualBox/02%20install%20ubuntu/img/12.png?raw=true" align="center" title="install ubuntu 12" alt="install ubuntu 12"></img>
```
1. Done 엔터
```
******************

<img src="https://github.com/huvso/study/blob/master/VirtualBox/02%20install%20ubuntu/img/13.png?raw=true" align="center" title="install ubuntu 13" alt="install ubuntu 13"></img>
```
1. Use An Entire Disk 선택 후 엔터
```
******************

<img src="https://github.com/huvso/study/blob/master/VirtualBox/02%20install%20ubuntu/img/14.png?raw=true" align="center" title="install ubuntu 14" alt="install ubuntu 14"></img>
```
1. 엔터
```
******************

<img src="https://github.com/huvso/study/blob/master/VirtualBox/02%20install%20ubuntu/img/15.png?raw=true" align="center" title="install ubuntu 15" alt="install ubuntu 15"></img>
```
1. Done 엔터
```
******************

<img src="https://github.com/huvso/study/blob/master/VirtualBox/02%20install%20ubuntu/img/16.png?raw=true" align="center" title="install ubuntu 16" alt="install ubuntu 16"></img>
```
1. Continue 엔터
```
******************

<img src="https://github.com/huvso/study/blob/master/VirtualBox/02%20install%20ubuntu/img/17.png?raw=true" align="center" title="install ubuntu 17" alt="install ubuntu 17"></img>
```
1. 서버이름, 유저이름, 패스워드 입력
2. Done 엔터
```
******************

<img src="https://github.com/huvso/study/blob/master/VirtualBox/02%20install%20ubuntu/img/18.png?raw=true" align="center" title="install ubuntu 18" alt="install ubuntu 18"></img>
```
1. Install OpenSSH server 선택
2. Done 엔터
```
******************

<img src="https://github.com/huvso/study/blob/master/VirtualBox/02%20install%20ubuntu/img/19.png?raw=true" align="center" title="install ubuntu 19" alt="install ubuntu 19"></img>
```
1. server 관리 시 필요한 패키지 선택 후
2. Done 엔터
```

* 패키지 정보

|Pacakage Name|Description|
|-------------|-----------|
|microk8s|Kubernetes for workstations and appliances|
|nextcloud|Nextcloud Server - A safe home for all your data|
|wekan|Open-Source Kanban|
|kata-containers|Lightweight virtual machines that seamlessly plug into the containers ecosystem|
|docker|Docker container runtime|
|canonical-livepatch|Canonical Livepatch Client|
|rocketchat-server|Group chat server for 100s, installed in seconds.|
|mosquitto|Eclipse Mosquitto MQTT broker|
|etcd|Resilient key-value store by CoreOS|
|powershell|PowerShell for every system!|
|stress-ng|A tool to load, stress test and benchmark a computer|
|sabnzbd|SABnzbd|
|worwhole|get things from one computer to another, safely|
|aws-cli|Universal Command Line Interface for Amazon Web Server|
|google-cloud-sdk|Command-line interface for Google Cloud Platform products and services|
|slcli|Python based SoftLayer API Tool|
|doctl|DigitalOcean command line tool|
|conjure-up|Package runtime for conjure-up spells|
|minidlna-escoand|server software with the aim of being fully compliant with DLNA/UPnP clients.|
|postgresql10|PostgreSQL is a powerful, open source object-relational database system.|
|heroku|CLI client for Heroku|
|keepalived|High availability VRRP/BFD and load-balancing for Linux|
|prometheus|The Prometheus monitoring system and time series database|
|juju|Simple, secure and stable devops. Juju keeps complexity low and productivity high. Manage applications wherever they are run.|
******************

<img src="https://github.com/huvso/study/blob/master/VirtualBox/02%20install%20ubuntu/img/21.png?raw=true" align="center" title="install ubuntu 21" alt="install ubuntu 21"></img>
```
1. 설치 진행
2. 설치 완료 후 Reboot 엔터
```
******************

<img src="https://github.com/huvso/study/blob/master/VirtualBox/02%20install%20ubuntu/img/22.png?raw=true" align="center" title="install ubuntu 22" alt="install ubuntu 22"></img>
```
1. 우분투 미디어 제거를 위해 엔터
```
******************