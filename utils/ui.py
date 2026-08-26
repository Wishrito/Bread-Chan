from typing import Optional, Union, cast


import discord


class SayModal(discord.ui.Modal, title="contenu du reply"):
    def __init__(self, msg: discord.Message):
        self.msg = msg
        super().__init__()
    textinput = discord.ui.TextInput(
        style=discord.TextStyle.paragraph, label="Texte", min_length=1)
    ping = discord.ui.TextInput(style=discord.TextStyle.short, label="Mention",
                                min_length=3, max_length=3, placeholder="Oui ou Non", required=False)
    ping2 = bool(ping.value.casefold().replace(
        "oui", "True").replace("non", "False"))

    async def on_submit(self, interaction: discord.Interaction):
        if not self.ping:
            await self.msg.reply(self.textinput.value, mention_author=True)
            await interaction.response.send_message(content="ton message a bien été envoyé", ephemeral=True)
        else:
            await self.msg.reply(self.textinput.value, mention_author=self.ping2)
            await interaction.response.send_message(content="ton message a bien été envoyé", ephemeral=True)


class ButtonView(discord.ui.View):
    def __init__(self, url: str, user: Union[discord.User, discord.Member], timeout: float | None = 180):
        super().__init__(timeout=timeout)
        self.add_item(discord.ui.Button(style=discord.ButtonStyle.url,
                      label=f"Photo de profil de {user.name}", url=url))
