# nginx-password-validation
1. Git clone source
```
git clone https://github.com/c00cjz00/nginx-password-validation.git
```

2. Crearte account and passwd
```
htpasswd -c nginx-password-validation/.htpasswd allen
```

3. Edit nginx-password-validatio/default.conf for proxy_pass 
```
# relace $REPLACE_YOUR_TOKEN_HERE with your API KEY (Example api key from TAIDE)
proxy_set_header Authorization "Bearer $REPLACE_YOUR_TOKEN_HERE";
# relace $proxy_pass with your API HOSTNAME
proxy_pass https://td.nchc.org.tw/api/;		
```
4. RUN NGINX
```
docker run --name nginx_password \
-p 80:80 \
-v nginx-jwt-validatio/default.conf:/etc/nginx/conf.d/default.conf:ro \
-v nginx-password-validation/.htpasswd:/etc/nginx/.htpasswd:ro \
-d nginx
```

5. Testing with curl
- replace JWT_KEY below 
```
curl -u $username:$password [http://](http://$NGINX_SERVER/api/v1)
```
- output
```
<Response [200]>
```

6. Testing with python
```
import requests
session = requests.Session()
user = 'allen'
password = ''
host = "http://$NGINX_SERVER/api/v1"
session.auth = (user, password)
response = session.get(url=host)
response.request.headers
```

7. Testing with TAIDE CHAT
- replace user and password in app.py
```
python app.py
```
- output
```
# 英文
question = """During the latter half of the 19th and the first decades of the 20th century, the anarchist movement flourished in most parts of the world and had a significant role in workers' struggles for emancipation.
Various anarchist schools of thought formed during this period

# 翻譯成中文
十九世紀後半葉及二十世紀初年，世界多數地區出現無政府主義運動，並在工人爭取解放鬥爭中發揮重要角色。這個時期內，各種無政府主義思潮也於此時形成。
```

