import discord
import random
from discord import member
from discord import channel
from discord.ext import commands
import json
from PIL import Image
from io import BytesIO
from PIL import ImageFont
from PIL import ImageDraw
from PIL import ImageOps
import asyncio
from discord.ext.commands.errors import MissingRequiredArgument
from discord.flags import SystemChannelFlags
from discord.ext.commands import has_permissions, MissingPermissions
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix = '"s ', intents=intents)
client.remove_command("help")

#------------------------LINK & CHANNEL------------------------------

guild_link = ''
level_link = ''
log_channel = 
onready_channel = 
support_channel = 
tarmac_font = ''
tarmac_original_img = ''
tarmac_final_img = ''
tarmac_bye_original_img = ''
tarmac_bye_final_img = ''
level_font = ''
level_font1 = ''
level_original_img = ''
level_final_img = ''

#----------------------------EVENT------------------------------

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f'\"s help'))
    print('---{ SuperPlayBot }---')
    print('Connecté au robot : {}'.format(client.user.name))
    print('ID: {}'.format(client.user.id))
    print('2021 - SPA')
    channel = client.get_channel(onready_channel)
    embed=discord.Embed(title="SuperPlayBot", description="Je suis en ligne !", color=0x9900ff)
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/797593407513559080/848962608740171847/SPB_ONLINE.png?width=859&height=468")
    embed.add_field(name="Besoin d'aide ?", value="\"s help", inline=True)
    embed.add_field(name="Si vous voulez rapporté un problème :", value="\"s support", inline=True)
    embed.set_footer(text="2021 - SPA ⭐")
    await channel.send(embed=embed)

@client.event
async def on_member_join(member):
    with open(guild_link, 'r', encoding='utf-8') as f:
        guilds_dict = json.load(f)
    channel_id = guilds_dict[str(member.guild.id)]
    font = ImageFont.truetype(tarmac_font, 175)
    img = Image.open(tarmac_original_img)
    draw = ImageDraw.Draw(img)
    draw.text((1975,620),f"{member.name},",(255,255,255),font=font)
    img.save(tarmac_final_img)
    await client.get_channel(int(channel_id)).send(file=discord.File(tarmac_final_img))
    with open(level_link, 'r') as f:
        users = json.load(f)
    await update_data(users, member)
    with open(level_link, 'w') as f:
        json.dump(users, f)

@client.event
async def on_member_remove(member):
    with open(guild_link, 'r', encoding='utf-8') as f:
        guilds_dict = json.load(f)

    channel_id = guilds_dict[str(member.guild.id)]
    font = ImageFont.truetype(tarmac_font, 175)
    img = Image.open(tarmac_bye_original_img)
    draw = ImageDraw.Draw(img)
    draw.text((2135,620),f"{member.name},",(255,255,255),font=font)
    img.save(tarmac_bye_final_img)
    await client.get_channel(int(channel_id)).send(file=discord.File(tarmac_bye_final_img))

@client.event
async def on_command_error(ctx, error):
    log = client.get_channel(log_channel)
    if isinstance(error, commands.CommandNotFound):
        embed=discord.Embed(title="Cette commande n'existe pas...", description='`Code erreur 001 - Pour contacter le support : \"s support`', color=0x9900ff)
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/797593407513559080/859527922029428756/SPB_ERROR.png?width=508&height=468")
        embed.set_footer(text="2021 - SPA ⭐")
        await ctx.message.reply(embed=embed)
        await log.send('-> Erreur 001')
    if isinstance(error, MissingRequiredArgument):
        embed=discord.Embed(title="Cette commande à besoin d'un argument !", description='`Code erreur 002 - Pour contacter le support : \"s support`', color=0x9900ff)
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/797593407513559080/859527922029428756/SPB_ERROR.png?width=508&height=468")
        embed.set_footer(text="2021 - SPA ⭐")
        await ctx.message.reply(embed=embed)
        await log.send('-> Erreur 002')
    elif isinstance(error, MissingPermissions):
        embed=discord.Embed(title="Cette commande à besoin d'une permission... que tu n'a pas...", description='`Code erreur 003 - Contacte l\'administrateur du serveur !`', color=0x9900ff)
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/797593407513559080/859527922029428756/SPB_ERROR.png?width=508&height=468")
        embed.set_footer(text="2021 - SPA ⭐")
        await ctx.message.reply(embed=embed)
        await log.send('-> Erreur 003')

