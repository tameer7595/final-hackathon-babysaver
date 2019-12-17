import requests

addr = 'http://10.144.71.51:5000'
test_url = addr + '/api/web_page'

# prepare headers for http request
x = "24-057-12,0585453364"
response = requests.post(test_url, data=x)
