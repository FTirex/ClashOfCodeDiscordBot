import discord
from discord.ext import commands

# define a function to calculate the score
def calculate_score(player_name, time_given, progress_percent, rank):
    try:
        # convert time_given to seconds
        time_seconds = 0
        for time_part in time_given.split():
            if time_part.endswith("s"):
                time_seconds += int(time_part[:-1])
            elif time_part.endswith("m"):
                time_seconds += int(time_part[:-1]) * 60

        # check if time_given is within range
        if time_seconds < 0 or time_seconds > 900:
            raise ValueError("time_given should be between 0 and 15 minutes (900 seconds).")

        # check if progress_percent is within range
        if progress_percent < 0 or progress_percent > 100:
            raise ValueError("progress_percent should be between 0 and 100.")

        # calculate the score for the round
        if time_seconds == 0:
            score = 0
        else:
            score = int(100.0 / time_seconds * progress_percent * (16 - rank) / 15)

        # return the calculated score
        return f"The score for {player_name}'s round is {score}."

    except ValueError as e:
        # return an error message
        return f"Error: {e}"
    except ZeroDivisionError:
        # return an error message
        return "Error: time_given cannot be zero."
    
# create a Discord bot
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='/', intents=intents)

# define a command to calculate the score
@bot.command()
async def score(ctx, name, time_given, progress, rank):
    score = calculate_score(name, time_given, float(progress), int(rank)) 
    # !score John 1m 30s 50 2
    await ctx.send(score)

# start the bot
bot.run('Token Here')



