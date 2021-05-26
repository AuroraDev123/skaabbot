import discord
from discord.ext import commands
from discord.ext.commands import Context

client = commands.Bot(command_prefix="!")

@client.event
async def on_message(message):
    if message.content == "hello":
        general_channel = client.get_channel(810697372971696131)
        await general_channel.send("Less goo")

client.run("ODQ1NDkxODE4MjQ5NTg0Njkw.YKhvnQ.F7wD0iPJcOLleoppAGLS2Mjk7l0")
