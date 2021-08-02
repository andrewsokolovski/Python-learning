from urllib.request import urlopen
html = urlopen ('https://olrnet.comfone.com/')
print(html.read())