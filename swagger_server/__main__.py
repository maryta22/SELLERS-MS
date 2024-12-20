#!/usr/bin/env python3

from connexion import FlaskApp
from flask_cors import CORS

from swagger_server import encoder


def main():
    app = FlaskApp(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'SELLERS-MS'}, pythonic_params=True)
    app.run(port=3030)


if __name__ == '__main__':
    main()
