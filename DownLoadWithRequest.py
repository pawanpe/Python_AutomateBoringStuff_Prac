import requests

# Requests downloads the page.
res = requests.get('https://designpsych.in')
if(res.status_code == 200):
    print("SUCCESS")
   # print(res.text[:400]) #first 400 chars
    # requests.readthedocs.org
    print(res.text)

res.raise_for_status()