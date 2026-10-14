#got indentation issue in this 
#request module allows you to interact with API
import requests
 
url = "https://fake-json-api.mock.beeceptor.com"
response = requests.get(url=url)
print(response.json())