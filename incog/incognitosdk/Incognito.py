from .Connections import *
from .Utilities import *
import copy


class Incognito:
    def __init__(self, config=None):
        self._config = Incognito.Config() if config is None else config

        if self._config.WsUrl is None:
            self._websocket = None
        else:
            self._websocket = WebSocket(self._config.WsUrl)
            self._websocket.open()

        self._rpc = Rpc(url=self._config.RpcUrl)

        self.Public = Incognito.Public(self)
        self.Private = Incognito.Private(self)

    def destroy(self):
        if self._websocket is not None:
            self._websocket.close()

    # Do not use to modify configuration; it won't have any effect on configuration
    # To change configuration, you should recreate an Incognito object
    def get_config(self):
        return copy.deepcopy(self._config)

    class Config:
        def __init__(self):
            self.RpcUrl = "https://community-fullnode.incognito.org/"
            self.WsUrl = "ws://fullnode.incognito.best:19334"
            self.TokenListUrl = "https://api.incognito.org/ptoken/list"

    class Public:
        def __init__(self, incognito_instance):
            self._ii = incognito_instance
            self._rpc = self._ii._rpc
            self._websocket = self._ii._websocket
            self._config = self._ii._config

            self.TokenDict = {}
            # This updates TokenDict object as a side effect too.
            self.TokenList = self.refresh_token_list()

        def get_beacon_height(self):
            return self._rpc. \
                with_method('getblockchaininfo'). \
                with_params([]).execute().data()['Result']['BestBlocks']['-1']['Height']

        def get_blockchain_info(self):
            """Get the blockchain info"""
            return self._rpc. \
                with_method('getblockchaininfo'). \
                with_params([]).execute()

        def get_blocks(self, last_block_count, shard_id):
            return self._rpc. \
                with_method('getblocks'). \
                with_params([last_block_count, shard_id]). \
                execute()

        def get_mem_pool(self):
            return self._rpc. \
                with_method("getmempoolinfo"). \
                with_params([]). \
                execute()

        def get_pde_inst(self, beacon_height):
            return self._rpc. \
                with_method("extractpdeinstsfrombeaconblock"). \
                with_params([{"BeaconHeight": beacon_height}]). \
                execute()

        def get_pde_state(self, beacon_height):
            return self._rpc. \
                with_method("getpdestate"). \
                with_params([{"BeaconHeight": beacon_height}]). \
                execute()

        def list_privacy_custom_token(self):
            return self._rpc. \
                with_method("listprivacycustomtoken"). \
                with_params([]). \
                execute()

        def get_privacy_custom_token(self, token_id):
            return self._rpc. \
                with_method("getprivacycustomtoken"). \
                with_params([token_id]). \
                execute()

        def get_total_staker(self):
            return self._rpc. \
                with_method('gettotalstaker'). \
                with_params([]).execute().data()['Result']['TotalStaker']

        def get_trade_response(self, tx_id):
            return self._rpc. \
                with_method("getpdetradestatus"). \
                with_params([{"TxRequestIDStr": tx_id}]). \
                execute()

        def get_tx_by_hash(self, tx_id):
            return self._rpc. \
                with_method("gettransactionbyhash"). \
                with_params([tx_id]). \
                execute()

        def refresh_token_list(self):
            self.TokenList = requests.get(self._config.TokenListUrl)

            self.TokenDict = {x['TokenID']: x for x in self.TokenList.json()['Result']}
            self.TokenDict.update({PRV_ID: {'Symbol': 'PRV', 'PSymbol': 'PRV', 'PDecimals': 9}})

            return self.TokenList

        def subscribe(self, subscriptionType, params, handler):
            return self._websocket.subscribe(subscriptionType, params, handler)

    class Private:
        def __init__(self, incognito_instance):
            self._ii = incognito_instance
            self._rpc = self._ii._rpc
            self._websocket = self._ii._websocket
            self._config = self._ii._config

        def send_prv(self, sender_private_key, receiver_payment_address, prv_amount, fee=-1, privacy=1):
            """
            3rd param: -1 => auto estimate fee; >0 => fee * transaction size (KB)
            4th param: 0 => no privacy ; 1 => privacy
            """
            return self._rpc. \
                with_method("createandsendtransaction"). \
                with_params(
                [sender_private_key,
                 {receiver_payment_address: coin(prv_amount, self._ii.Public.TokenDict[PRV_ID]['PDecimals'])},
                 fee, privacy]). \
                execute()

        def send_token(self, sender_private_key, receiver_payment_address, token_id,
                       token_amount, prv_amount=0, prv_fee=-1, token_fee=0, prv_privacy=1,
                       token_privacy=1):
            """
            Can be use to send not only custom token but also PRV, can also send both at the same time
            :param sender_private_key:
            :param receiver_payment_address:
            :param token_id:
            :param token_amount:
            :param prv_amount: amount of prv to be sent
            :param prv_fee: using prv to pay for fee
            :param token_fee: using custom token to pay for fee
            :param prv_privacy:
            :param token_privacy:
            :return: Response Object
            """
            param = [sender_private_key]
            if prv_amount == 0:
                param.append(None)
            else:
                param.append(
                    {receiver_payment_address: coin(prv_amount, self._ii.Public.TokenDict[PRV_ID]['PDecimals'])})

            param.extend([prv_fee,
                          prv_privacy,
                          {
                              "Privacy": True,
                              "TokenID": token_id,
                              "TokenName": "",
                              "TokenSymbol": "",
                              "TokenTxType": 1,
                              "TokenAmount": 0,
                              "TokenReceivers": {
                                  receiver_payment_address: coin(token_amount,
                                                                 self._ii.Public.TokenDict[token_id]['PDecimals'])
                              },
                              "TokenFee": token_fee
                          },
                          "", token_privacy])
            return self._rpc. \
                with_method("createandsendprivacycustomtokentransaction"). \
                with_params(param). \
                execute()

        def get_balance(self, private_key):
            return self._rpc. \
                with_method("getbalancebyprivatekey"). \
                with_params([private_key]). \
                execute()

        def list_custom_token_balance(self, private_key):
            return self._rpc. \
                with_method("getlistprivacycustomtokenbalance"). \
                with_params([private_key]). \
                execute()

        def trade_prv(self, private_key, payment_address, amount_to_sell, token_id_to_buy, min_amount_to_buy,
                      trading_fee=0):
            return self._rpc. \
                with_method("createandsendtxwithprvtradereq"). \
                with_params([private_key,
                             {
                                 BURNING_ADDRESS: coin(amount_to_sell, self._ii.Public.TokenDict[PRV_ID]['PDecimals'])
                             }, -1, -1,
                             {
                                 "TokenIDToBuyStr": token_id_to_buy,
                                 "TokenIDToSellStr": PRV_ID,
                                 "SellAmount": coin(amount_to_sell, self._ii.Public.TokenDict[PRV_ID]['PDecimals']),
                                 "MinAcceptableAmount": coin(min_amount_to_buy,
                                                             self._ii.Public.TokenDict[token_id_to_buy]['PDecimals']),
                                 "TraderAddressStr": payment_address,
                                 "TradingFee": trading_fee
                             }
                             ]). \
                execute()

        def trade_prv_cross(self, private_key, payment_address, amount_to_sell, token_id_to_buy, trading_fee,
                            acceptable_amount=1,
                            burn_amount=None):
            if burn_amount is None:
                burn_amount = amount_to_sell + trading_fee
            return self._rpc.with_method('createandsendtxwithprvcrosspooltradereq').with_params([
                private_key,
                {
                    BURNING_ADDRESS: str(coin(burn_amount, self._ii.Public.TokenDict[PRV_ID]['PDecimals']))
                }, -1, -1,
                {
                    "TokenIDToBuyStr": token_id_to_buy,
                    "TokenIDToSellStr": PRV_ID,
                    "SellAmount": str(coin(amount_to_sell, self._ii.Public.TokenDict[PRV_ID]['PDecimals'])),
                    "MinAcceptableAmount": str(coin(acceptable_amount,
                                                    self._ii.Public.TokenDict[token_id_to_buy]['PDecimals'])),
                    "TradingFee": str(trading_fee),
                    "TraderAddressStr": payment_address
                }
            ]).execute()

        def trade_token(self, private_key, payment_address, token_id_to_sell, amount_to_sell, token_id_to_buy,
                        min_amount_to_buy, trading_fee=0):
            total_amount = amount_to_sell + trading_fee
            return self._rpc. \
                with_method("createandsendtxwithptokentradereq"). \
                with_params([private_key,
                             None,
                             2,
                             -1,
                             {
                                 "Privacy": True,
                                 "TokenID": token_id_to_sell,
                                 "TokenTxType": 1,
                                 "TokenName": "",
                                 "TokenSymbol": "",
                                 "TokenAmount": coin(total_amount,
                                                     self._ii.Public.TokenDict[token_id_to_sell]['PDecimals']),
                                 "TokenReceivers": {
                                     BURNING_ADDRESS: coin(total_amount,
                                                           self._ii.Public.TokenDict[token_id_to_sell]['PDecimals'])
                                 },
                                 "TokenFee": 0,

                                 "TokenIDToBuyStr": token_id_to_buy,
                                 "TokenIDToSellStr": token_id_to_sell,
                                 "SellAmount": coin(amount_to_sell,
                                                    self._ii.Public.TokenDict[token_id_to_sell]['PDecimals']),
                                 "MinAcceptableAmount": coin(min_amount_to_buy,
                                                             self._ii.Public.TokenDict[token_id_to_buy]['PDecimals']),
                                 "TradingFee": trading_fee,
                                 "TraderAddressStr":
                                     payment_address
                             },
                             "",
                             0
                             ]). \
                execute()

        # here, payment address is the address belonging to the first parameter (private_key). until simplification,
        # it will be kept.
        def trade_token_cross(self, private_key, payment_address, token_id_to_sell, amount_to_sell, token_id_to_buy,
                              min_acceptable_amount=1, trading_fee=0):
            return self._rpc.with_method('createandsendtxwithptokencrosspooltradereq').with_params([
                private_key,
                {
                    BURNING_ADDRESS: str(trading_fee)
                }, -1, 0,
                {
                    "Privacy": True,
                    "TokenID": token_id_to_sell,
                    "TokenTxType": 1,
                    "TokenName": "",
                    "TokenSymbol": "",
                    "TokenAmount": str(coin(amount_to_sell,
                                            self._ii.Public.TokenDict[token_id_to_sell]['PDecimals'])),
                    "TokenReceivers": {
                        BURNING_ADDRESS: str(coin(amount_to_sell,
                                                  self._ii.Public.TokenDict[token_id_to_sell]['PDecimals'])),
                    },
                    "TokenFee": "0",
                    "TokenIDToBuyStr": token_id_to_buy,
                    "TokenIDToSellStr": token_id_to_sell,
                    "SellAmount": str(coin(amount_to_sell,
                                           self._ii.Public.TokenDict[token_id_to_sell]['PDecimals'])),
                    "MinAcceptableAmount": str(coin(min_acceptable_amount,
                                                    self._ii.Public.TokenDict[token_id_to_buy]['PDecimals'])),
                    "TradingFee": str(trading_fee),
                    "TraderAddressStr": payment_address
                }, "", 0
            ]).execute()

        def create_and_send_staking_transaction(self, candidate_private_key, candidate_payment_key,
                                                candidate_validator_key,
                                                reward_receiver_payment_key):
            return self._rpc.with_method("createandsendstakingtransaction"). \
                with_params([candidate_private_key,
                             {
                                 BURNING_ADDRESS: 1750000000000},
                             2, 0,
                             {
                                 "StakingType": 63,
                                 "CandidatePaymentAddress": candidate_payment_key,
                                 "PrivateSeed": candidate_validator_key,
                                 "RewardReceiverPaymentAddress": reward_receiver_payment_key,
                                 "AutoReStaking": True
                             }
                             ]).execute()
