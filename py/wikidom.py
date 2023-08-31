import webbrowser
import json
import urllib.request, json 
from pynput.mouse import Listener

url = "https://fr.wikipedia.org/api/rest_v1/page/random/summary"

with urllib.request.urlopen(url) as url2:
    data = json.load(url2)
    print('Voici la page que vous devez trouver : ' + data['title'] + " : " + data['extract'])

webbrowser.open("https://fr.wikipedia.org/wiki/Sp%C3%A9cial:Page_au_hasard")

click_count = 0 
def on_click(x, y, button, pressed):
    global click_count
    if button == button.left and pressed:
        click_count +=1
        print(f"Nombres de clics gauches ! {click_count}")
    elif button == button.right and pressed:
        print(f"Tu as réussi en {click_count} coups")
        return False

with Listener(on_click=on_click) as listener:
    listener.join()
