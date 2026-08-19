import logging

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s in %(filename)s: %(message)s - (Line: %(lineno)d)')
logger = logging.getLogger(__name__)
