import discord

token = 'TOKEN'

client = discord.Client()

@client.event
async def on_message(message):
    if len(message.mentions) > 9:
	if mesaage.author.guild_permissions.manage_messages:
	    return
			
        try:
            await message.delete()
	except:
            pass
	await message.author.ban(reason='멘션테러')
        await message.channel.send(f'{message.author} 차단됨')
		
client.run(token)
