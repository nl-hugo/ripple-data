import json
import logging
import logging.config

from .ripple_api import RippleAPI
from .accounts import RippleAccount
from .currencies import RippleCurrency
from .exchanges import RippleExchange
from .gateways import RippleGateway
from .network import RippleNetwork

# Initialize logging
with open("logging.json", "r", encoding="utf-8") as fd:
    config = json.load(fd)
    logging.config.dictConfig(config)

logger = logging.getLogger(__name__)
logger.info('Initialized ripple_data')
