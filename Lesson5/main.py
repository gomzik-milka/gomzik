import requests

response = requests.get('https://www.whenisthenextmcufilm.com/api')

if response.ok:
    as_json = response.json()
    print(as_json['title'])
    print(as_json['overview'])
    print(f"{as_json['title']} releases in {as_json['title']} days!")
else:
    print(f'{response.status_code=}')