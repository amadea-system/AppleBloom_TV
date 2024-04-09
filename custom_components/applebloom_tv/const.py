"""Constants for applebloom_tv."""
from logging import Logger, getLogger

LOGGER: Logger = getLogger(__package__)

NAME = "AppleBloom TV"
DOMAIN = "applebloom_tv"
VERSION = "0.0.0"
ATTRIBUTION = "Data provided by http://jsonplaceholder.typicode.com/"

## -- From Apple TV Integration Code -- ##
CONF_CREDENTIALS = "credentials"
CONF_IDENTIFIERS = "identifiers"

CONF_START_OFF = "start_off"
