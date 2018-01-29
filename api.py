import json

from flask import jsonify, request, Response
import connexion
import inflection
from awslogs import AWSLogs


config = {
    'streams_start_default': '1h',
    'logs_start_default': '5m',
    'logs_log_stream_name_default': 'ALL',
}


def hello():
    return "Hello World!"


def groups():
    params = dict(request.args.items())
    return jsonify({'groups': list(AWSLogs(**params).get_groups())})


def streams():
    params = dict(request.args.items())
    params['start'] = params.get('start') or config['streams_start_default']
    return jsonify({'streams': list(AWSLogs(**params).get_streams())})


def logs():
    params = dict(request.args.items())
    params['start'] = params.get('start') or config['logs_start_default']
    params['log_stream_name'] = (params.get('log_stream_name')
                                 or config['logs_log_stream_name_default'])
    params['watch'] = params.get('watch') == 'true'
    logs = (snake_keys(log) for log in AWSLogs(**params).iter_logs())
    if params['watch']:
        return Response((json.dumps(log) + '\r\n' for log in logs),
                        mimetype='text/plain')
    else:
        return jsonify({'logs': list(logs)})


def snake_keys(dic):
    res = {}
    for key, value in dic.items():
        res[inflection.underscore(key)] = value
    return res


app = connexion.FlaskApp(__name__)
app.add_api('swagger.yaml', arguments=config)
if __name__ == '__main__':
    app.run()
