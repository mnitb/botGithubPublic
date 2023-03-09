from discord.message import Message
# -*- coding: utf8 -*-
import urllib.request
import PIL
import random
import nest_asyncio
import shutil
import time
nest_asyncio.apply()
# bot.py
GOOGLE_IMAGE = \
    'https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&'
import discord
from discord.ext import commands
from bs4 import *
import requests
import os
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
  
TOKEN=''

  
client = discord.Client()
count=0
check=False
check1=True
@client.event
async def on_message(message):
  if ("_lnd" in message.content.lower()):
            msg= message.content.lower()
            print(msg)
            if "-log" in msg:
              lnlog=True
            else:
              lnlog=False
            msg = msg.replace("-log","")
            print(msg)
            lninfo = msg.split()
            lninfo.pop(0)
            lnname=  lninfo[0]
            lnname= lnname+"_"+str(message.author)[0:-5]+'.txt'
            lnlink = lninfo[1]
            print(lnlink)
            print(lnname,lnlink)
            if ("docln" in lnlink) or ("shinigamilnteam.com" in lnlink):
                  import ssl
                  ssl._create_default_https_context = ssl._create_unverified_context
                  text = ''
                  lninfo.pop(0)
                  lninfo.pop(0)
                  lnlinkslist=[]
                  headers = {'User-Agent': user_agent }
                  lnrequest = urllib.request.Request(
                    lnlink, None, headers)
                  response = urllib.request.urlopen(lnrequest)
                  data = response.read() 
                  soup = BeautifulSoup(data, features="html.parser")

                  # kill all script and style elements"""
                  for script in soup(["script", "style"]):
                      script.extract()  

                  if ("docln.net" in lnlink):
                    for link in soup.find_all('a'):
                        tg = link.get('href')
                        tg=  str(tg)
                        if all(item in tg for item in lninfo):
                          tg = 'https://docln.net' + tg
                          if "docln.nethttps://docln.net" in tg:
                            await message.channel.send("errors")
                            print("error")
                            check1=False
                            break
                          lnlinkslist.append(tg)
                  else:
                    for link in soup.find_all('a'):
                        tg = link.get('href')
                        tg=  str(tg)
                        if all(item in tg for item in lninfo):
                          tg = 'https://shinigamilnteam.com' + tg
                          lnlinkslist.append(tg)
                  if check1==True:
                    with open(lnname, 'w', encoding='utf-8') as f:
                      for t in lnlinkslist:
                        print(lnlinkslist.index(t)+1)
                        if lnlog:
                          await message.channel.send(str(lnlinkslist.index(t)+1)+"/"+str(len(lnlinkslist))+"   "+t[8:len(t)])
                        headers = {'User-Agent': user_agent, }
                        request = urllib.request.Request(
                                t, None, headers)
                        lncheck=True
                        while lncheck==True:
                          try:
                            response = urllib.request.urlopen(request)
                            lncheck=False
                          except:
                            time.sleep(50)
                        lndata = response.read()  
                        lnsoup = BeautifulSoup(lndata, features="html.parser") 
                        # get text
                        #text = soup.find_all('p')[1].get_text()
                        n = len(lnsoup.find_all('p'))
                        for i in range(n):
                            text = text + '\n' + lnsoup.find_all('p')[i].get_text()
                        text = text + '\n ==================================================== \n'
                        f.write(text)
                      f.close()
                      CHUNK_SIZE = 6000000
                      file_number = 1
                      with open(lnname) as f:
                          chunk = f.read(CHUNK_SIZE)
                          while chunk:
                              with open('part_' + str(file_number)+".txt", 'w') as chunk_file:
                                  chunk_file.write(chunk)
                              file_number += 1
                              chunk = f.read(CHUNK_SIZE) 
                              await message.channel.send(file=discord.File('part_' + str(file_number-1)+".txt"))
                              os.remove('part_' + str(file_number-1)+".txt")
            else:
                await message.channel.send("fuck_you")
            #os.remove(lnname)
            #os.remove(lnname[0:-4]+".zip")

client.run(TOKEN)

