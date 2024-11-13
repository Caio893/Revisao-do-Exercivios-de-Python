import requests
import urllib
import urllib.request
def pudim():
    try:
        tentar = requests.get('https://www.pudim.com.br/', timeout=5)
        return True
    except requests.ConnectionError:
        return False

if pudim():
    print('O site está acessivel !!')
else:
    print('O Site não está acessivel !!')

def pudim2():
    try:
        site = urllib.request.urlopen('https://www.pudim.com.br')
    except urllib.request.URLError:
        print('Deu erro')
    else:
        print('Deu bom')
        print(site.read())

pudim2()
