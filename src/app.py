import sys

from flask import Flask

import configuration as config
import logger as logger

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def handle_request():
    pass


def runserver(port=config.SERVER_PORT):
    app.run(host=config.SERVER_HOST, port=port)


if __name__ == '__main__':
    try:
        if len(sys.argv) > 1:
            server_port = int(sys.argv[1])
            logger.log_info('starting server on custom port', server_port)
            runserver(server_port)
        else:
            logger.log_info('starting server on default port')
            runserver()
    except KeyboardInterrupt:
        exit(0)
