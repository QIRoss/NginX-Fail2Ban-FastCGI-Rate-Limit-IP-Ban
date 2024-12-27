# NginX Fail2Ban FastCGI Rate Limit IP Ban

Three different tests to check NginX features against DDOS.


## NginX Rate Limit
```
docker build -t nginx-rate-limit .
docker run -d -p 8080:80 --name nginx-rate-limiter nginx-rate-limit
./test_ddos.sh
```

## NginX Fail2Ban
```
docker-compose up --build
```

## NginX FastCGI IP Ban
Not working properly
```
docker-compose up --build
```