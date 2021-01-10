from discord.ext import commands
import asyncio
import requests
import json
import logging
import os, sys, discord, platform, random, aiohttp, json
if not os.path.isfile("config.py"):
    sys.exit("'config.py' not found! Please add it and try again.")
else:
    import config


currency_symbol_dict = {'USD': '$', 'BTC': '₿', 'ETH': 'Ξ', 'LTC': 'Ł', 'EUR': '€', 'JPY': '¥', 'RUB': '₽',
                        'AED': 'د.إ', 'BDT': '৳', 'BHD': 'BD', 'CNY': '¥', 'CZK': 'Kč', 'DKK': 'kr.', 'GBP': '£',
                        'HUF': 'Ft', 'IDR': 'Rp', 'ILS': '₪', 'INR': '₹', 'KRW': '₩', 'KWD': 'KD', 'LKR': 'රු',
                        'MMK': 'K', 'MYR': 'RM', 'NOK': 'kr', 'PHP': '₱', 'PKR': 'Rs', 'PLN': 'zł', 'SAR': 'SR',
                        'SEK': 'kr', 'THB': '฿', 'TRY': '₺', 'VEF': 'Bs.', 'VND': '₫', 'ZAR': 'R', 'XDR': 'SDR',
                        'XAG': 'XAG', 'XAU': 'XAU'}


class CryptoTicker(commands.Cog, name="cryptoticker"):
    def __init__(self, bot):
        self.bot = bot
        self.base_currency = config.BASE_CURRENCY
        self.url = config.URL
        self.coin_list = requests.get(config.COIN_LIST).json()
        self.supported_currencies = requests.get(config.SUPPORTED_CURRENCIES).json()
        self.this_extension = 'cogs.cryptoticker'

    @commands.command()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            if error.param.name == 'new_base':
                await ctx.send(f'```BASE_CURRENCY: {self.base_currency}\n'
                               f'command usage: basecurrency <currency>```')
                logging.info(f'[CryptoTicker Prompted]: {ctx.message.author}: basecurrency')
                logging.info('[CryptoTicker Returned]: basecurrency usage message')

        if isinstance(error, commands.MissingRequiredArgument):
            if error.param.name == 'ticker':
                await ctx.send('```command usage: price <currency> [base_currency]```')
                logging.info(f'[CryptoTicker Prompted]: {ctx.message.author}: price')
                logging.info('[CryptoTicker Returned]: price usage message')

    @commands.command(pass_context=True)
    async def basecurrency(self, ctx, new_base):
        logging.info(f'[CryptoTicker Prompted]: {ctx.message.author}: basecurrency {new_base}')

        new_base = new_base.lower()
        if new_base == self.base_currency:
            async with ctx.typing():
                await asyncio.sleep(1)
                await ctx.send(f'Default base currency is already set to {new_base.upper()}')
                logging.info(f'[CryptoTicker Returned]: Default base currency is already set to {new_base.upper()}')
                await ctx.message.add_reaction('\N{THUMBS UP SIGN}')
        elif new_base in self.supported_currencies:
            try:
                self.bot.config["CRYPTOTICKER"]["BASE_CURRENCY"] = new_base
                with open(self.bot.config_path, 'w') as updated_config:
                    json.dump(self.bot.config, updated_config, indent=2, sort_keys=False, ensure_ascii=True)

                self.bot.unload_extension(self.this_extension)
                self.bot.load_extension(self.this_extension)

                async with ctx.typing():
                    await asyncio.sleep(1)
                    await ctx.send(f'Changing default base currency to {new_base.upper()}')
                    logging.info(f'[CryptoTicker Reload]: Config update - BASE_CURRENCY is now {new_base.upper()}')
                    await ctx.message.add_reaction('\N{THUMBS UP SIGN}')

            except Exception as error:
                async with ctx.typing():
                    await asyncio.sleep(1)
                    await ctx.send(f'basecurrency command returned with error: {error}')
                    logging.info(f'[CryptoTicker Error]: basecurrency command returned with error: {error}')
                    await ctx.message.add_reaction('\N{THUMBS DOWN SIGN}')
        else:
            async with ctx.typing():
                await asyncio.sleep(1)
                await ctx.send(f'CryptoTicker Error: {new_base.upper()} is not a supported currency')
                logging.info(f'[CryptoTicker Error]: {new_base.upper()} is not a supported currency')
                await ctx.message.add_reaction('\N{THUMBS DOWN SIGN}')

    @commands.command(pass_context=True)
    async def price(self, ctx, ticker, base=None):
        if base is None:
            base = self.base_currency

        logging.info(f'[CryptoTicker Prompted]: {ctx.message.author}: price {ticker} {base}')

        currency_symbol = currency_symbol_dict.get(base.upper(), '$')
        ticker = ticker.lower()
        base = base.lower()

        if base in self.supported_currencies:
            try:
                for coin in self.coin_list:
                    if ticker == coin['symbol']:
                        ticker = coin['id']

                response = requests.get(self.url + ticker + '&vs_currency=' + base).json()
                symbol = response[0]['symbol']
                current_price = response[0]['current_price']
                formatted_price = f'{current_price:,.2f}'
                if formatted_price.startswith('0'):
                    formatted_price = f'{current_price:,.4f}'
                if base == 'btc':
                    formatted_price = f'{current_price:,.8f}'

                async with ctx.typing():
                    await asyncio.sleep(1)
                    await ctx.send(f'{symbol.upper()}/{base.upper()}: {currency_symbol}{formatted_price}')
                    logging.info(f'[CryptoTicker Returned]: {symbol.upper()}/{base.upper()}:'
                                 f' {currency_symbol}{formatted_price}')
                    await ctx.message.add_reaction('\N{THUMBS UP SIGN}')

            except Exception as error:
                async with ctx.typing():
                    await asyncio.sleep(1)
                    await ctx.send(f'price command returned with error: {error}')
                    logging.info(f'[CryptoTicker Error]: price command returned with error: {error}')
                    await ctx.message.add_reaction('\N{THUMBS DOWN SIGN}')
        else:
            async with ctx.typing():
                await asyncio.sleep(1)
                await ctx.send(f'CryptoTicker Error: {base.upper()} is not a supported currency')
                logging.info(f'[CryptoTicker Error]: User: {ctx.message.author} Error: {base}'
                             f' is not a supported currency')
                await ctx.message.add_reaction('\N{THUMBS DOWN SIGN}')


def setup(bot):
    bot.add_cog(CryptoTicker(bot))
