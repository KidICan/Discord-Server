import schedule 
import time
import os
from discord.ext import commands

bot= commands.Bot(command_prefix='.')

@bot.event
async def on_ready():
  print("Bot is ready")

async def event(ctx, eventName):
  await ctx.send("@everyone we have the event"+eventName+"Don't fortget to join in")
  await ctx.send("test")
  print("test")

def nothing(t):
  return 0

@bot.command()
async def now(ctx):
  schedule.every(1).seconds.do(nothing,await event(ctx, "OW"))
  while 1:
      schedule.run_pending()
      time.sleep(1)



@bot.command()
async def addEvent(ctx, arg1, arg2, arg3):
  if(arg2 =="monday"):
    schedule.every().monday.at(arg3).do(nothing, await event(ctx,arg1))
    await ctx.send("Event created {} Monday at {} " .format(arg1, arg3))
    

  if(arg2 == "tuesday"):
    schedule.every().tuesday.at(arg3).do(nothing, await event(ctx,arg1))
    await ctx.send("Event created {} Tuesday at {} " .format(arg1, arg3))
  

  if(arg2 == "wednesday"):
    schedule.every().wednesday.at(arg3).do(nothing, await event(ctx,arg1))
    await ctx.send("Event created {} Wednesday at {} " .format(arg1, arg3))
  

  if(arg2 == "thursday"):
    schedule.every().thursday.at(arg3).do(nothing, await event(ctx,arg1))
    await ctx.send("Event created {} Thursday at {} " .format(arg1, arg3))
   

  if(arg2 == "friday"):
    schedule.every().friday.at(arg3).do(nothing, await event(ctx,arg1))
    await ctx.send("Event created {} Friday at {} " .format(arg1, arg3))
  

  if(arg2 == "saturday"):
    schedule.every().saturday.at(arg3).do(nothing, await event(ctx,arg1))
    await ctx.send("Event created {} Saturday at {} " .format(arg1, arg3))
   

  if(arg2 == "sunday"):
    schedule.every().sunday.at(arg3).do(nothing, await event(ctx,arg1))
    await ctx.send("Event created {} Sunday at {} " .format(arg1, arg3))
  
  while 1:
      schedule.run_pending()
      time.sleep(1)



@bot.command()
async def eventHelp(ctx):
  await ctx.send('!To create an event, type in the following format ".createEvent {day} {time}" \n !When inserting the day please spell the entire day and in lower case.\n !When inserting time user the follwoing format "HH:SS" use a 24 hour format. Exp. 13:30 is 1:30 pm.')
@bot.command()
async def test(ctx, arg1):
  await ctx.send('{}'.format(arg1))

bot.run(os.getenv('TOKEN'))