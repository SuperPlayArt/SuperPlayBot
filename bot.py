import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix = '!s ')
client.remove_command("help")


@client.event
async def on_ready():
    print('Bot is ready')
    


@client.command(aliases=['invite'])
async def pub(ctx):
    await ctx.message.reply('Salut a toi jeune entrepreneur ! \nTu n\'arrives pas à trouver un serveur intéressant et drôle ? Eh bien ce serveur est fait pour toi ! Alors tu veux continuer à faire pitié en cherchant LE serveur qu\'il te faut, ou commencé très vite à rigoler avec moi . Moi je pense que la question elle est vite répondue. Alors à tous de suite.\nBisou. \nhttps://discord.gg/2puWE2ZWgd')

@client.command(aliases=['golog'])
async def alertelog(ctx):
    await ctx.send('https://media.discordapp.net/attachments/797593407513559080/830180368853893180/exit.png?width=1440&height=529')





@client.command()
async def info(ctx):
    embed=discord.Embed(title="SuperPlayBot - Les infos du bot !", description="Voici les infos du bot !", color=0x9900ff)
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/797593407513559080/830098585772884028/Logo_SPA_v2.png?width=1240&height=676")
    embed.add_field(name="Création du bot :", value="09/04/21", inline=False)
    embed.add_field(name="Créateur : ", value="SPA (SuperPlayArt)", inline=True)
    embed.add_field(name="Langages :", value="Python", inline=True)
    embed.add_field(name="Préfix :", value="!s", inline=True)
    embed.set_footer(text="2021 - SPA")
    await ctx.message.reply(embed=embed)

@client.command(aliases=['pp'])
async def avatar(ctx, *, member: discord.Member=None): # set the member object to None
    if not member:
        member = ctx.message.author # set member as the author
    userAvatar = member.avatar_url
    embed=discord.Embed(title=member, url="https://fr.wikipedia.org/wiki/Avatar_(film,_2009)", description="C'est son avatar (Pas le film mdr)", color=0x9900ff)
    embed.set_image(url=userAvatar)
    await ctx.message.reply(embed=embed)


@client.command(aliases=['aide'])
async def help(ctx):
    embed=discord.Embed(title="SuperPlayBot - Les commandes", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", description="Voici les commandes du bot !", color=0x9900ff)
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/797593407513559080/830098585772884028/Logo_SPA_v2.png?width=1240&height=676")
    embed.add_field(name="!s help ", value="Actuellement utilisé.", inline=False)
    embed.add_field(name="!s avatar", value="Pour avoir ton avatar ou celui des autres.", inline=True)
    embed.add_field(name="!s serv", value="Pioche au hasard un serveur dans une liste.", inline=True)
    embed.add_field(name="!s alertelog", value="Quand une blague nulle est faites utilisé cette commande.", inline=True)
    embed.add_field(name="!s say", value="Parler en tant que SPB. (Ne pas en abuser, sinon c'est lourd)", inline=True)
    embed.set_footer(text="2021 - SPA")
    await ctx.message.reply(embed=embed)


@client.command()
async def serv(ctx):
  responses = ['Serveur LLANCOSS\'WORLD : https://discord.gg/qVYeCdZqMP', 'Serveur Bourgade Slawkienne : https://discord.gg/P4J3gzRSrp', 'Serveur DBKILLER x Guigui : https://discord.gg/7mPYHjRkDc', 'Serveur Chromavirus : https://discord.gg/VGCCaZq']
  responses = random.choice(responses)
  embed=discord.Embed(title="SPA te conseil ce serveur !", description=responses, color=0x9900ff)
  embed.set_thumbnail(url="https://media.discordapp.net/attachments/797593407513559080/830098585772884028/Logo_SPA_v2.png?width=1240&height=676")
  await ctx.message.reply(embed=embed)

# Startup Information
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('!s help'))

    print('Connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))

@client.command(aliases=['dire'])
async def say(ctx, *texte, member: discord.Member=None):
    member = ctx.message.author
    embed=discord.Embed(title=" ".join(texte), color=0x9900ff)
    embed.set_footer(text=member)
    await ctx.message.delete()
    await ctx.send(embed=embed)


@client.command()
async def vaporwave(ctx, *text):
    VaporChar = "ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ"
    VaporText = []
    for word in text:
        for char in word:
            if char.isalpha():
                index = ord(char) - ord("a")
                transformed = VaporChar [index]
                VaporText.append(transformed)
            else:
                VaporText.append(char)
            VaporText.append(" ")
    await ctx.send("".join(VaporText))



client.run('TOKEN HERE')
