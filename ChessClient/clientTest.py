import requests
import json

url = 'http://localhost:5000/predict'
headers = {'content-type': 'application/json'}
payload = [
    {
        'ilkHamle': 'b3',
        'ikinciHamle': 'h6',
        'ucuncuHamle': 'f3',
        'dorduncuHamle': 'Bh7',
        'besinciHamle': 'e4',
        'altinciHamle': 'f5',
        'yedinciHamle': 'e5',
        'sekizinciHamle': 'f4',
        'dokuzuncuHamle': 'Qc3',
        'onuncuHamle': 'Nc6',
    },
]
response = requests.post(url, data=json.dumps(payload), headers=headers)

print(response.text)
