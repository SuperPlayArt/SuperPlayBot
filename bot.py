import discord
import random
from discord import member
from discord import channel
from discord.ext import commands

#from PIL import Image
#from io import BytesIO
#from PIL import ImageFont
#from PIL import ImageDraw
#from PIL import ImageOps
import asyncio
from discord.ext.commands.errors import MissingRequiredArgument

from discord.flags import SystemChannelFlags
from discord.ext.commands import has_permissions, MissingPermissions

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix = '!s ', intents=intents)
client.remove_command("help")



@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f'!𝚜 𝚑𝚎𝚕𝚙'))
    print('Connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))
    channel = client.get_channel(830072847929835571)
    embed=discord.Embed(title="SuperPlayBot", description="Je suis en ligne !", color=0x9900ff)
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/797593407513559080/830098585772884028/Logo_SPA_v2.png?width=1240&height=676")
    embed.set_footer(text="2021 - SPA ⭐")
    await channel.send(embed=embed)
    
@client.event 
async def on_member_join(member):
    channel = client.get_channel(778991515468955668)
    embed=discord.Embed(title=f"Bienvenue **{member.name}** !", color=0x9900ff)
    embed.set_image(url='https://media.discordapp.net/attachments/797593407513559080/845581688990203954/bienvenue.png')
    embed.set_footer(text="2021 - SPA ⭐")
    await channel.send(embed=embed)
    #dm = await member.create_dm()
    #await dm.send(f'Bienvenue **{member.name}** sur le serveur !\nJe t\'invite à lire les règles et à les acceptés en appuyant sur :white_check_mark: !')
    log = client.get_channel(827879112185610311)
    await log.send(f'{member.name} vient d\'arrivé !')

@client.event 
async def on_member_remove(member):
    channel = client.get_channel(778991591997177876)
    embed=discord.Embed(title=f"A bientôt **{member.name}** !", color=0x9900ff)
    embed.set_image(url='https://media.discordapp.net/attachments/797593407513559080/845581682895093760/au_revoir.png')
    embed.set_footer(text="2021 - SPA ⭐")
    await channel.send(embed=embed)
    log = client.get_channel(827879112185610311)
    await log.send(f'{member.name} vient de partir !')

@client.command(aliases=['invite'])
async def pub(ctx):
    await ctx.message.reply('Salut a toi jeune entrepreneur ! \nTu n\'arrives pas à trouver un serveur intéressant et drôle ? Eh bien ce serveur est fait pour toi ! Alors tu veux continuer à faire pitié en cherchant LE serveur qu\'il te faut, ou commencé très vite à rigoler avec moi . Moi je pense que la question elle est vite répondue. Alors à tous de suite.\nBisou. \nhttps://discord.gg/2puWE2ZWgd')

@client.command(aliases=['golog'])
async def alertelog(ctx):
    await ctx.send('https://media.discordapp.net/attachments/797593407513559080/830180368853893180/exit.png?width=1440&height=529')


@client.command(aliases=['spbinvite'])
async def invitebot(ctx):
    #embed=discord.Embed(title="Clique ici pour inviter le bot !", url="https://discord.com/api/oauth2/authorize?client_id=820733417640951808&permissions=2113793271&scope=bot", description="Ce bot est encore en bêta, donc ne lui en demandez pas trop : )", color=0x9900ff)
    #embed.set_thumbnail(url="https://media.discordapp.net/attachments/797593407513559080/830098585772884028/Logo_SPA_v2.png?width=1240&height=676")
    #embed.set_footer(text="2021 - SPA ⭐")
    #await ctx.send(embed=embed)
    embed=discord.Embed(title="Cette commande est désactivée temporairement.", color=0x9900ff)
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/797593407513559080/830098585772884028/Logo_SPA_v2.png?width=1240&height=676")
    embed.set_footer(text="2021 - SPA ⭐")
    await ctx.send(embed=embed)

@client.command(aliases=['don'])
async def spa(ctx):
    embed=discord.Embed(title="Cliquez ici pour faire un don à la SPA ", url="https://soutenir.la-spa.fr/b/mon-don", description="(la vrai, pas à SuperPlayArt)", color=0x9900ff)
    embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/fr/thumb/0/00/Logo_de_la_SPA_%28France%29.png/800px-Logo_de_la_SPA_%28France%29.png")
    embed.set_footer(text="2021 - SPA ⭐")
    await ctx.message.reply(embed=embed)

@client.command()
async def info(ctx):
    embed=discord.Embed(title="SuperPlayBot - Les infos du bot !", description="Voici les infos du bot !", color=0x9900ff)
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/797593407513559080/830098585772884028/Logo_SPA_v2.png?width=1240&height=676")
    embed.add_field(name="Création du bot :", value="09/04/21", inline=False)
    embed.add_field(name="Créateur : ", value="SPA (SuperPlayArt)", inline=True)
    embed.add_field(name="Langages :", value="Python", inline=True)
    embed.add_field(name="Préfix :", value="!s", inline=True)
    embed.add_field(name="Nombre de serveur :", value=len(client.guilds), inline=True)
    embed.add_field(name="GitHub :", value="[Cliquez ici](https://github.com/SuperPlayArt/SuperPlayBot)", inline=True)
    embed.add_field(name="Email :", value="superplayart@gmail.com", inline=True)
    embed.set_footer(text="2021 - SPA ⭐")
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
    embed=discord.Embed(title="SuperPlayBot - Les commandes", description="Voici les commandes du bot !", color=0x9900ff)
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/797593407513559080/830098585772884028/Logo_SPA_v2.png?width=1240&height=676")
    embed.add_field(name="!s help ", value="Actuellement utilisé.", inline=True)
    embed.add_field(name="!s info ", value="Permet d\'avoir les infos sur le bot.", inline=True)
    embed.add_field(name="!s invitebot ", value="Permet d\'invité le bot sur votre serveur.", inline=True)
    embed.add_field(name="!s invite ", value="Permet d'avoir le lien du serveur.", inline=True)
    embed.add_field(name="!s avatar", value="Pour avoir ton avatar ou celui des autres.", inline=True)
    embed.add_field(name="!s serv", value="Pioche au hasard un serveur dans une liste.", inline=True)
    embed.add_field(name="!s userinfo", value="Permet d\'avoir les information d'un utilisateur.", inline=True)
    embed.add_field(name="!s alertelog", value="Quand une blague nulle est faites utilisé cette commande.", inline=True)
    embed.add_field(name="!s say", value="Parler en tant que SPB. (Ne pas en abuser, sinon c'est lourd)", inline=True)
    embed.add_field(name="!s spa", value="Aidez la SPA.", inline=True)
    embed.add_field(name="Plus d'information ici :", value="[GitHub](https://github.com/SuperPlayArt/SuperPlayBot)", inline=True)
    embed.set_footer(text="2021 - SPA ⭐")
    await ctx.message.reply(embed=embed)


@client.command()
async def serv(ctx):
  responses = ['Serveur LLANCOSS\'WORLD : https://discord.gg/qVYeCdZqMP', 'Serveur Bourgade Slawkienne : https://discord.gg/P4J3gzRSrp', 'Serveur DBKILLER x Guigui : https://discord.gg/7mPYHjRkDc', 'Serveur Chromavirus : https://discord.gg/VGCCaZq']
  responses = random.choice(responses)
  embed=discord.Embed(title="SPA te conseil ce serveur !", description=responses, color=0x9900ff)
  embed.set_thumbnail(url="https://media.discordapp.net/attachments/797593407513559080/830098585772884028/Logo_SPA_v2.png?width=1240&height=676")
  embed.set_footer(text="2021 - SPA ⭐")
  await ctx.message.reply(embed=embed)

@client.command(aliases=['dire'])
async def say(ctx, *texte, member: discord.Member=None):
    member = ctx.message.author.name
    channel = client.get_channel(827879112185610311)
    embed=discord.Embed(title=" ".join(texte), color=0x9900ff)
    embed.set_author(name="Anonymous", icon_url="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a6/Anonymous_emblem.svg/1024px-Anonymous_emblem.svg.png")
    embed.set_footer(text='2021 - SPA ⭐')
    await ctx.message.delete()
    await ctx.send(embed=embed)
    await channel.send(f'{member} à utilisé !s say')

@client.command()
async def userinfo(ctx, *, member: discord.Member=None):
    if not member:
        member = ctx.message.author
    username = member.name
    userAvatar = member.avatar_url
    usercreation = member.created_at.strftime("%m/%d/%Y à %H:%M")
    rolelist = [r.mention for r in member.roles if r != ctx.guild.default_role]
    userjoin = member.joined_at.strftime("%m/%d/%Y à %H:%M")
    embed=discord.Embed(title=f'**Voici les infos de {username} !**', color=0x9900ff)
    embed.set_thumbnail(url=member.avatar_url)
    embed.add_field(name="Nom d'utilisateur :", value=member, inline=False)
    embed.add_field(name="Date de création :", value=usercreation, inline=False)
    embed.add_field(name="Date d'arrivée :", value=userjoin, inline=False)
    embed.add_field(name="Rôle(s) :", value=", ".join(rolelist), inline=False)
    embed.set_footer(text="2021 - SPA ⭐")
    await ctx.message.reply(embed=embed)

#@client.command()
#async def dm(ctx, member: discord.Member, *, content):
    channel = await member.create_dm()
    await channel.send(content)

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Arf, je ne connais pas cette commande")
    if isinstance(error, MissingRequiredArgument):
        await ctx.send("Il manque un argument :/")
    elif isinstance(error, MissingPermissions):
        await ctx.send("Tu n'a pas la permission d'utilisé cette commande...")

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, nombre: int):
    messages = await ctx.channel.history(limit=nombre +1).flatten()
    for message in messages:
        await message.delete()



client.run('TOKEN')
