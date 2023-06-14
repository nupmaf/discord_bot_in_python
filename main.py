
import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)
client = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="mafia"))
    print('Бот запущен!')

@bot.command()
async def ссылка(ctx):
    await ctx.send('Ссылка на канал: url')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if "Привет" in message.content.lower() or "Здарова" in message.content.lower() or "Привет всем" in message.content.lower() or "прив" in message.content.lower():
         await message.channel.send(f'Привет, {message.author.mention}!')
    await bot.process_commands(message)

@bot.command()
async def linkch (ctx):
    embed = discord.Embed(
        title="Нажми для перехода",
        description="Ссылка для перехода на канал ",
        url='you url',
    )
    await ctx.send(embed=embed)

@bot.command()
async def test(ctx):
    embed = discord.Embed(
        title="Привет всем!",
    )
    await ctx.send(embed=embed)
   


@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'{member} Был забанен!')

@bot.command()
async def check(ctx):
    await ctx.send('Я готов к работе!')

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'{member} Был кикнут!')

@bot.command()
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    role = discord.utils.get(ctx.guild.roles, name='Muted')
    await member.add_roles(role, reason=reason)
    await ctx.send(f'{member} Замучен!')

@bot.command()
async def admins(ctx):
    admin_role = discord.utils.find(lambda r: r.name == 'Admin', ctx.message.guild.roles)
    admins = ''
    for member in ctx.guild.members:
        if admin_role in member.roles:
            admins += f'{member.name}\n'
    await ctx.send(f'Админы сервера:\n{admins}')

@bot.command()
async def info(ctx):
    guild = ctx.guild
    embed = discord.Embed(title=f"{guild.name}", description="Server Info", timestamp=ctx.message.created_at, color=discord.Color.blue())
    embed.set_thumbnail(url=guild.icon_url)
    embed.add_field(name="Server Crated It", value=f"{guild.created_at}")
    embed.add_field(name="Ваделец сервера", value=f"{guild.owner}")
    embed.add_field(name="Регион сервера", value=f"{guild.region}")
    embed.add_field(name="Сервер id", value=f"{guild.id}")
    await ctx.send(embed=embed)

bot.run('your_token_bot')