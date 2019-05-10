import requests

# res=requests.get('https://xkcd.com/353/')
# print(res.text)

# rimg=requests.get('https://imgs.xkcd.com/comics/python.png')

# with open('comic.png','wb') as f:
#     f.write(rimg.content)
#
# print(rimg.status_code)
# print(rimg.headers)
# payload={'page':2,'count':25}
# r=requests.get('https://httpbin.org/get',params=payload)
# print(r.text)

# payload={'username':'caihong','password':'2125'}
# r=requests.post('https://httpbin.org/post',data=payload)
# rDict = r.json()
#
# print(rDict['form'])

# r=requests.get('https://httpbin.org/basic-auth/caihong/testing',auth=('caihong','testing'))
# # # print(r.text)
# # # print(r)
# # #
# # # r=requests.get('https://httpbin.org/basic-auth/caihong/testing',auth=('caihong','Testing'))
# # # print(r.text)
# # # print(r)


r=requests.get('https://httpbin.org/delay/3',timeout=4)
print(r)

r=requests.get('https://httpbin.org/delay/3',timeout=1)
print(r)