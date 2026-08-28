
import traceback
import discord
from discord import SelectOption
from discord.ui import FileUpload, Label, Select
from typing import Optional, Union, cast




class SayModal(discord.ui.Modal, title="contenu du reply"):

    text = Label(text="Contenu du message", component=discord.ui.TextInput(
        style=discord.TextStyle.paragraph, label="Texte", min_length=1)
    )

    ping = Label(text="Mention", component=discord.ui.Select(
            options=[
                SelectOption(label="Oui", value="True", default=True),
                SelectOption(label="Non", value="False")
            ]
        )
    )

    file = Label(text="Photo de profil", component=FileUpload(required=False, min_values=0, max_values=1))

    def __init__(self, msg: discord.Message):
        self.msg = msg
        super().__init__()


    async def on_submit(self, interaction: discord.Interaction):
        # make the type checker shut the f up
        assert isinstance(self.text.component, discord.ui.TextInput)
        assert isinstance(self.ping.component, discord.ui.Select)
        assert isinstance(self.file.component, discord.ui.FileUpload)

        text = self.text.component.value
        ping = bool(self.ping.component.values[0])
        file = self.file.component.values[0]

        await self.msg.reply(content=text, mention_author=ping)
        await interaction.response.send_message(content="ton message a bien été envoyé", ephemeral=True)
        

    async def on_error(self, interaction: discord.Interaction, error: Exception) -> None:
        await interaction.response.send_message('Oops! Something went wrong.', ephemeral=True)

        # Make sure we know what the error actually is
        traceback.print_exception(type(error), error, error.__traceback__)

class ButtonView(discord.ui.LayoutView):
    def __init__(self, url: str, user: Union[discord.User, discord.Member], timeout: float | None = 180):
        super().__init__(timeout=timeout)
        self.add_item(discord.ui.Button(style=discord.ButtonStyle.url,
                      label=f"Photo de profil de {user.name}", url=url))