@client.event
async def on_message(message):
    if not message.author.bot:
        with open(level_link,'r') as f:
            users = json.load(f)
        await update_data(users, message.author,message.guild)
        await add_experience(users, message.author, 4, message.guild)
        await level_up(users, message.author,message.channel, message.guild)

        with open(level_link,'w') as f:
            json.dump(users, f)
    await client.process_commands(message)

@client.event
async def on_guild_remove(guild):
    with open(guild_link, 'r', encoding='utf-8') as f:
        guilds_dict = json.load(f)
    guilds_dict.pop(guild.id)
    with open(guild_link, 'w', encoding='utf-8') as f:
        json.dump(guilds_dict, f, indent=4, ensure_ascii=False)

#----------------------------COMMANDES BASIQUES------------------------------

@client.command()
async def info(ctx):
    embed=discord.Embed(title="SuperPlayBot - Les infos du bot !", description="Voici les infos du bot !", color=0x9900ff)
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/797593407513559080/859525089984118815/SPB_INFO.png?width=508&height=468")
    embed.add_field(name="Création du bot :", value="09/04/21", inline=False)
    embed.add_field(name="Créateur : ", value="SPA (SuperPlayArt)", inline=True)
    embed.add_field(name="Systeme : ", value="Raspberry Pi 3B+", inline=True)
    embed.add_field(name="Langages :", value="Python", inline=True)
    embed.add_field(name="Préfix :", value="\"s", inline=True)
    embed.add_field(name="Nombre de serveur :", value=len(client.guilds), inline=True)
    embed.add_field(name="GitHub :", value="[Cliquez ici](https://github.com/SuperPlayArt/SuperPlayBot)", inline=True)
    embed.add_field(name="Email :", value="superplayart@gmail.com", inline=True)
    embed.set_footer(text="2021 - SPA ⭐")
    await ctx.message.reply(embed=embed)

@client.command(aliases=['pp'])
async def avatar(ctx, *, member: discord.Member=None):
    if not member:
        member = ctx.message.author # set member as the author
    userAvatar = member.avatar_url
    embed=discord.Embed(title=member, url="https://fr.wikipedia.org/wiki/Avatar_(film,_2009)", description="C'est son avatar (Pas le film mdr)", color=0x9900ff)
    embed.set_image(url=userAvatar)
    await ctx.message.reply(embed=embed)

@client.command(aliases=['aide'])
async def help(ctx):
    contents = ["**__Voici les commandes basiques !__**\n\n**\"s help**\nTu l'utilises actuellement !\n**\"s support**\nPermet de contacté le support du bot.\n**\"s info**\nPermet d'avoir des informations sur le bot.\n**\"s setup (set)**\nPermet de configurer le SPB.\n**\"s userinfo**\nPermet d'avoir des infos sur un toi ou un utilisateur.\n**\"s serverinfo**\nPermet d'avoir des infos sur le serveur.\n**\"s level**\nPermet de savoir ton level sur un serveur.\n**\"s avatar**\nPermet d'avoir l'avatar d'un membre ou le tiens.", "**__Voici les autres commandes !__**\n\n**\"s spa**\nAidez la spa.\n**\"s say**\nPermet de se prendre pour Anonymous."]
    pages = 2
    cur_page = 1
    embed=discord.Embed(title=f"SuperPlayBot - Les commandes \[ {cur_page}/{pages} ]", description=f"{contents[cur_page-1]}", color=0x9900ff)
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/797593407513559080/859525087568330762/SPB_HELP.png?width=508&height=468")
    embed.set_footer(text="2021 - SPA ⭐")
    message = await ctx.message.reply(embed=embed)
    await message.add_reaction("◀️")
    await message.add_reaction("▶️")
    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"]
    while True:
        try:
            reaction, user = await client.wait_for("reaction_add", timeout=60, check=check)
            if str(reaction.emoji) == "▶️" and cur_page != pages:
                cur_page += 1
                embed=discord.Embed(title=f"SuperPlayBot - Les commandes \[ {cur_page}/{pages} ]", description=f"{contents[cur_page-1]}", color=0x9900ff)
                embed.set_thumbnail(url="https://media.discordapp.net/attachments/797593407513559080/859525087568330762/SPB_HELP.png?width=508&height=468")
                embed.set_footer(text="2021 - SPA ⭐")
                await message.edit(embed=embed)
                await message.remove_reaction(reaction, user)
            elif str(reaction.emoji) == "◀️" and cur_page > 1:
                cur_page -= 1
                embed=discord.Embed(title=f"SuperPlayBot - Les commandes \[ {cur_page}/{pages} ]", description=f"{contents[cur_page-1]}", color=0x9900ff)
                embed.set_thumbnail(url="https://media.discordapp.net/attachments/797593407513559080/859525087568330762/SPB_HELP.png?width=508&height=468")
                embed.set_footer(text="2021 - SPA ⭐")
                await message.edit(embed=embed)
                await message.remove_reaction(reaction, user)
            else:
                await message.remove_reaction(reaction, user)
        except asyncio.TimeoutError:
            await message.delete()
            break

