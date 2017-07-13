import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])  # [mapit.py bxb 08392] --> argv
else:
    # Get from clipboard
    address = pyperclip.paste()

webbrowser.open('https://maps.google.com/maps/place/' + address)
webbrowser.open_new_tab('https://www.openstreetmap.org/search?query=' + address)