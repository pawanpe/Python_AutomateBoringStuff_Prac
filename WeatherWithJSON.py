import json,sys,requests

def getWeather():
    # Compute location
    if len(sys.argv) < 3:
        print("Usage: weather location countrycode")
        sys.exit()
    location = ' '.join(sys.argv[1])
    print(sys.argv[1])
    print(sys.argv[2])
    countrycode = ' '.join(sys.argv[2])

    # Download JSON
    url = 'api.openweathermap.org/data/2.5/forecast?q=%s,%s' % location % countrycode
    res = requests.get(url)
    res.raise_for_status()

    # Load JSON
    weatherData = json.loads(res.text)
    w = weatherData['list']
    print('Current weather in %s:' % location)
    print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
    print()
    print('Tomorrow:')
    print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
    print()
    print('Day after tomorrow:')
    print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
    wait = input("PRESS ...")

getWeather()
