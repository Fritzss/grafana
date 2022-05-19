#!/usr/bin/python3

from flask import Flask, request

APP = Flask(__name__)


@APP.route('/route', methods=['POST'])
def route():
    login = request.args.get('login')
    password = request.args.get('password')
    if login == 'us' and password == 'pass':
        route = request.args.get('packageName')
        data = request.data
        print(f'route {route} {data}')
        res = request.data
    else:
        res = 'fail'
    return res


if __name__ == "__main__":
    from waitress import serve
    serve(APP, host="0.0.0.0", port=8080)
