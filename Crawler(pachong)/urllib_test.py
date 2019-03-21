
import urllib.request
import urllib.parse
import urllib.request

response = urllib.request.urlopen("https://www.baidu.com")
#print('get请求：',response.read().decode('utf-8'))

data = bytes(urllib.parse.urlencode({'word':'hello'}),encoding='utf8')
response = urllib.request.urlopen("http://httpbin.org/post",data=data)
print(response.read())




