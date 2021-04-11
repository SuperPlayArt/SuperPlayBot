import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix = '!s ')
client.remove_command("help")


@client.event
async def on_ready():
    print('Bot is ready')
    bot. load_extension('cogs.leveling')


@client.command(aliases=['invite'])
async def pub(ctx):
    await ctx.message.reply('Salut a toi jeune entrepreneur ! \nTu n\'arrives pas à trouver un serveur intéressant et drôle ? Eh bien ce serveur est fait pour toi ! Alors tu veux continuer à faire pitié en cherchant LE serveur qu\'il te faut, ou commencé très vite à rigoler avec moi . Moi je pense que la question elle est vite répondue. Alors à tous de suite.\nBisou. \nhttps://discord.gg/2puWE2ZWgd')

@client.command(aliases=['golog'])
async def alertelog(ctx):
    await ctx.send('https://media.discordapp.net/attachments/797593407513559080/830180368853893180/exit.png?width=1440&height=529')


@client.command(aliases=['spbinvite'])
async def invitebot(ctx):
    embed=discord.Embed(title="Clique ici pour invité le bot !", url="https://discord.com/api/oauth2/authorize?client_id=820733417640951808&permissions=2113793271&scope=bot", description="Ce bot est encore en bêta, donc ne lui en demander pas trop : )", color=0x9900ff)
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/797593407513559080/830098585772884028/Logo_SPA_v2.png?width=1240&height=676")
    embed.set_footer(text="2021 - SPA")
    await ctx.send(embed=embed)

@client.command(aliases=['don'])
async def spa(ctx):
    embed=discord.Embed(title="Cliquez ici pour faire un don à la SPA ", url="https://soutenir.la-spa.fr/b/mon-don", description="(la vrai, pas à SuperPlayArt)", color=0x9900ff)
    embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/fr/thumb/0/00/Logo_de_la_SPA_%28France%29.png/800px-Logo_de_la_SPA_%28France%29.png")
    embed.set_footer(text="2021 - SPA")
    await ctx.message.reply(embed=embed)

@client.command()
async def info(ctx):
    embed=discord.Embed(title="SuperPlayBot - Les infos du bot !", description="Voici les infos du bot !", color=0x9900ff)
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/797593407513559080/830098585772884028/Logo_SPA_v2.png?width=1240&height=676")
    embed.add_field(name="Création du bot :", value="09/04/21", inline=False)
    embed.add_field(name="Créateur : ", value="SPA (SuperPlayArt)", inline=True)
    embed.add_field(name="Langages :", value="Python", inline=True)
    embed.add_field(name="Préfix :", value="!s", inline=True)
    embed.add_field(name="GitHub :", value="[Cliquez ici](https://github.com/SuperPlayArt/SuperPlayBot)", inline=True)
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
    embed.add_field(name="!s info ", value="Permet d\'avoir les infos sur le bot.", inline=False)
    embed.add_field(name="!s invitebot ", value="Permet d\'invité le bot sur votre serveur.", inline=False)
    embed.add_field(name="!s invite ", value="Permet d'avoir le lien du serveur.", inline=False)
    embed.add_field(name="!s avatar", value="Pour avoir ton avatar ou celui des autres.", inline=True)
    embed.add_field(name="!s serv", value="Pioche au hasard un serveur dans une liste.", inline=True)
    embed.add_field(name="!s userinfo", value="Permet d\'avoir les information d'un utilisateur.", inline=True)
    embed.add_field(name="!s alertelog", value="Quand une blague nulle est faites utilisé cette commande.", inline=True)
    embed.add_field(name="!s say", value="Parler en tant que SPB. (Ne pas en abuser, sinon c'est lourd)", inline=True)
    embed.add_field(name="!s spa", value="Aidez la SPA.", inline=True)
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
    member = ctx.message.author.name
    embed=discord.Embed(title=" ".join(texte), color=0x9900ff)
    embed.set_footer(text=f'{member} à utilisé !s say')
    await ctx.message.delete()
    await ctx.send(embed=embed)

@client.command()
async def userinfo(ctx, *, member: discord.Member=None):
    if not member:
        member = ctx.message.author
    username = member.name
    userAvatar = member.avatar_url
    usercreation = member.created_at.strftime("%A, %B %d %Y at %H:%M:%S %p")
    userjoin = member.joined_at.strftime("%A, %B %d %Y at %H:%M:%S %p")
    embed=discord.Embed(title=f'**Voici les infos de {username} !**', color=0x9900ff)
    embed.set_thumbnail(url=member.avatar_url)
    embed.add_field(name="Nom d'utilisateur :", value=member, inline=False)
    embed.add_field(name="Date de création :", value=usercreation, inline=False)
    embed.add_field(name="Date d'arrivée :", value=userjoin, inline=False)
    embed.set_footer(text="2021 - SPA", icon_url="https://media.discordapp.net/attachments/797593407513559080/830098585772884028/Logo_SPA_v2.png?width=1240&height=676")
    await ctx.message.reply(embed=embed)



client.run('TOKEN')
