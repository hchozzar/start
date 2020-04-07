import discord
import os

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("숨 쉬기")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content.startswith("/형준"):
        await message.channel.send("https://www.op.gg/summoner/userName=poro%EC%99%95")
    if message.content.startswith("poro왕"):
        await message.channel.send("https://www.op.gg/summoner/userName=poro%EC%99%95")
    if message.content.startswith("/동현"):
        await message.channel.send("https://www.op.gg/summoner/userName=%EB%90%B4%EA%B5%AC%EB%8A%90%EC%8A%A4")
    if message.content.startswith("됴구느스"):
        await message.channel.send("https://www.op.gg/summoner/userName=%EB%90%B4%EA%B5%AC%EB%8A%90%EC%8A%A4")
    if message.content.startswith("/형철"):
        await message.channel.send("위대한 신의 이름 https://www.op.gg/summoner/userName=Hide%20on%20bush")
    if message.content.startswith("huh7"):
        await message.channel.send("https://www.op.gg/summoner/userName=huh7")
    if message.content.startswith("/기법"):
        await message.channel.send("https://www.op.gg/summoner/userName=%EC%A0%95%EA%B8%80%EC%9E%A5%EC%9D%B8cptcpt")
    if message.content.startswith("정글장인cptcpt"):
        await message.channel.send("https://www.op.gg/summoner/userName=%EC%A0%95%EA%B8%80%EC%9E%A5%EC%9D%B8cptcpt")
    if message.content.startswith("/시현"):
        await message.channel.send("https://www.op.gg/summoner/userName=%EB%AD%90%EB%A7%8C%ED%95%98%EB%A9%B4%EB%AF%B8%EB%93%9C%EC%B0%A8%EC%9D%B4")
    if message.content.startswith("뭐만하면미드차이"):
        await message.channel.send("https://www.op.gg/summoner/userName=%EB%AD%90%EB%A7%8C%ED%95%98%EB%A9%B4%EB%AF%B8%EB%93%9C%EC%B0%A8%EC%9D%B4")
    if message.content.startswith("/범석"):
        await message.channel.send("https://www.op.gg/summoner/userName=%EC%98%A4%EB%8A%98%EC%95%84%EC%B9%A8%EC%8B%9C%EC%9B%90%ED%95%98%EB%84%A4")
    if message.content.startswith("오늘아침시원하네"):
        await message.channel.send("https://www.op.gg/summoner/userName=%EC%98%A4%EB%8A%98%EC%95%84%EC%B9%A8%EC%8B%9C%EC%9B%90%ED%95%98%EB%84%A4")
    if message.content.startswith("/성진"):
        await message.channel.send("https://www.op.gg/summoner/userName=%EC%95%84%EC%A7%84%EC%A7%84")
    if message.content.startswith("아진진"):
        await message.channel.send("https://www.op.gg/summoner/userName=%EC%95%84%EC%A7%84%EC%A7%84")
    if message.content.startswith("닥쳐"):
        await message.channel.send("응 아니야")
    if message.content.startswith("ㅆㅂ"):
        await message.channel.send("ㅄ")
    if message.content.startswith("/일웅"):
        await message.channel.send("https://www.op.gg/summoner/userName=%ED%82%AC%EB%94%B8%EC%9B%90%EC%B1%94")
    if message.content.startswith("킬딸원챔"):
        await message.channel.send("https://www.op.gg/summoner/userName=%ED%82%AC%EB%94%B8%EC%9B%90%EC%B1%94")
    if message.content.startswith("?"):
        await message.channel.send("?")
    if message.content.startswith("/ㅈㅈ"):
        import random
        menu = ['ㅅㅍㅊㅇ', 'ㅇㄷㅊㅇ', 'ㅁㄷㅊㅇ', 'ㅌㅊㅇ', 'ㅈㄱㅊㅇ']
        dinner = random.choice(menu)
        await message.channel.send(str(dinner))







access_token - os.environ["BOT_TOKEN"]
client.run(access_token)

















