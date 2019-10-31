import serial
import discord
from discord.ext import commands

ser = serial.Serial('COM3', 9600)
bot = commands.Bot(command_prefix='')

@bot.event
async def on_ready():
    print('------------')
    print('Logado como ')
    print(bot.user.name)
    print(bot.user.id)
    print('------------')

@bot.command()
async def piscar(ctx):
    await ctx.send("Seu desejo é uma ordem, leds piscando!!")
    msg = 'a'
    ser.write(msg.encode())

@bot.command()
async def apagar(ctx):
    await ctx.send("Ah, tava tão legal!\nOk, vou apagar os leds")
    msg = 'b'
    ser.write(msg.encode())

@bot.command()
async def vermelho(ctx):
    await ctx.send("Led vermelho aceso, será que tem algo dando errado?")
    msg = 'c'
    ser.write(msg.encode())

@bot.command()
async def verde(ctx):
    await ctx.send("Opa, o led verde está aceso, pode seguir!")
    msg = 'd'
    ser.write(msg.encode())

@bot.command()
async def amarelo(ctx):
    await ctx.send("Amarelo é sinal de atenção!\nCuidado!")
    msg = 'e'
    ser.write(msg.encode())

@bot.command()
async def julia(ctx):
    await ctx.send("A namorada do Iago? Ah ela é tão linda!")

@bot.command()
async def jujuba(ctx):
    await ctx.send("O Iago me disse que esse apelido aí é só pros íntimos, cuidado!")

@bot.command()
async def iago(ctx):
    await ctx.send("Muito gente boa!")

@bot.command()
async def stewie(ctx):
    await ctx.send("O Clutch Master!")

@bot.command()
async def cientista(ctx):
    await ctx.send("Só erra os tiro!")

@bot.command()
async def somar(ctx, a: int, b: int):
    await ctx.send(a+b)

@bot.command()
async def subtrair(ctx, a: int, b: int):
    await ctx.send(a-b)

@bot.command()
async def multiplicar(ctx, a: int, b: int):
    await ctx.send(a*b)

@bot.command()
async def dividir(ctx, a: int, b: int):
    await ctx.send(a/b)

@bot.command()
async def piada(ctx):
    await ctx.send("Por que a galinha atravessou a rua?\nPra chegar do outro lado! :smiley: :wave:")

@bot.command()
async def eae(ctx):
    await ctx.send(":smiley: :wave: Eae, amigão!")

@bot.command()
async def gato(ctx):
    await ctx.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")

@bot.command()
async def ajuda(ctx):
    embed = discord.Embed(title="Bot", description="Os comandos estão aqui", color=0xeee657)

    embed.add_field(name="somar X Y", value="Soma dois valores", inline=False)
    embed.add_field(name="subtrair X Y", value="Subtrai dois valores", inline=False)
    embed.add_field(name="multiplicar X Y", value="Multiplica dois valores", inline=False)
    embed.add_field(name="dividir", value="Divide dois valores", inline=False)
    embed.add_field(name="piada", value="Conta uma piada", inline=False)
    embed.add_field(name="eae", value="Saudações", inline=False)
    embed.add_field(name="gato", value="Um gatinho nervoso", inline=False)
    embed.add_field(name="julia", value="Descubra", inline=False)
    embed.add_field(name="iago", value="Descubra", inline=False)
    embed.add_field(name="cientista", value="Descubra", inline=False)
    embed.add_field(name="stewie", value="Descubra", inline=False)
    embed.add_field(name="piscar", value="Pisca os leds no arduíno", inline=False)
    embed.add_field(name="apagar", value="Apaga todas os leds no arduíno", inline=False)
    embed.add_field(name="vermelho", value="Liga o led vermelho", inline=False)
    embed.add_field(name="verde", value="Liga o led verde", inline=False)
    embed.add_field(name="amarelo", value="Liga o led amarelo", inline=False)
    embed.add_field(name="ajuda", value="Lista os comandos do bot", inline=False)


    await ctx.send(embed=embed)

bot.run('NjM4OTY0ODc2MzQ5Mjc2MTcx.XbkqHQ.tQajICMehBqffYci3kwg4Dy9MkY')