@client.command()
async def userinfo(ctx, *, member: discord.Member=None):
    if not member:
        member = ctx.message.author
    username = member.name
    userAvatar = member.avatar_url
    usercreation = member.created_at.strftime("%d/%m/%Y à %H:%M")
    rolelist = [r.mention for r in member.roles if r != ctx.guild.default_role]
    userjoin = member.joined_at.strftime("%d/%m/%Y à %H:%M")
    embed=discord.Embed(title=f'**Voici les infos de {username} !**', color=0x9900ff)
    embed.set_thumbnail(url=member.avatar_url)
    embed.add_field(name="Nom d'utilisateur :", value=member, inline=False)
    embed.add_field(name="Date de création :", value=usercreation, inline=False)
    embed.add_field(name="Date d'arrivée :", value=userjoin, inline=False)
    embed.add_field(name="Rôle(s) :", value=", ".join(rolelist), inline=False)
    embed.set_footer(text="2021 - SPA ⭐")
    await ctx.message.reply(embed=embed)

@client.command()
async def serverinfo(ctx, *, member: discord.Member=None):
  name = str(ctx.guild.name)
  description = str(ctx.guild.description)
  owner = str(ctx.guild.owner.name)
  id = str(ctx.guild.id)
  region = str(ctx.guild.region)
  memberCount = str(ctx.guild.member_count)
  icon = str(ctx.guild.icon_url)
  server = ctx.message.guild
  role_count = len(server.roles)
  emoji_count = len(server.emojis)
  RoleList = [r.mention for r in ctx.guild.roles]
  embed = discord.Embed(title=f"Voici les information du serveur **{name}** :", color=0x9900ff)
  embed.set_thumbnail(url=icon)
  embed.add_field(name="Administrateur :", value=owner, inline=True)
  embed.add_field(name="ID :", value=id, inline=True)
  embed.add_field(name="Nombre de personne :", value=memberCount, inline=True)
  embed.add_field(name='Date de création :', value=server.created_at.__format__("%d/%m/%Y à %H:%M"), inline=True)
  embed.add_field(name='Nombre de rôles :', value=str(role_count))
  embed.add_field(name='Nombre d\'émojis :', value=str(emoji_count))
  embed.add_field(name='Liste des rôles :', value=", ".join(RoleList))
  await ctx.message.reply(embed=embed)

@client.command(aliases=['clear'])
@commands.has_permissions(manage_messages=True)
async def suppr(ctx, nombre: int):
    messages = await ctx.channel.history(limit=nombre +1).flatten()
    for message in messages:
        await message.delete()

@client.command()
async def support(ctx, *texte):
    member = ctx.message.author
    source = ctx.guild.name
    channel_source = ctx.channel.name
    support = client.get_channel(support_channel)
    embed1=discord.Embed(title='SuperPlayBot - Support', color=0x9900ff)
    embed1.add_field(name="Message :", value=" ".join(texte), inline=False)
    embed1.add_field(name="Source :", value=f'Depuis `{source}`, dans le salon `{channel_source}`, envoyé par `{member}`', inline=False)
    embed1.set_thumbnail(url="https://media.discordapp.net/attachments/797593407513559080/859525096518320158/SPB_SUPPORT.png?width=508&height=468")
    embed1.set_footer(text="2021 - SPA ⭐")
    await support.send(embed=embed1)
    await ctx.message.reply(f'{member.mention}, ton message à bien était envoyé au support !')

