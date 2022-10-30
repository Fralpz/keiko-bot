from .utils import check_message_has_link
from app import redis_client
from app.data import moderations as moderations_data, cogs as cogs_data
from app.views.form import Form

# TODO: create save cog method to parse channels name to channe id

async def check_message(guild_id, message):
    """Command service to check if exists link on message"""
    enabled = moderations_data.find_parameter_by_guild(guild_id, "block_links")

    if enabled:
        parameters = cogs_data.find_cog_by_guild_id(guild_id)

        allowed_chats = parameters["allowed_chats"]
        allowed_links = parameters["allowed_links"]

        message_has_link = check_message_has_link(message, allowed_links)
        message_chat = str(message.channel.id)

        if message_has_link and message_chat not in allowed_chats:
            await message.delete()
            await message.channel.send(parameters["message"], delete_after=5)


async def manager(ctx, guild_id):
    enabled = moderations_data.find_parameter_by_guild(guild_id, "block_links")

    if not enabled:
        # TODO: move this to utils
        print("Não está ativado")
        for key in redis_client.scan_iter(f"{guild_id}@block_links:*"):
            redis_client.delete(key)

        form_view = Form(key="block_links")
        embed = form_view.get_question_embed_by_key("form")

        await ctx.response.send_message(embed=embed, view=form_view)