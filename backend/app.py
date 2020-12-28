#!/usr/bin/env python3


from flask import Flask


app = Flask(__name__)


@app.route('/example', methods=[])
def example():
    return "hello world", 200


def main():
    ''' main driver '''
    app.run(host='0.0.0.0', port=6969)


if __name__ == '__main__':
    main()
