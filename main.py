import discord
import os
import player
import queue
import helperFunctions as hf

client = discord.Client()
queue_list = []

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  for g in client.guilds:
    queue_list.append((g, queue.Queue()))
    print(g)
  

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$test'):
        player_id = message.author.id
        p1 = player.Player(player_id)
        await message.channel.send('your id is: ' + str(p1.playerid))

    if message.content.startswith('$enqueue'):
        player_id = message.author.id
        p1 = player.Player(player_id)
        local_queue = hf.getLocalQueue(queue_list,message.guild)
        local_queue.put(p1)
        await message.channel.send('player ' + str(p1.playerid) + ' added to queue')
        message_string = 'all players in queue\n'
        for x in list(local_queue.queue):
          message_string = message_string + '<@' + str(x.playerid) + '>\n'
        await message.channel.send(message_string)


  
if __name__ == "__main__":
  client.run(os.environ['TOKEN'])

if 
