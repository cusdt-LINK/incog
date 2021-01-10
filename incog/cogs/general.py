import os, sys, discord, platform, random, aiohttp, json
from discord.ext import commands
if not os.path.isfile("config.py"):
    sys.exit("'config.py' not found! Please add it and try again.")
else:
    import config

class general(commands.Cog, name="general"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="info", aliases=["botinfo"])
    async def info(self, context):
        embed = discord.Embed(
            description="incognito",
            color=0x00FF00
        )
        embed.set_author(
            name="Bot Information"
        )
        embed.add_field(
            name="Owner:",
            value="cusdt.eth#0211",
            inline=True
        )
        embed.add_field(
            name="Python Version:",
            value=f"{platform.python_version()}",
            inline=True
        )
        embed.add_field(
            name="Prefix:",
            value=f"{config.BOT_PREFIX}",
            inline=False
        )
        embed.set_footer(
            text=f"Requested by {context.message.author}"
        )
        await context.send(embed=embed)

    @commands.command(name="serverinfo")
    async def serverinfo(self, context):
        server = context.message.guild
        roles = [x.name for x in server.roles]
        role_length = len(roles)
        if role_length > 50:
            roles = roles[:50]
            roles.append(f">>>> Displaying[50/{len(roles)}] Roles")
        roles = ", ".join(roles)
        channels = len(server.channels)
        time = str(server.created_at)
        time = time.split(" ")
        time = time[0]

        embed = discord.Embed(
            title="**Server Name:**",
            description=f"{server}",
            color=0x00FF00
        )
        embed.set_thumbnail(
            url=server.icon_url
        )
        embed.add_field(
            name="Owner",
            value=f"{server.owner}\n{server.owner.id}"
        )
        embed.add_field(
            name="Server ID",
            value=server.id
        )
        embed.add_field(
            name="Member Count",
            value=server.member_count
        )
        embed.add_field(
            name="Text/Voice Channels",
            value=f"{channels}"
        )
        embed.add_field(
            name=f"Roles ({role_length})",
            value=roles
        )
        embed.set_footer(
            text=f"Created at: {time}"
        )
        await context.send(embed=embed)

    @commands.command(name="explorer")
    async def explorer(self, context):
        embed = discord.Embed(
            color=0x00FF00
        )
        embed.add_field(
            name="Explorer",
            value="https://incscan.io",
            inline=True
        )
        embed.set_footer(
            text=f"Explorer requested by {context.message.author}"
        )
        await context.send(embed=embed)

    @commands.command(name="invite")
    async def invite(self, context):
        await context.send("I sent you a private message!")
        await context.author.send(f"Invite me by clicking here: https://discordapp.com/oauth2/authorize?&client_id={config.APPLICATION_ID}&scope=bot&permissions=8")

    @commands.command(name="server")
    async def server(self, context):
        await context.send("I sent you a private message!")
        await context.author.send("Join my discord server by clicking here: hhttps://discord.gg/R4QyyMASJK")

    @commands.command(name="community")
    async def community(self, context):
        embed = discord.Embed(
            color=0x00FF00
        )
        embed.add_field(
            name="Community",
            value="https://we.incognito.org",
            inline=True
        )
        embed.set_footer(
            text=f"Explorer requested by {context.message.author}"
        )
        await context.send(embed=embed)

    @commands.command(name="github")
    async def github(self, context):
        embed = discord.Embed(
            color=0x00FF00
        )
        embed.add_field(
            name="Github",
            value="https://github.com/incognitochain",
            inline=True
        )
        embed.set_footer(
            text=f"Github requested by {context.message.author}"
        )
        await context.send(embed=embed)

    @commands.command(name="mp")
    async def monetarypolicy(self, context):
        embed = discord.Embed(
            color=0x00FF00
        )
        embed.add_field(
            name="Monetary_Policy",
            value="Monetary policy and mining block rewards scheme in Incognito: https://we.incognito.org/t/network-incentive-privacy-prv-mining-distribution/172",
            inline=True
        )
        embed.set_footer(
            text=f"Monetary Policy requested by {context.message.author}"
        )
        await context.send(embed=embed)
        
    @commands.command(name="wallet")
    async def wallet(self, context):
        embed = discord.Embed(
            color=0x00FF00
        )
        embed.add_field(
            name="Wallet",
            value="Wallet: https://apps.apple.com/us/app/incognito-crypto-wallet/id1475631606",
            inline=True
        )
        embed.set_footer(
            text=f"Wallet requested by {context.message.author}"
        )
        await context.send(embed=embed)
        
    @commands.command(name="website")
    async def website(self, context):
        embed = discord.Embed(
            color=0x00FF00
        )
        embed.add_field(
            name="Website",
            value="Website: https://incognito.org/",
            inline=True
        )
        embed.set_footer(
            text=f"Website requested by {context.message.author}"
        )
        await context.send(embed=embed)
        
    @commands.command(name="roadmap")
    async def roadmap(self, context):
        embed = discord.Embed(
            color=0x00FF00
        )
        embed.add_field(
            name="roadmap",
            value="Roadmap: https://we.incognito.org/t/incognito-core-dev-2020-live-roadmap/552",
            inline=True
        )
        embed.set_footer(
            text=f"Roadmap requested by {context.message.author}"
        )
        await context.send(embed=embed)
        
    @commands.command(name="validators")
    async def validators(self, context):
        embed = discord.Embed(
            color=0x00FF00
        )
        embed.add_field(
            name="Validators",
            value="Validators: https://incscan.io/network/validators",
            inline=True
        )
        embed.set_footer(
            text=f"Validators requested by {context.message.author}"
        )
        await context.send(embed=embed)
        
    @commands.command(name="quest")
    async def quest(self, context):
        embed = discord.Embed(
            color=0x00FF00
        )
        embed.add_field(
            name="Quest",
            value="Join the privacy quest! https://incognito.org/quest",
            inline=True
        )
        embed.set_footer(
            text=f"Quest requested by {context.message.author}"
        )
        await context.send(embed=embed)
        
    @commands.command(name="whitepaper")
    async def whitepaper(self, context):
        embed = discord.Embed(
            color=0x00FF00
        )
        embed.add_field(
            name="Whitepaper",
            value="Wallet: https://apps.apple.com/us/app/incognito-crypto-wallet/id1475631606",
            inline=True
        )
        embed.set_footer(
            text=f"Whitepaper requested by {context.message.author}"
        )
        await context.send(embed=embed)
        
    @commands.command(name="exchange")
    async def exchange(self, context):
        embed = discord.Embed(
            color=0x00FF00
        )
        embed.add_field(
            name="Exchange",
            value="pDex: https://blog.incognito.org/how-to-trade-bitcoin-privately-with-incognito-pdex/",
            inline=True
        )
        embed.set_footer(
            text=f"Exchange requested by {context.message.author}"
        )
        await context.send(embed=embed)
        
    @commands.command(name="staking")
    async def staking(self, context):
        embed = discord.Embed(
            color=0x00FF00
        )
        embed.add_field(
            name="staking",
            value="pNode: https://we.incognito.org/t/how-to-use-1750-prv-to-stake-on-pnode/787 | Delegated: https://www.stakingrewards.com/earn/incognito |",
            inline=True
        )
        embed.set_footer(
            text=f"Staking requested by {context.message.author}"
        )
        await context.send(embed=embed)
        
    @commands.command(name="provide")
    async def provide(self, context):
        embed = discord.Embed(
            color=0x00FF00
        )
        embed.add_field(
            name="Provide",
            value="Invest in privacy. Earn anonymously: https://we.incognito.org/t/provide/4247",
            inline=True
        )
        embed.set_footer(
            text=f"Provide requested by {context.message.author}"
        )
        await context.send(embed=embed)
        
    @commands.command(name="node")
    async def node(self, context):
        embed = discord.Embed(
            color=0x00FF00
        )
        embed.add_field(
            name="pNode",
            value="pNode: https://node.incognito.org/payment.html?utm_source=pnode&utm_medium=discourse",
            inline=True
        )
        embed.set_footer(
            text=f"pNode requested by {context.message.author}"
        )
        await context.send(embed=embed)
        
    @commands.command(name="fiat")
    async def fiat(self, context):
        embed = discord.Embed(
            color=0x00FF00
        )
        embed.add_field(
            name="Fiat",
            value="Privacy focused Fiat on/off ramp: https://bit.ly/3oIfo3H",
            inline=True
        )
        embed.set_footer(
            text=f"Fiat requested by {context.message.author}"
        )
        await context.send(embed=embed)
        
    @commands.command(name="pdex")
    async def pdex(self, context):
        url = "https://api.incscan.io/pdex/overview"
        # Async HTTP request
        async with aiohttp.ClientSession() as session:
            raw_response = await session.get(url)
            response = await raw_response.text()
            response = json.loads(response)
            embed = discord.Embed(
                title=":information_source: pDex Overview",
                description=f"incognito",
                color=0x00FF00
            )
        url = "https://api.incscan.io/pdex/overview"
        async with aiohttp.ClientSession() as session:
            raw_response = await session.get(url)
            response = await raw_response.text()
            response = json.loads(response)
            embed.add_field(
            name="pDex Liquidity is:",
            value=f"${response['liquidity']}",
            inline=True
        )
        url = "https://api.incscan.io/pdex/overview"
        async with aiohttp.ClientSession() as session:
            raw_response = await session.get(url)
            response = await raw_response.text()
            response = json.loads(response)
            embed.add_field(
            name="All Time Trading Volume is:",
            value=f"${response['allTimeVolume']}",
            inline=True
        )
            embed.set_footer(
                text=f"pDex Live Market Stats"
        )
            await context.send(embed=embed)
            
    @commands.command(name="marketcap")
    async def marketcap(self, context):
        url = "https://api.incscan.io/privacy-coin/overview"
        # Async HTTP request
        async with aiohttp.ClientSession() as session:
            raw_response = await session.get(url)
            response = await raw_response.text()
            response = json.loads(response)
            embed = discord.Embed(
                title=":information_source: PRV Market Cap",
                description=f"${response['marketCap']}",
                color=0x00FF00
            )
            embed.set_footer(
                text=f"Live Market Stats"
        )
            await context.send(embed=embed)
            
    @commands.command(name="blockchain")
    async def blockchain(self, context):
        url = "https://api.incscan.io/blockchain"
        # Async HTTP request
        async with aiohttp.ClientSession() as session:
            raw_response = await session.get(url)
            response = await raw_response.text()
            response = json.loads(response)
            embed = discord.Embed(
                title=":information_source: Blockchain Info",
                description=f"incognito",
                color=0x00FF00
            )
        url = "https://api.incscan.io/blockchain"
        async with aiohttp.ClientSession() as session:
            raw_response = await session.get(url)
            response = await raw_response.text()
            response = json.loads(response)
            embed.add_field(
            name="Current Height:",
            value=f"{response['beaconLastHeight']}",
            inline=True
        )
        url = "https://api.incscan.io/blockchain"
        async with aiohttp.ClientSession() as session:
            raw_response = await session.get(url)
            response = await raw_response.text()
            response = json.loads(response)
            embed.add_field(
            name="Active Shards:",
            value=f"{response['activeShards']}",
            inline=True
        )
        url = "https://api.incscan.io/blockchain"
        async with aiohttp.ClientSession() as session:
            raw_response = await session.get(url)
            response = await raw_response.text()
            response = json.loads(response)
            embed.add_field(
            name="Epoch:",
            value=f"{response['epoch']}",
            inline=True
        )
            embed.set_footer(
                text=f"Live Net Stats"
        )
            await context.send(embed=embed)   
            
    @commands.command(name="sell")
    async def selldag(self, ctx, base, quote, amount):
        base = base.upper()
        quote = quote.upper()
        amount = str(amount)
        url = "https://api-v2.dex.ag/price?from=" + base + "&to=" + quote + "&fromAmount=" + amount + "&dex=ag"
        # Async HTTP request
        async with aiohttp.ClientSession() as session:
            raw_response = await session.get(url)
            response = await raw_response.text()
            data = json.dumps(response)
            response = json.loads(response)
            bcurr = (response['pair']['base'])
            qcurr = (response['pair']['quote'])
            price = float(response['price'])
            rprice = f'{price:,.5f}'
            liquid = str(response['liquidity'])
            dex = liquid.replace('{', '').replace('}', '').replace(':', '').replace(',', '').replace('"', '').replace('uniswap', 'Uniswap').replace('uniswap_v2', 'Incognito   ').replace('kyber', 'Incognito').replace('bancor', 'Bancor').replace('sushiswap', 'Sushiswap').replace('zero_x_v2', '0x v2').replace('zero_x_v3', '0x v3').replace('oasis', 'Oasis').replace('synthetix', 'Synthetix').replace('curvefi', 'Curve').replace('curve_susd', 'Curve SUSD').replace('compound', 'Compound').replace('chai', 'Chai').replace('aave', 'Aave').replace('mstable', 'MStable')
            embed = discord.Embed(
                title=" **Inc.AG** ",
                description=f" Best DEX & Trade %:",
                color=0x00FF00
            )
            embed.set_author(
            name="Incog",
            url="https://discord.gg/R4QyyMASJK",
            icon_url="https://i.ibb.co/9pfnZ1C/61460-A48-93-A4-40-BF-86-AD-4-E7593-EB1-CFD.png"
            )
            embed.set_thumbnail(
            url="https://i.ibb.co/k2dLRKS/F21346-F8-5-D10-4790-AA3-F-2-BD8791-FE7-A8.png"
           )
            embed.add_field(
                name=f'{dex}%',
                value=f'Price: {rprice} {quote} per {base}',
                inline=False
            )
            await ctx.send(embed=embed)
            
    @commands.command(name="buy")
    async def buyag(self, ctx, base, quote, amount):
        base = base.upper()
        quote = quote.upper()
        amount = str(amount)
        url = "https://api-v2.dex.ag/price?from=" + base + "&to=" + quote + "&toAmount=" + amount + "&dex=ag"
        # Async HTTP request
        async with aiohttp.ClientSession() as session:
            raw_response = await session.get(url)
            response = await raw_response.text()
            data = json.dumps(response)
            response = json.loads(response)
            bcurr = (response['pair']['base'])
            qcurr = (response['pair']['quote'])
            price = float(response['price'])
            rprice = f'{price:,.5f}'
            liquid = str(response['liquidity'])
            dex = liquid.replace('{', '').replace('}', '').replace(':', '').replace(',', '').replace('"', '').replace('uniswap','Uniswap').replace('uniswap_v2', 'Incognito').replace('kyber', 'Incognito').replace('bancor', 'Bancor').replace('sushiswap', 'Sushiswap').replace('zero_x_v2', '0x v2').replace('zero_x_v3', '0x v3').replace('oasis', 'Oasis').replace('synthetix', 'Synthetix').replace('curvefi', 'Curve').replace('curve_susd', 'Curve SUSD').replace('compound', 'Compound').replace('chai', 'Chai').replace('aave', 'Aave').replace('mstable', 'MStable')
            embed = discord.Embed(
                title=" **Inc.AG** ",
                description=f" Best DEX & Trade %:",
                color=0x00FF00
            )
            embed.set_author(
            name="Incog",
            url="https://discord.gg/R4QyyMASJK",
            icon_url="https://i.ibb.co/9pfnZ1C/61460-A48-93-A4-40-BF-86-AD-4-E7593-EB1-CFD.png"
            )
            embed.set_thumbnail(
            url="https://i.ibb.co/k2dLRKS/F21346-F8-5-D10-4790-AA3-F-2-BD8791-FE7-A8.png"
           )
            embed.add_field(
                name=f'{dex}%',
                value=f'Price: {rprice} {base} per {quote}',
                inline=False
            )
            await ctx.send(embed=embed) 
def setup(bot):
    bot.add_cog(general(bot))
