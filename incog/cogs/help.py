import os, sys, discord
from discord.ext import commands
if not os.path.isfile("config.py"):
    sys.exit("'config.py' not found! Please add it and try again.")
else:
    import config

class Help(commands.Cog, name="help"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help")
    async def help(self, context):
        # Note that commands made only for the owner of the bot are not listed here.
        embed = discord.Embed(
            title="incog",
            description="Commands & Usage:",
            color=0x00FF00
        )
        embed.add_field(
            name="Price",
            value=f"Usage: {config.BOT_PREFIX}price <prv> <base_currency>",
            inline=False
        )
        embed.add_field(
            name="Explorer",
            value=f"Usage: {config.BOT_PREFIX}explorer",
            inline=False
        )
        embed.add_field(
            name="Privacy Quest",
            value=f"Usage: {config.BOT_PREFIX}quest",
            inline=False
        )
        embed.add_field(
            name="Github",
            value=f"Usage: {config.BOT_PREFIX}github",
            inline=False
        )
        embed.add_field(
            name="Exchange",
            value=f"Usage: {config.BOT_PREFIX}exchange",
            inline=False
        )
        embed.add_field(
            name="pTokens",
            value=f"Usage: {config.BOT_PREFIX}ptoken",
            inline=False
        )
        embed.add_field(
            name="Invest, Earn anonymously",
            value=f"Usage: {config.BOT_PREFIX}provide",
            inline=False
        )
        embed.add_field(
            name="privacy focused fiat on/off ramp",
            value=f"Usage: {config.BOT_PREFIX}fiat",
            inline=False
        )
        embed.add_field(
            name="Staking",
            value=f"Usage: {config.BOT_PREFIX}staking",
            inline=False
        )
        embed.add_field(
            name="pNode",
            value=f"Usage: {config.BOT_PREFIX}node",
            inline=False
        )
        embed.add_field(
            name="Whitepaper",
            value=f"Usage: {config.BOT_PREFIX}whitepaper",
            inline=False
        )
        embed.add_field(
            name="Validators",
            value=f"Usage: {config.BOT_PREFIX}validators",
            inline=False
        )
        embed.add_field(
            name="Roadmap",
            value=f"Usage: {config.BOT_PREFIX}roadmap",
            inline=False
        )
        embed.add_field(
            name="Website",
            value=f"Usage: {config.BOT_PREFIX}website",
            inline=False
        )
        embed.add_field(
            name="Community",
            value=f"Usage: {config.BOT_PREFIX}community",
            inline=False
        )
        embed.add_field(
            name="Monetary Policy",
            value=f"Usage: {config.BOT_PREFIX}mp",
            inline=False
        )
        embed.add_field(
            name="Server",
            value=f"Usage: {config.BOT_PREFIX}server",
            inline=False
        )
        embed.add_field(
            name="Invite",
            value=f"Usage: {config.BOT_PREFIX}invite",
            inline=False
        )
        embed.add_field(
            name="Info",
            value=f"Usage: {config.BOT_PREFIX}info",
            inline=False
        )
        embed.add_field(
            name="Stake **(DM ONLY)**",
            value=f"Usage: {config.BOT_PREFIX}stake <Priv Key> <Address> <Validator Key> <Reward Address>",
            inline=False
        )
        embed.add_field(
            name="Transaction Explorer",
            value=f"Usage: {config.BOT_PREFIX}gettx <txn hash/id>",
            inline=False
        )
        embed.add_field(
            name="DEX Aggregator",
            value=f"Usage: {config.BOT_PREFIX}buy or {config.BOT_PREFIX}sell <base currency> <quote currency>",
            inline=False
        )
        embed.add_field(
            name="pDex Live Net Stats",
            value=f"Usage: {config.BOT_PREFIX}pdex",
            inline=False
        )
        embed.add_field(
            name="Live Blockchain Stats",
            value=f"Usage: {config.BOT_PREFIX}blockchain",
            inline=False
        )
        embed.add_field(
            name="Updated Marketcap",
            value=f"Usage: {config.BOT_PREFIX}marketcap",
            inline=False
        )
        embed.add_field(
            name="Help",
            value=f"Usage: {config.BOT_PREFIX}help",
            inline=False
        )
        await context.send(embed=embed)

def setup(bot):
    bot.add_cog(Help(bot))
