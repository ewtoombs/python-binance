SYMBOL_TYPE_SPOT = 'SPOT'

ORDER_STATUS_NEW = 'NEW'
ORDER_STATUS_PARTIALLY_FILLED = 'PARTIALLY_FILLED'
ORDER_STATUS_FILLED = 'FILLED'
ORDER_STATUS_CANCELED = 'CANCELED'
ORDER_STATUS_PENDING_CANCEL = 'PENDING_CANCEL'
ORDER_STATUS_REJECTED = 'REJECTED'
ORDER_STATUS_EXPIRED = 'EXPIRED'

KLINE_INTERVAL_1MINUTE = '1m'
KLINE_INTERVAL_3MINUTE = '3m'
KLINE_INTERVAL_5MINUTE = '5m'
KLINE_INTERVAL_15MINUTE = '15m'
KLINE_INTERVAL_30MINUTE = '30m'
KLINE_INTERVAL_1HOUR = '1h'
KLINE_INTERVAL_2HOUR = '2h'
KLINE_INTERVAL_4HOUR = '4h'
KLINE_INTERVAL_6HOUR = '6h'
KLINE_INTERVAL_8HOUR = '8h'
KLINE_INTERVAL_12HOUR = '12h'
KLINE_INTERVAL_1DAY = '1d'
KLINE_INTERVAL_3DAY = '3d'
KLINE_INTERVAL_1WEEK = '1w'
KLINE_INTERVAL_1MONTH = '1M'

SIDE_BUY = 'BUY'
SIDE_SELL = 'SELL'

ORDER_TYPE_LIMIT = 'LIMIT'
ORDER_TYPE_MARKET = 'MARKET'
ORDER_TYPE_STOP_LOSS = 'STOP_LOSS'
ORDER_TYPE_STOP_LOSS_LIMIT = 'STOP_LOSS_LIMIT'
ORDER_TYPE_TAKE_PROFIT = 'TAKE_PROFIT'
ORDER_TYPE_TAKE_PROFIT_LIMIT = 'TAKE_PROFIT_LIMIT'
ORDER_TYPE_LIMIT_MAKER = 'LIMIT_MAKER'

TIME_IN_FORCE_GTC = 'GTC'  # Good till cancelled
TIME_IN_FORCE_IOC = 'IOC'  # Immediate or cancel
TIME_IN_FORCE_FOK = 'FOK'  # Fill or kill

ORDER_RESP_TYPE_ACK = 'ACK'
ORDER_RESP_TYPE_RESULT = 'RESULT'
ORDER_RESP_TYPE_FULL = 'FULL'

WS_DEPTH_5 = '5'
WS_DEPTH_10 = '10'
WS_DEPTH_20 = '20'

# For munching upon the data returned by Client.aggregate_trades() and
# websockets.aggregate_trades().
AGG_ID             = 'a'
AGG_PRICE          = 'p'
AGG_QUANTITY       = 'q'
AGG_FIRST_TRADE_ID = 'f'
AGG_LAST_TRADE_ID  = 'l'
AGG_TIME           = 'T'
AGG_BUYER_MAKES    = 'm'
AGG_BEST_MATCH     = 'M'

# Ditto, websockets.trades().
TRADE_ID              = "t"
TRADE_PRICE           = "p"
TRADE_QUANTITY        = "q"
TRADE_BUYER_ORDER_ID  = "b"
TRADE_SELLER_ORDER_ID = "a"
TRADE_TIME            = "T"
TRADE_BUYER_MAKES     = "m"
TRADE_IGNORE          = "M"

# Common keys in many websocket events.
WS_EVENT_TYPE = 'e'
WS_EVENT_TIME = 'E'
WS_SYMBOL = 's'

# error codes
# 10xx - General Server or Network issues
E_UNKNOWN = -1000
E_DISCONNECTED = -1001
E_UNAUTHORIZED = -1002
E_TOO_MANY_REQUESTS = -1003
E_UNEXPECTED_RESP = -1006
E_TIMEOUT = -1007
E_ERROR_MSG_RECEIVED = -1010
E_INVALID_MESSAGE = -1013
E_UNKNOWN_ORDER_COMPOSITION = -1014
E_TOO_MANY_ORDERS = -1015
E_SERVICE_SHUTTING_DOWN = -1016
E_UNSUPPORTED_OPERATION = -1020
E_INVALID_TIMESTAMP = -1021
E_INVALID_SIGNATURE = -1022

# 11xx - Request issues
E_ILLEGAL_CHARS = -1100
E_TOO_MANY_PARAMETERS = -1101
E_MANDATORY_PARAM_EMPTY_OR_MALFORMED = -1102
E_UNKNOWN_PARAM = -1103
E_UNREAD_PARAMETERS = -1104
E_PARAM_EMPTY = -1105
E_PARAM_NOT_REQUIRED = -1106
E_NO_DEPTH = -1112
E_TIF_NOT_REQUIRED = -1114
E_INVALID_TIF = -1115
E_INVALID_ORDER_TYPE = -1116
E_INVALID_SIDE = -1117
E_EMPTY_NEW_CL_ORD_ID = -1118
E_EMPTY_ORG_CL_ORD_ID = -1119
E_BAD_INTERVAL = -1120
E_BAD_SYMBOL = -1121
E_INVALID_LISTEN_KEY = -1125
E_MORE_THAN_XX_HOURS = -1127
E_OPTIONAL_PARAMS_BAD_COMBO = -1128
E_INVALID_PARAMETER = -1130

# 20xx - Processing Issues
E_BAD_API_ID = -2008
E_DUPLICATE_API_KEY_DESC = -2009
E_NEW_ORDER_REJECTED = -2010
E_CANCEL_REJECTED = -2011
E_CANCEL_ALL_FAIL = -2012
E_NO_SUCH_ORDER = -2013
E_BAD_API_KEY_FMT = -2014
E_REJECTED_MBX_KEY = -2015

# Messages for -1010 ERROR_MSG_RECEIVED, -2010 NEW_ORDER_REJECTED, and -2011
# CANCEL_REJECTED
EMSG_ACTION_DISABLED = 'This action disabled is on this account.'
EMSG_BALANCE = 'Account has insufficient balance for requested action.'
EMSG_CANCEL_INVALID = 'Cancel order is invalid. Check origClOrdId and orderId.'
EMSG_CLOSED = 'Market is closed.'
EMSG_DUPLICATE = 'Duplicate order sent.'
EMSG_ICEBERGQTY = 'IcebergQty exceeds QTY.'
EMSG_NO_ICEBERG = 'Iceberg orders are not supported for this symbol.'
EMSG_NO_MARKET = 'Market orders are not supported for this symbol.'
EMSG_NO_STOP_LOSS = 'Stop loss orders are not supported for this symbol.'
EMSG_NO_STOP_LOSS_LIMIT = \
        'Stop loss limit orders are not supported for this symbol.'
EMSG_NO_TAKE_PROFIT = 'Take profit orders are not supported for this symbol.'
EMSG_NO_TAKE_PROFIT_LIMIT = \
        'Take profit limit orders are not supported for this symbol.'
EMSG_ORDER_COMBO = 'Unsupported order combination'
EMSG_PRICE_QTY = 'Price * QTY is zero or less.'
EMSG_WOULD_TAKE = 'Order would immediately match and take.'
EMSG_WOULD_TRIGGER = 'Order would trigger immediately.'
# Undocumented, but happen often.
EMSG_NO_TRADES = 'Rest API trading is not enabled.'
EMSG_UNKNOWN_ORDER = 'UNKNOWN_ORDER'
