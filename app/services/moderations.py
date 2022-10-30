from app.data import moderations as moderations_data, cogs as cogs_data
from typing import Any


async def upsert_parameter_by_guild(guild_id: str, parameter: str):
    if not guild_id:
        print("Check if guild_id is correct to save cog")
        return

    return moderations_data.upsert_parameters_by_guild(
        guild_id=guild_id, parameter=parameter
    )


async def upsert_cog_by_guild(guild_id: str, cog: str, data: dict[str, Any]):
    if not data.get("guild_id"):
        print("Check if guild_id is correct to save cog")
        return

    return cogs_data.upsert_cog_by_guild_id(guild_id, cog, data)


def apply_default_role_all_members():
    pass
    # role = discord.utils.get(guild.roles, id=838123185978998788)

    # for member in guild.members:
    #     if not role in member.roles:
    #         print(""")
    #         await member.add_roles(role)
    # print("Os cargos estão atualizados corretamente!")


def apply_role_in_member(guild, role_id):
    pass
    # role = discord.utils.get(guild.roles, id=role_id)
    # await member.add_roles(role)


async def send_welcome_message():
    pass
    # random_number = random.randint(0, 19)
    # rules_channel = self.bot.get_channel(838125350185074758)
    # channel = self.bot.get_channel(838123186142052442)

    # embed = discord.Embed(
    #     title=random.choice(self.config.welcome_messages_title).replace(
    #         "{person_name}", member.name
    #     ),
    #     description=random.choice(
    #         self.config.welcome_messages_descriptions
    #     ).replace("{channel_mention}", rules_channel.mention),
    #     color=0xFFCFFF,
    # )
    # embed.set_thumbnail(url=member.avatar_url)
    # embed.set_footer(text="")

    # if random_number == 15:
    #     embed.set_image(url="")

    # await channel.send(embed=embed)