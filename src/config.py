import os, logging

DEBUG = True
HOST = os.getenv('HOST', '0.0.0.0')
PORT = int(os.getenv('PORT', '5000'))

DB_HOST = os.getenv('DB_PORT_5432_TCP_ADDR', 'localhost')
DB_PORT = os.getenv('DB_PORT_5432_TCP_PORT', '5432')
DB_URI = 'postgresql://postgres@'+DB_HOST+':'+DB_PORT+'/postgres'

logging.basicConfig(
    filename='error.log',
    level=logging.DEBUG,
    format='%(levelname)s: %(asctime)s pid:%(process)s module:%(module)s %(message)s',
    datefmt='%d/%m/%y %H:%M:%S',
)

# If the file "local_config.py" exists, load it
try:
    from local_config import *
except ImportError:
    pass
