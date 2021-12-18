import requests
url = "https://cat-fact.herokuapp.com/facts"
headers = {
        'Content-Type': "application/json",
        'Authorization': "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbkBleGFtcGxlLmNvbSIsImV4cCI6MTY0MjMyMTExOX0.ww2t8QeCXL-LSfiw5EOWqYrKDySVLSCf0w0znGRD5s8"
        }

response = requests.request("GET", url)

print(response.text)