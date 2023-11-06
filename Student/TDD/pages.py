from requests import get


response = get('https://shrinking-world.com')
print('SW: ', response)
print(response.text)