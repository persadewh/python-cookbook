from urllib import request, parse

headers = {
    'User-agent': 'none/ofyourbusiness',
    'Spam': 'Eggs'
}

url = r"http://httpbin.org/post"

params = {
    'name1': 'value1',
    'name2': 'value2'
}

querystring = parse.urlencode(params)

req = request.Request(url, querystring.encode('ascii'), headers=headers)

u = request.urlopen(req)

resp = u.read()

print(resp)
