import discord
import youtube_dl as ytb_dl
#id 502858151612383232
client = discord.Client()
token = open("token.txt", 'r').read()
# pip install -U git+https://github.com/Rapptz/discord.py@rewrite#egg=discord.py[voice]

@client.event
async def on_ready():
    print("Logged In.")

@client.event
async def on_message(message):
    msg = message.content.lower()
    if msg.startswith(">"):
        if msg[1] == "t":
            await message.channel.send(f"Working")
        if msg == ">quit":
            print("Logged out")
            await client.close()
client.run(token)