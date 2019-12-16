import requests

addr = 'http://10.144.71.51:5000'
test_url = addr + '/api/pi'

# prepare headers for http request
x = "car number.."
response = requests.post(test_url, data=x)
