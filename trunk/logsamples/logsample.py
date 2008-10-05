# Logging
import logging
import logging.config
LOGFILE = 'loggin.conf'
logging.config.fileConfig(LOGFILE)
logger = logging.getLogger('apsl')

if __name__== "__main__":
    print "logging ..."
    logger.info('This is an info message')
    logger.debug('this is a debug message')
    logger.error('this is an error message')
    logger.warn('you have been warned')
