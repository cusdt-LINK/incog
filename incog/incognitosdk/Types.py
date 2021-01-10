class SubscriptionType:
    """
    Enumeration of Websocket subscriptions
    """
    NewShardBlock = "subcribenewshardblock"
    PendingTransaction = "subcribependingtransaction"
    NewBeaconBlock = "subcribenewbeaconblock"


class TransactionType:
    Shielding = 25
    Erc20Shielding = 81
    Trade = 206
    Unstake = 41
    Stake = 63
    AddLiquidity = 90
    RemoveLiquidity = 94


class TradeStatus:
    Accepted = "xPoolTradeAccepted"
