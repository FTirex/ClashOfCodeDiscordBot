import colorama
from colorama import Fore
from typing import Any
import asyncio
from nextcord import SlashOption, Interaction, Embed, Colour, Color
import nextcord
from nextcord.ext import commands

bot = commands.Bot(command_prefix='.')

async def send(
    interaction: Interaction, 
    message: str, 
    color: Colour = Color.red(),
    title: str = '',
) -> Any:
    try:
        return await interaction.response.send_message(embed=Embed(
            description=message,
            color=color,
            title=title,
        ))
    except:
        return await interaction.send(embed=Embed(
            description=message,
            color=color,
            title=title,
        ))

@bot.slash_command(
    name='calculate_score',
    description='calculate score',
)
async def calculate_score(
    inter: Interaction,
    player_name: str=SlashOption(
        name='player_name',
        description='put the player name',
        required=True,
    ),
    time_given: str=SlashOption(
        name='time_given',
        description='put the time given',
        required=True,
    ),
    progress_percent: float=SlashOption(
        name='progress_percent',
        description='put the progress percent',
        required=True,
    ),
    rank: int=SlashOption(
        name='rank',
        description='put the rank',
        required=True,
    )
): 
    time_seconds = 0
    for time_part in time_given.split():
        if time_part.endswith("s"):
            time_seconds += int(time_part[:-1])
        elif time_part.endswith("m"):
            time_seconds += int(time_part[:-1]) * 60

    if time_seconds < 0 or time_seconds > 900:
        await send(interaction=inter, message="time_given should be between 0 and 15 minutes (900 seconds).")

    if progress_percent < 0 or progress_percent > 100:
        await send(interaction=inter, message="progress_percent should be between 0 and 100.")
    
    if time_seconds == 0:
        score = 0
    else:
        score = int(100.0 / time_seconds * progress_percent * (16 - rank) / 15)

    await send(interaction=inter, message=f"The score for {player_name}'s round is {score}.")




@bot.event
async def on_ready():
    print('Connected')
    print(bot.user.name)
    print(bot.user.id)

bot.run('')
