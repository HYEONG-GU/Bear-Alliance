import discord
import asyncio
import os

client = discord.Client()

@client.event
async def on_ready():
    print("Bear-Alliance")
    print("봇이 켜졌습니다.")
    game = discord.Game("Manager_Bot 개발중")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith("매니저 명함"):
        embed = discord.Embed(colour=0xff0000)
        embed.add_field(name='[Alliance 명함]', value='안녕하세요 Bear입니다. 저희 Alliance에 대해 알려드리도록하겟습니다.\n\u200b현재는 공부중입니다. 하지만 추후 계획은 많은 스크립트들을 판매를 할것입니다. \n\u200b\n Made by Bear#1901', inline=True)
        await message.channel.send(embed=embed)
    if message.content.startswith("개발현황"):
        embed = discord.Embed(colour=0xeeff00)
        embed.add_field(name='[개발현황]', value='현재 LUA언어 공부중에 있습니다.\n\u200b\n Made by Bear#1901', inline=True)
        await message.channel.send(embed=embed)

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
