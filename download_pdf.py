import requests
import sys

url = sys.argv[1]
filename = sys.argv[2]

response = requests.get(url, stream = True)

with open(filename, 'wb') as f:
    f.write(response.content)