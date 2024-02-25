import requests
session = requests.Session()
user = 'allen'
password = ''
host = "http://$NGINX_SERVER/api/v1"
session.auth = (user, password)
session.verify = False
response = session.get(url=host)
Authorization=response.request.headers['Authorization']
headers = {
"Authorization": Authorization
}

#chat
question = """During the latter half of the 19th and the first decades of the 20th century, the anarchist movement flourished in most parts of the world and had a significant role in workers' struggles for emancipation.
Various anarchist schools of thought formed during this period
"""
prompt_1 = f"[INST] 請將以下句子從英文翻譯成中文: {question} [/INST]"
prompt_2 = f"[INST] <<SYS>>\nYou are a helpful assistant.\n<</SYS>>\n\n 請將以下句子從英文翻譯成中文: {question} [/INST]"

data = {
"model": "TAIDE/b.11.0.0",
"prompt": prompt_1,
"temperature": 0.2,
"top_p": 0.9,
"presence_penalty": 1,
"frequency_penalty": 1,
"max_tokens": 1000,
}
r = requests.post(host+"/completions", json=data, headers=headers)
res = r.json()["choices"][0]["text"]
print(res)
