import asyncio
import aioschedule as  schedule 
import os
from discord.ext import commands
import time

bot= commands.Bot(command_prefix='.')

@bot.event
async def on_ready():
  print("Bot is ready")

async def event(ctx, eventName):
  await ctx.send("@everyone we have the event "+eventName+" Don't fortget to join in")
  #await ctx.send("test")
  print("test")
  return schedule.CancelJob

@bot.command()
async def now(ctx):
  schedule.every(5).seconds.do( event, ctx, "test")
  while 1:
      await schedule.run_pending() 


@bot.command()
async def addEvent(ctx, arg1, arg2, arg3):
  if(arg2 =="monday"):
    schedule.every().monday.at(str(arg3)).do( event, ctx,arg1)
    await ctx.send("Event created {} Monday at {} " .format(arg1, arg3))
    

  if(arg2 == "tuesday"):
    schedule.every().tuesday.at(str(arg3)).do(event,ctx, arg1)
    await ctx.send("Event created {} Tuesday at {} " .format(arg1, arg3))
  

  if(arg2 == "wednesday"):
    schedule.every().wednesday.at(str(arg3)).do( event,ctx,arg1)
    await ctx.send("Event created {} Wednesday at {} " .format(arg1, arg3))
  

  if(arg2 == "thursday"):
    schedule.every().thursday.at(str(arg3)).do( event,ctx,arg1)
    await ctx.send("Event created {} Thursday at {} " .format(arg1, arg3))
   

  if(arg2 == "friday"):
    schedule.every().friday.at(str(arg3)).do( event,ctx,arg1)
    await ctx.send("Event created {} Friday at {} " .format(arg1, arg3))
  

  if(arg2 == "saturday"):
    schedule.every().saturday.at(str(arg3)).do( event,ctx,arg1)
    await ctx.send("Event created {} Saturday at {} " .format(arg1, arg3))
   

  if(arg2 == "sunday"):
    schedule.every().sunday.at(str(arg3)).do(event,ctx,arg1)
    await ctx.send("Event created {} Sunday at {} " .format(arg1, arg3))
  
  
  while True:
    await schedule.run_pending()



@bot.command()
async def eventHelp(ctx):
  await ctx.send('!To create an event, type in the following format ".createEvent {day} {time}" \n !When inserting the day please spell the entire day and in lower case.\n !When inserting time user the follwoing format "HH:SS" use a 24 hour format. Exp. 13:30 is 1:30 pm.')
@bot.command()
async def test(ctx, arg1):
  await ctx.send('{}'.format(arg1))

bot.run(os.getenv('TOKEN'))