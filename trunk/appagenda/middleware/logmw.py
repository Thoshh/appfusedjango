from datetime import datetime
import logging

logger = None

class LoggingMiddleware(object):
    """
    Basic logging middleware. If settings.LOG_ENABLED is set, adds a logger
    instance as request.logger

    Logging can be used as request.logger.[debug, info, warning, error and critical]

    Ex: request.logger.info("This is an info message")

    Requires LOG_ENABLED settings value.

    If settings.LOG_ENABLED is True, requires LOG_FILE value.

    LOG_NAME is optional, and will specify a name for this logger
    instance (not shown in default format string)
    """

    def process_request(self, request):
        from django.conf import settings
        enabled = getattr(settings, 'LOG_ENABLED', False)
        logfile = getattr(settings, 'LOG_FILE', None)
        console = getattr(settings, 'LOG_TO_CONSOLE',True)
        if not enabled or not logfile:
            return

        global logger
        if logger is None:
            logging.basicConfig(
                level=logging.DEBUG,
                format='%(asctime)s - %(levelname)s - %(message)s',
                datefmt='%Y-%m-%d %X',
                filename=settings.LOG_FILE,
                filemode='a'
            )
            # define a Handler which writes INFO messages or higher to the sys.stderr
            console = logging.StreamHandler()
            console.setLevel(logging.DEBUG)
            # set a format which is simpler for console use
            formatter = logging.Formatter('%(asctime)s - %(name)-12s: %(levelname)-8s %(message)s')
            # tell the handler to use this format
            console.setFormatter(formatter)
            # add the handler to the root logger
            logging.getLogger('').addHandler(console)
            logger = logging.getLogger(getattr(settings, 'LOG_NAME', 'django'))
            logger.setLevel(logging.DEBUG)

        request.logger = logger
