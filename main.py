def printtitle():
    print("""
 ██░ ██  ▄▄▄       ▄████▄ ██▒   █▓ ██ ▄█▀ ██▀███  
▓██░ ██▒▒████▄    ▒██▀ ▀█▓██░   █▒ ██▄█▒ ▓██ ▒ ██▒
▒██▀▀██░▒██  ▀█▄  ▒▓█    ▄▓██  █▒░▓███▄░ ▓██ ░▄█ ▒
░▓█ ░██ ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▒██ █░░▓██ █▄ ▒██▀▀█▄  
░▓█▒░██▓ ▓█   ▓██▒▒ ▓███▀ ░ ▒▀█░  ▒██▒ █▄░██▓ ▒██▒
 ▒ ░░▒░▒ ▒▒   ▓▒█░░ ░▒ ▒  ░ ░ ▐░  ▒ ▒▒ ▓▒░ ▒▓ ░▒▓░
 ▒ ░▒░ ░  ▒   ▒▒ ░  ░  ▒    ░ ░░  ░ ░▒ ▒░  ░▒ ░ ▒░
 ░  ░░ ░  ░   ▒   ░           ░░  ░ ░░ ░   ░░   ░ 
 ░  ░  ░      ░  ░░ ░          ░  ░  ░      ░     
                  ░           ░                   
    """)

import requests
import time
import ctypes
from bs4 import BeautifulSoup
import os

ses = requests.session()

discordheaders = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36',
    'Content-Type': 'application/json'
}

whurl = "https://discord.com/api/webhooks/955261733696573500/-ieVo8SyeUfDz9xp5HVgyU8662k38-eu4y7GAxnYhkXoRCUNFkVRH8-U-ORYVRuRDj43"
gameid = "334907712"


def webhook(users, pc, fps, ping, jobid):
    json = {
        "content": "",
        "embeds": [
        {
            "title": "HC currently in game",
            "description": f"\n**Users:** {users}",
            "color": 16711680,
            "footer": {
                "text": f"Players: {pc}\nFPS: {fps}\nPing: {ping}\nGUID: {jobid}\nCredits: Dr.Wells#0001"
            }
        }
        ]
    }

    ses.post(
        whurl,
        headers=discordheaders, json=json)


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36',
    'Content-Type': 'application/json',
    'x-csrf-token': 'YUjq4hqujssr',
    'cookie': 'GuestData=UserID=-252296175; _gcl_au=1.1.1752639906.1643769504; RBXSource=rbx_acquisition_time=2/1/2022 8:38:24 PM&rbx_acquisition_referrer=https://www.roblox.com/&rbx_medium=Direct&rbx_source=www.roblox.com&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=1; __utma=200924205.1409187138.1643769508.1643769508.1643769508.1; __utmb=200924205.0.10.1643769508; __utmc=200924205; __utmz=200924205.1643769508.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); .ROBLOSECURITY=_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_C58B989CD615433B89D2B8E1BF81098AE501A273B54202358263D57ABF093CF846B80168B31CAA4483C1A4558B9E66F935E398F2D8D22B516FB8A033E44A91FF6A23E3B3F16A7A5F65440332F7ED7DFA839B70B9D17F1098F902B42C758172E1CB9431194EEBDF6CF032441E1C5D84A993414226A9D0DF6DF5249AF71BC27CAA71CD347ABC3FD9078E8689373FF5DE22DC46D88A27F9E2545D736F94FBDF06479C7601C6376331F1A25F7DDDEA18638EC030623FDA507F87922CD40B3EA968B0C20BADA35F44C719F9471AA379C1460E868E829B0238F84D39B59FE9ACE901445F22D4214FDD012415235787DCB1D31814E43A7B6A1B8536BFD36F2B8FA58BA19E615C487431AFF1AF92D8DF899FD138A0148A2CF20DE76100E8C33354D0AF2F38F011E3888A4F2C11218A3091045A46E66DCAAFF0D3EA14D30B6B6BA754D320170E92494B24B33CA182B0652794FE0E4512443B; .RBXID=_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIyOGVjMjFjMy0yYzQ4LTRjNDktYWY5MC04ZWJhMTVlYWNkNTgiLCJzdWIiOjY2NDQ3NjkzOH0.80oo-BiBl5ZY9-gHFt5c00OOtQQJrMlIA5o8i-sMHpA; RBXEventTrackerV2=CreateDate=2/1/2022 8:38:35 PM&rbxid=1819152826&browserid=125740267336; RBXSessionTracker=sessionid=22ca2a73-0356-401a-8f58-7c7c721c3877'
}

