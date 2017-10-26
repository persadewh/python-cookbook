import requests #

headers = {
    'User-agent': 'none/ofyourbusiness',
    'Spam': 'Eggs'
}

url = r"http://httpbin.org/post"

params = {
    'name1': 'value1',
    'name2': 'value2'
}

resp = requests.post(url, data=params, headers=headers)

print(resp.text)

status = resp.status_code

content_length = resp.headers['content-length']

print("status : " + str(status))
print("content_length : " + str(content_length))


url = r"http://pypi.python.org/pypi?:action=login"

resp = requests.get(url, auth=('persadewh', '90871098Wh422'))
# print(resp.text)

print(resp.cookies)

# 利用requests将HTTP cookies从一个请求传递到另一个

resp2 = requests.get(url, cookies=resp.cookies)

# 上传文件

url = r"http://httpbin.org/post"
files = {'file': ('data.csv', open('data.csv', 'rb'))}

resp = requests.post(url, files=files)
# print(resp.text)

# 测试发出的请求
# url = r"http://httpbin.org/get?name=Dave&n=37"
# headers = {'User-agent': 'goaway/1.0'}
# resp = requests.get(url, headers=headers)
# r = resp.json
# print(r['args'])