@client.command(aliases = ['rank','lvl'])
async def level(ctx,member: discord.Member = None):
    log = client.get_channel(log_channel)
    if not member:
        user = ctx.message.author
        with open(level_link,'r') as f:
            users = json.load(f)
        if not f'{ctx.guild.id}' in users:
            embed=discord.Embed(title="LƎVƎL est désactivé sur ce serveur =(", description=f'`Code erreur 010 - Vous pouvez l\'activé via \"s set`', color=0x9900ff)
            embed.set_thumbnail(url="https://media.discordapp.net/attachments/797593407513559080/859525092065148948/SPB_LEVEL.png?width=508&height=468")
            embed.set_footer(text="2021 - SPA ⭐")
            await ctx.message.reply(embed=embed)
            await log.send('-> Erreur 010')
        else:
            lvl = users[str(ctx.guild.id)][str(user.id)]['level']
            exp = users[str(ctx.guild.id)][str(user.id)]['experience']
            embed=discord.Embed(title=f"LƎVƎL :", description="Voici tes statistiques :", color=0x9900ff)
            embed.add_field(name='Level :', value=lvl)
            embed.add_field(name='EXP :', value=exp)
            embed.set_thumbnail(url="https://media.discordapp.net/attachments/797593407513559080/859525092065148948/SPB_LEVEL.png?width=508&height=468")
            embed.set_footer(text="2021 - SPA ⭐")
            await ctx.message.reply(embed=embed)
    else:
      with open(level_link,'r') as f:
          users = json.load(f)
      lvl = users[str(ctx.guild.id)][str(member.id)]['level']
      exp = users[str(ctx.guild.id)][str(member.id)]['experience']
      embed=discord.Embed(title=f"LƎVƎL :", description=f"Voici les statistiques de {member.name} :", color=0x9900ff)
      embed.add_field(name='Level :', value=lvl)
      embed.add_field(name='EXP :', value=exp)
      embed.set_thumbnail(url="https://media.discordapp.net/attachments/797593407513559080/859525092065148948/SPB_LEVEL.png?width=508&height=468")
      embed.set_footer(text="2021 - SPA ⭐")
      await ctx.message.reply(embed=embed)

