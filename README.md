# nginx-password-validation
1. Git clone source
```
git clone https://github.com/c00cjz00/nginx-password-validation.git
```

2. Crearte account and passwd
```
htpasswd -c nginx-password-validation/etc/nginx/.htpasswd allen
```

3. Edit nginx-password-validatio/default.conf for proxy_pass 
```
# replace auth_jwt_key with "Secret for nginx"
auth_jwt_key "00112233445566778899AABBCCDDEEFF00112233445566778899AABBCCDDEEFF";
# relace $REPLACE_YOUR_TOKEN_HERE with your API KEY (Example api key from TAIDE)
proxy_set_header Authorization "Bearer $REPLACE_YOUR_TOKEN_HERE";
# relace $proxy_pass with your API HOSTNAME
proxy_pass https://td.nchc.org.tw/api/;		
```
2. 
RUN NGINX
docker run --name nginx \
-p 80:80 \
-v nginx-jwt-validatio/default.conf:/etc/nginx/conf.d/default.conf:ro \
-d docker.io/c00cjz00/nginx-jwt-validation:latest

docker run --name nginx_password \
-p 80:80 \
-v ~/nginx/password:/etc/nginx/password:ro \
-v nginx-jwt-validatio/default.conf:/etc/nginx/conf.d/default.conf:ro \


-v ~/nginx/nginx_conf:/etc/nginx:ro -v ~/nginx/html:/usr/share/nginx/html:ro -d nginx
