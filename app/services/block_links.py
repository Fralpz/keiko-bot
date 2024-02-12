import discord

from app.constants import Commands as constants
from app.data import cogs as cogs_data
from app.services.moderations import (
    send_command_form_message,
    send_command_manager_message,
)

from .utils import check_message_has_link, check_two_lists_intersection, list_roles_id


async def check_message(guild_id: str, message: discord.Message):
    """Command service to check if exists link on message"""
    cogs = cogs_data.find_cog_by_guild_id(guild_id, constants.BLOCK_LINKS_KEY)

    if not cogs:
        return

    message_author_has_allowed_role = check_two_lists_intersection(
        list_roles_id(message.author.roles),
        cogs[constants.ALLOWED_ROLES_KEY],
    )

    if message_author_has_allowed_role:
        return

    allowed_chats = cogs[constants.ALLOWED_CHATS_KEY]
    allowed_links = cogs[constants.ALLOWED_LINKS_KEY]

    message_has_link = check_message_has_link(message, allowed_links)
    message_chat = str(message.channel.id)

    if message_has_link and message_chat not in allowed_chats:
        await message.delete()
        await message.channel.send(cogs[constants.ANSWER_KEY], delete_after=5)


async def manager(ctx, guild_id):
    cogs = cogs_data.find_cog_by_guild_id(guild_id, constants.BLOCK_LINKS_KEY)

    if not cogs:
        return await send_command_form_message(ctx, constants.BLOCK_LINKS_KEY)

    await send_command_manager_message(ctx, constants.BLOCK_LINKS_KEY, cogs)