@client.command(name='setup', aliases = ['set','configuration'])
@has_permissions(administrator=True, manage_messages=True)
async def setup(ctx,arg=None,arg2=None, channel: discord.TextChannel = None, member: discord.Member = None):
    log = client.get_channel(log_channel)
    if arg == 'tarmac':
        with open(guild_link, 'r', encoding='utf-8') as f:
            guilds_dict = json.load(f)
        if arg2 == 'on':
            if not channel:
                embed=discord.Embed(title="Pour configurer le tarmac il faut mentionner le salon de bienvenue et de départ", description=f'`Code erreur 004 - Pour contacter le support : "s support`', color=0x9900ff)
                embed.set_thumbnail(url="https://media.discordapp.net/attachments/797593407513559080/864057019660501012/SPB_TARMAC.png?width=508&height=468")
                embed.set_footer(text="2021 - SPA ⭐")
                await ctx.message.reply(embed=embed)
                await log.send('-> Erreur 004')
            else:
                if not f'{ctx.guild.id}' in guilds_dict:
                    guilds_dict[str(ctx.guild.id)] = str(channel.id)
                    with open('/home/pi/Desktop/BOT/guilds.json', 'w', encoding='utf-8') as f:
                        json.dump(guilds_dict, f, indent=4, ensure_ascii=False)

                    embed=discord.Embed(title="Le tarmac a bien été configuré !", description=f'Les arrivées et les départs seront affichés dans le salon `{channel.name}` sur le serveur {ctx.message.guild.name}', color=0x9900ff)
                    embed.set_thumbnail(url="https://media.discordapp.net/attachments/797593407513559080/864057019660501012/SPB_TARMAC.png?width=508&height=468")
                    embed.set_footer(text="2021 - SPA ⭐")
                    await ctx.message.reply(embed=embed)
                else:
                    embed=discord.Embed(title="Le tarmac a déjà été configuré !", description=f'`Code erreur 005 - Pour contacter le support : "s support`', color=0x9900ff)
                    embed.set_thumbnail(url="https://media.discordapp.net/attachments/797593407513559080/864057019660501012/SPB_TARMAC.png?width=508&height=468")
                    embed.set_footer(text="2021 - SPA ⭐")
                    await ctx.message.reply(embed=embed)
                    await log.send('-> Erreur 005')

        if arg2 == 'off':
            if f'{ctx.guild.id}' in guilds_dict:
                del guilds_dict[str(ctx.guild.id)]
                with open(guild_link, 'w', encoding='utf-8') as f:
                    json.dump(guilds_dict, f, indent=4, ensure_ascii=False)
                embed=discord.Embed(title="Le tarmac a bien été supprimé !", description=f'Les arrivées et les départs seront plus affichés dans le serveur {ctx.message.guild.name}', color=0x9900ff)
                embed.set_thumbnail(url="https://media.discordapp.net/attachments/797593407513559080/864057019660501012/SPB_TARMAC.png?width=508&height=468")
                embed.set_footer(text="2021 - SPA ⭐")
                await ctx.message.reply(embed=embed)
            else:
                embed=discord.Embed(title="Le tarmac a déjà été supprimé !", description=f'`Code erreur 006 - Pour contacter le support : "s support`', color=0x9900ff)
                embed.set_thumbnail(url="https://media.discordapp.net/attachments/797593407513559080/864057019660501012/SPB_TARMAC.png?width=508&height=468")
                embed.set_footer(text="2021 - SPA ⭐")
                await ctx.message.reply(embed=embed)
                await log.send('-> Erreur 006')

    elif arg == 'level':
        if arg2 == 'on':
            with open(level_link, 'r', encoding='utf-8') as f:
                users = json.load(f)
            if not f'{ctx.guild.id}' in users:
                users[str(ctx.guild.id)] = {}
                with open(level_link, 'w', encoding='utf-8') as f:
                    json.dump(users, f, indent=4, ensure_ascii=False)

                embed=discord.Embed(title="LƎVƎL a été activé !", color=0x9900ff)
                embed.set_thumbnail(url="https://media.discordapp.net/attachments/797593407513559080/859525092065148948/SPB_LEVEL.png?width=508&height=468")
                embed.set_footer(text="2021 - SPA ⭐")
                await ctx.message.reply(embed=embed)
            else:
                embed=discord.Embed(title="LƎVƎL est déjà activé !", description=f'`Code erreur 007 - Pour contacter le support : "s support`', color=0x9900ff)
                embed.set_thumbnail(url="https://media.discordapp.net/attachments/797593407513559080/859525092065148948/SPB_LEVEL.png?width=508&height=468")
                embed.set_footer(text="2021 - SPA ⭐")
                await ctx.message.reply(embed=embed)
                await log.send('-> Erreur 007')

        if arg2 == 'off':
            with open(level_link, 'r', encoding='utf-8') as f:
                users = json.load(f)
            if not f'{ctx.guild.id}' in users:
                embed=discord.Embed(title="LƎVƎL est déjà désactivé !", description=f'`Code erreur 008 - Pour contacter le support : "s support`', color=0x9900ff)
                embed.set_thumbnail(url="https://media.discordapp.net/attachments/797593407513559080/859525092065148948/SPB_LEVEL.png?width=508&height=468")
                embed.set_footer(text="2021 - SPA ⭐")
                await ctx.message.reply(embed=embed)
                await log.send('-> Erreur 008')
            else:
                del users[str(ctx.guild.id)]
                with open(level_link, 'w', encoding='utf-8') as f:
                    json.dump(users, f, indent=4, ensure_ascii=False)

                embed=discord.Embed(title="LƎVƎL a été désactivé !", color=0x9900ff)
                embed.set_thumbnail(url="https://media.discordapp.net/attachments/797593407513559080/859525092065148948/SPB_LEVEL.png?width=508&height=468")
                embed.set_footer(text="2021 - SPA ⭐")
                await ctx.message.reply(embed=embed)
    else:
        embed=discord.Embed(title="SuperPlayBot - Setup", description="__**Bienvenue dans le configurateur !**__\n\n**\"s set level on/off**\nPermet d'activé ou desactivé les levels dans votre serveur. [ Par défaut, il est désactivé ]\n**\"s tarmac on/off**\nPermet l'activation du tarmac sur un salon. [ Par défaut, il est désactivé ]", color=0x9900ff)
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/797593407513559080/859701708417400892/SPB.png?width=846&height=468")
        embed.set_footer(text="2021 - SPA ⭐")
        await ctx.message.reply(embed=embed)

