import json
import requests

resp = requests.get('http://samples.openweathermap.org/data/2.5/weather?zip=44143,us&appid=b1b15e88fa797225412429c1c50c122a1')

test = json.dumps(json.loads(resp.content), indent=4)

print("Test: " + test)