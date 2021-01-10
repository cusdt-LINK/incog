import os, sys, discord, platform, random, aiohttp, json, asyncio
from discord.ext import commands
from cmd import Cmd
from incognitosdk.Incognito import *
if not os.path.isfile("config.py"):
    sys.exit("'config.py' not found! Please add it and try again.")
else:
    import config

class rpc(commands.Cog, name="rpc"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="stake")
    @commands.dm_only()
    async def stake(self, ctx, candidate_private_key, candidate_payment_key, candidate_validator_key, reward_receiver_payment_key):
        config = Incognito.Config()
        config.WsUrl = None  # Do not open websocket connection
        incognitoApi = Incognito(config)
        raw_response = incognitoApi.Private.create_and_send_staking_transaction(candidate_private_key, candidate_payment_key, candidate_validator_key, reward_receiver_payment_key)
        print(raw_response)
        with open(f'result.text', 'w') as outfile:
            json.dump(raw_response.data(), outfile);
        with open("/root/incog/result.text", encoding='utf-8') as data_file:
            data = json.load(data_file)
        status = (data["Error"]["Message"])
        result = (data["Result"])
        code = (data["Error"]["Code"])
        embed = discord.Embed(
            title="**Staking Status:**",
            description="Incognito Chain",
            color=0x00FF00
        )
        embed.set_author(
            name="Incog Scan",
            url="https://discord.gg/R4QyyMASJK",
            icon_url="https://i.ibb.co/9pfnZ1C/61460-A48-93-A4-40-BF-86-AD-4-E7593-EB1-CFD.png"
        )
        embed.set_thumbnail(
            url="https://i.ibb.co/bvzRJb8/C5-EA58-A2-6422-4500-AF40-D5-D6-A383-AFCB.png"
        )
        embed.add_field(
            name="**Result:**",
            value=f'{result}',
            inline=False
        )
        embed.add_field(
            name="**Message:**",
            value=f'Message: {status}',
            inline=False
        )
        embed.set_footer(
            text=f'Code: {code}',
        )
        await ctx.send(embed=embed)
        
    @commands.command(name="gettx")
    async def gettx(self, ctx, tx_id):
        config = Incognito.Config()
        config.WsUrl = None  # Do not open websocket connection
        incognitoApi = Incognito(config)
        raw_response = incognitoApi.Public.get_tx_by_hash(tx_id)
        print(raw_response)
        with open(f'result.text', 'w') as outfile:
            json.dump(raw_response.data(), outfile);
        with open("/root/incog/result.text", encoding='utf-8') as data_file:
            data = json.load(data_file)
        status = (data["Result"])
        result = (data["Result"]["BlockHeight"])
        locktime = (data["Result"]["LockTime"])
        txsize = (data["Result"]["TxSize"])
        hashid = (data["Result"]["Hash"])
        shardid = (data["Result"]["ShardID"])
        success = (data["Result"]["IsInBlock"])
        typeid = (data["Result"]["Type"])
        fee = (data["Result"]["Fee"])
        image = (data["Result"]["Image"])
        embed = discord.Embed(
            title="**Transaction Details:**",
            description="Incognito Chain",
            color=0x00FF00
        )
        embed.set_author(
            name="Incog Scan",
            url="https://discord.gg/R4QyyMASJK",
            icon_url="https://i.ibb.co/9pfnZ1C/61460-A48-93-A4-40-BF-86-AD-4-E7593-EB1-CFD.png"
        )
        embed.set_thumbnail(
            url="https://i.ibb.co/4MM4zc6/9-DB06-FAC-D50-A-4873-8-A3-B-27-EF7796-F164.png"
        )
        embed.add_field(
            name="**Transaction Success:**",
            value=f'{success}',
            inline=False
        )
        embed.add_field(
            name="**Block Height:**",
            value=f'{result}', 
            inline=False
        )
        embed.add_field(
            name="**Timestamp:**",
            value=f'{locktime}',
            inline=False
        )
        embed.add_field(
            name="**Tx ID:**",
            value=f'{hashid}',
            inline=False
        )
        embed.add_field(
            name="**Shard ID:**",
            value=f'{shardid}',
            inline=False
        )
        embed.add_field(
            name="**Tx Size:**",
            value=f'{txsize}kb',
            inline=False
        )
        embed.add_field(
            name="**Tx Type:**",
            value=f'{typeid}',
            inline=False
        )
        embed.add_field(
            name="**Tx Fee:**",
            value=f'0.00000000{fee} PRV',
            inline=False
        )
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(rpc(bot))
