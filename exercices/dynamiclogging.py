import logging, logging.config
import json
import sys

def configure_logging(verbose: bool) ->logging.Logger:
    if not isinstance(verbose, bool):
        raise TypeError("verbose should be True or False")
    config = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'simple': {
                'format': '%(levelname)s: %(message)s'
            }
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'simple',
                'stream': 'ext://sys.stdout'
            }
        },
        'loggers': {
            'root': {
                'level': 'INFO',
                'handlers': ['console']
            }
        }
    }

    if verbose:
        config["loggers"]["root"]["level"] = "DEBUG"
    
    logging.config.dictConfig(config)
    logger = logging.getLogger()
    return logger

if __name__ == "__main__":
    log = configure_logging("dede")
    log.debug("Testing debug...")