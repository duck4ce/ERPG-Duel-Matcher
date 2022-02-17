import discord
import os
import player


client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$test'):
        player_id = message.author.id
        p1 = player.Player(player_id)
        await message.channel.send('your id is: ' + str(p1.playerid))

if __name__ == "__main__":
  client.run(os.environ['TOKEN'])
