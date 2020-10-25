import requests

payload = {
    '__anti-forgery-token' : '',
    'email' : '',
    'password' : ''
}

response = requests.post('url',data=payload)