import os

from werkzeug.serving import run_simple
from werkzeug.wrappers import Request
from werkzeug.wrappers import Response

from jsonrpc import dispatcher
from jsonrpc import JSONRPCResponseManager


@Request.application
def app(request):
    dispatcher["echo"] = lambda s: s
    dispatcher["add"] = lambda a, b: a + b

    response = JSONRPCResponseManager.handle(request.data, dispatcher)

    return Response(response.json, mimetype='application/json')


if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 4000))
    HOST = os.environ.get('HOST', '0.0.0.0')

    run_simple(HOST, PORT, app)