@client.command(aliases=['spbinvite'])
async def invitebot(ctx):
    embed=discord.Embed(title="Clique ici pour inviter le bot !", url="https://discord.com/api/oauth2/authorize?client_id=820733417640951808&permissions=8&scope=bot%20applications.commands", description="⚠️ Ce bot est aussi stable que une connexion SFR ⚠️", color=0x9900ff)
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/797593407513559080/830098585772884028/Logo_SPA_v2.png?width=1240&height=676")
    embed.set_footer(text="2021 - SPA ⭐")
    await ctx.send(embed=embed)

@client.command(aliases=['golog'])
async def alertelog(ctx):
    await ctx.message.delete()
    await ctx.send('https://media.discordapp.net/attachments/797593407513559080/830180368853893180/exit.png?width=1440&height=529')

@client.command(aliases=['dire'])
async def say(ctx, *texte, member: discord.Member=None):
    member = ctx.message.author
    log = client.get_channel(log_channel)
    embed=discord.Embed(title=" ".join(texte), color=0x9900ff)
    embed.set_author(name=f"Anonymous - Agent {member.discriminator}", icon_url="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a6/Anonymous_emblem.svg/1024px-Anonymous_emblem.svg.png")
    embed.set_footer(text='2021 - SPA ⭐')
    await ctx.message.delete()
    await ctx.send(embed=embed)
    await log.send(f'{member.name} à utilisé !s say')

@client.command()
async def serv(ctx):
  responses = ['Serveur LLANCOSS\'WORLD : https://discord.gg/qVYeCdZqMP', 'Serveur Bourgade Slawkienne : https://discord.gg/P4J3gzRSrp', 'Serveur DBKILLER x Guigui : https://discord.gg/7mPYHjRkDc', 'Serveur Chromavirus : https://discord.gg/VGCCaZq']
  responses = random.choice(responses)
  embed=discord.Embed(title="SPA te conseil ce serveur !", description=responses, color=0x9900ff)
  embed.set_thumbnail(url="https://media.discordapp.net/attachments/797593407513559080/859701708417400892/SPB.png?width=846&height=468")
  embed.set_footer(text="2021 - SPA ⭐")
  await ctx.message.reply(embed=embed)

#----------------------------LEVEL------------------------------

async def update_data(users, user,server):
    if not str(server.id) in users:
        return
    elif not str(user.id) in users[str(server.id)]:
            users[str(server.id)][str(user.id)] = {}
            users[str(server.id)][str(user.id)]['experience'] = 0
            users[str(server.id)][str(user.id)]['level'] = 1

async def add_experience(users, user, exp, server):
   if not str(user.guild.id) in users:
        return
   elif str(user.guild.id) in users:
       users[str(user.guild.id)][str(user.id)]['experience'] += exp

async def level_up(users, user, channel, server):
  if not str(user.guild.id) in users:
        return
  elif str(user.guild.id) in users:
    experience = users[str(user.guild.id)][str(user.id)]['experience']
    lvl_start = users[str(user.guild.id)][str(user.id)]['level']
    lvl_end = int(experience ** (1/4))
    if str(user.guild.id) != '757383943116030074':
     if lvl_start < lvl_end:
        font = ImageFont.truetype(level_font, 160)
        font1 = ImageFont.truetype(level_font1, 700)
        img = Image.open(level_original_img)
        draw = ImageDraw.Draw(img)
        draw.text((2152,277),f"{user.name},",(255,255,255),font=font)
        draw.text((2922,840),f"{lvl_end}",(255,255,255),font=font1)
        img.save(level_final_img)
        await channel.send(file=discord.File(level_final_img))
        users[str(user.guild.id)][str(user.id)]['level'] = lvl_end

client.run('token')