from urllib import request, parse


url = r"http://httpbin.org/post"

params = {
    'name1': 'value1',
    'name2': 'value2'
}

querystring = parse.urlencode(params)

u = request.urlopen(url, querystring.encode('ascii'))

resp = u.read()

print(resp)