picture = ""


def getpicture(uid):
    png = ses.get("https://www.roblox.com/headshot-thumbnail/image?userId=" + uid + "&width=48&height=48&format=png",
        headers=discordheaders)
    global picture
    picture = png.url

userlist = {"Exphalo", "mikeyfuIs", "tfako", "YourCaesarSalad", "wagonman14", "TheePBHST", "OptimizedSwitch", "BloxChannel", "MrNepoliato", "DevEnqrypted", "lifealert_works", "ryxnly", "AlbertStransburg", "ConceptuaIist", "MOSABPRO20", "Chudgins", "XDMTuber", "ShadowsVhoq", "lnfinity_Stones", "8v0m", "dhfkgtdi", "Kryyos", "Ofline6543", "DjfrankensteinArmy", "FaceOfDeath0", "NinetyOneBravo", "YourNovaEclipse", "Aviaxton", "JoshhSaint", "Zampour", "Olivebucket", "StainlessOven", "Jay_Sav177", "samithebeast16", "themac217", "th3mario93", "Exlyen", "Early_Salads", "retyioplil", "DampHandsome_Prince", "iiArmaxdo", "LineWaves", "SonoUnNiente", "OfficerDecided", "DesiredSpecy", "AmericanDeadly", "Chills_President", "OurAdmiraI", "kindjelco", "TDchannel123", "Nilsvs_1", "wmpoliceofiser", "Polo_Zyxw", "RealLiohn", "AHD_grind4", "shellpro23", "withoutyou1314", "officer_jackson99", "dskilin", "Mr_ElonRusck", "scofield2122", "lying99", "atm_mac", "iiCIoudxies", "1RF4N12", "psychicmeows", "XxCool2020Xx", "HentanCoercion", "nnoahstar", "Plodeth", "Crabby_Nico", "wolfgamer234820", "Jakob_Izquierdo", "RobloxPhil2009", "unspeakable_gaming57", "youradopted54332", "xXElijahFamXx", "GENERALKINOBI1", "Flashhadi1", "TheWildFounder", "Testaccount112576", "taiajfoiahfjkashfkj", "Planetaries", "PSC4445", "asimo303413", "YouFoundKing", "gamingwithjay22345"}
useridlist = []

for user in userlist:
    r = ses.get(f"https://api.roblox.com/users/get-by-username?username={str(user)}", headers=headers)
    useridlist.append(f"{r.json()['Id']}:{str(user)}")

while True:
        peopleig = ""
        listofusers = ses.get(
            f"https://www.roblox.com/games/getgameinstancesjson?placeId={gameid}&startIndex=0",
            headers=headers)
        guid = "N/A"
        fps = "N/A"
        ping = "N/A"
        playercount = {"N", "A"}
        if listofusers.json()['Collection']:
            guid = listofusers.json()['Collection'][0]['Guid']
            fps = round(listofusers.json()['Collection'][0]['Fps'])
            ping = listofusers.json()['Collection'][0]['Ping']
            playercount = listofusers.json()['Collection'][0]['PlayersCapacity']
            playercount = playercount.split()
            os.system("cls")
            printtitle()
            print(f"Players: {playercount[0]}/{playercount[2]}\nServer FPS: {fps}\nPing: {ping}\nServer Instance ID: {guid}")
            listtxt = f'{listofusers.text}'

            for text in useridlist:
                newtext = text.split(":")
                getpicture(newtext[0])
                picurl = picture
                if listtxt.find(f'{picurl}') >= 1:
                    peopleig = f"{str(peopleig)}\n{str(newtext[1])}"

        if not peopleig == "":
            webhook(peopleig, f'{playercount[0]}/{playercount[2]}', fps, ping, guid)
            print(f"\nHC:{peopleig}")

        time.sleep(300)