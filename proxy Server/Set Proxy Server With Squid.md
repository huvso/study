# Set Proxy Server With Squid


## Squid
### What is Squid
 - 사전적인 의미로는 '오징어'
 - *오픈 소스(GPL)* 소프트웨어 **프록시 서버**이자 웹 캐시
 - 반복된 요청을 캐싱함으로 웹서버의 속도를 향상시킴
 - 네트워크 자원을 공유하려는 사람들에게 웹, DNS와 다른 네트워크 검색의 캐싱을 제공함
 - 트래픽을 걸러줌으로써 안정서에 도움을 주는 등에 이르기까지 광범위 하게 이용됨
- - -


## Install
### basic Intsall
```
# apt udpate
sudo apt update
sudo apt -t
```

### Service Start
```
sudo systemctl start squid
sudo systemctl enable squid
sudo systemctl restart squid
```
- - -


## Directory Structure
 - Squid Configuration File: /etc/squid/squid.conf
 - Squid Access log: /var/log/squid/access.log
 - Squid Cache log: /var/log/squid/cache.log
- - - 


## Cofiguration
### http connection
 - http_port: default는 3128 transparent mode로 바꾸길 원하면 포트 뒤에 transparent를 명시해주면 됨(http_port 8888 transparent)
 - http_access deny all: 
 - visible_hostname : squid server에 hostname을 명시 할 수 있음

### ACL(Access Control List)
 - Line Number 970 언저리에 ACL을 명시 할 수 있음

### Open Ports in Squid Proxy
 - 특정 포트만을 squid에서 사용 할 수 있도록 명시
 - acl SSL_ports port xxxx
 - acl Safe_ports port xxxx

- - -


## Squid Proxy Client Authentication
 

## 참고 URL
 - https://www.tecmint.com/install-squid-in-ubuntu/
 - http://cfile6.uf.tistory.com/attach/17645B434FA144E3022E40
 - https://www.clien.net/service/board/lecture/11500797

<!--stackedit_data:
eyJoaXN0b3J5IjpbMjA3MzY1MTQyM119
-->