import discord

from typing import Callable


class ConfirmButton(discord.ui.Button):
    def __init__(self, callback: Callable) -> None:
        self.callback = callback
        super().__init__(label="Confirmar", style=discord.ButtonStyle.green)


class CancelButtom(discord.ui.Button):
    def __init__(self) -> None:
        super().__init__(label="Cancelar", style=discord.ButtonStyle.red)

    async def callback(self, interaction: discord.Interaction) -> None:
        self.view.clear_items()
        await interaction.message.edit(view=self.view)


class OptionsButton(discord.ui.Button):
    def __init__(self, options_label: str, options_custom_id: str) -> None:
        super().__init__(
            label=options_label,
            style=discord.ButtonStyle.gray,
            custom_id=options_custom_id,
        )

    async def callback(self, interaction: discord.Interaction) -> None:
        if self.style == discord.ButtonStyle.primary:
            self.style = discord.ButtonStyle.gray
            del self.view.selected[self.custom_id]
        else:
            self.style = discord.ButtonStyle.primary
            self.view.selected[self.custom_id] = self.label

        await interaction.response.edit_message(view=self.view)