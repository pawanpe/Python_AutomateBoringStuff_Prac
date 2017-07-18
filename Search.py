import sys, bs4, requests,webbrowser

if len(sys.argv) < 2:
    print('Need search terms. Exiting the program ....')
    wait = input("PRESS ENTER TO CONTINUE.")
else:
    print("Searching...")
    address = ' '.join(sys.argv[1:])
    res = requests.get('https://google.com/search?q=' + address)
    print(res.text)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text,'html.parser')

    linkElems = soup.select('.r a')

    numOpen = min(5, len(linkElems))

    for i in range(numOpen):
        href = linkElems[i].get('href')
        webbrowser.open('http://google.com' + href)

#wait = input("PRESS ENTER TO CONTINUE.")