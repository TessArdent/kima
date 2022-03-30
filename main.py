import discord
import os

TOKEN = os.environ.get('TOKEN')

class Kima(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

kima = Kima()
kima.run(TOKEN)
