import json
import sys

from flask import Flask, request

import configuration as config
import logger as logger
from action_types import ActionTypes
from mongo_interface import initialize_mongo, submit_action, get_results

app = Flask(__name__)

mongo_collection = None


@app.route('/submit_action', methods=['POST'])
def handle_submission():
    request_data = request.form

    for field in config.SUBMISSION_MANDATORY_REQUEST_FIELDS:
        if field not in request_data:
            error_message = 'malformed post request data, excepting field {}'.format(field)
            logger.log_error(error_message)
            return error_message, 400

    if request_data['action_type'] not in ActionTypes.list_types():
        error_message = 'malformed post request data, invalid action type {}'.format(request_data['action_type'])
        logger.log_error(error_message)
        return error_message, 400

    submission_successful = submit_action(request_data)
    if not submission_successful:
        error_message = 'registration failed for {}'.format(request_data)
        logger.log_error(error_message)
        return error_message, 400

    return "done", 200


@app.route('/query', methods=['GET'])
def handle_query():
    request_data = request.form

    # filter=filter, projection=projection, skip=skip, limit=limit

    filter_criteria = json.loads(request_data['filter_criteria']) if 'filter_criteria' in request_data else None
    projection = json.loads(request_data['projection']) if 'projection' in request_data else None
    skip = int(request_data['skip']) if 'skip' in request_data else None
    limit = int(request_data['limit']) if 'limit' in request_data else None

    results = get_results(filter_criteria, projection, skip, limit)

    return results, 200


def runserver(port=config.SERVER_PORT):
    initialize_mongo()
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
