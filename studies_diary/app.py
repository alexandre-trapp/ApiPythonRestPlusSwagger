from flask import Flask, Blueprint
from restplus import api
from endpoints.helloworld import ns_default
from endpoints.category import ns_category
from db import config_db
from log import log

app = Flask(__name__)

def initialize_app(app):

    app.config["RESTPLUS_VALIDATE"] = True
    app.config['ERROR_404_HELP'] = False

    config_db(app)
    blueprint = Blueprint('api', __name__)

    api.init_app(blueprint)
    app.register_blueprint(blueprint)

    api.add_namespace(ns_default)
    api.add_namespace(ns_category)

def main():
    
    initialize_app(app)
    log.info(
        '>>>>> Starting development server at http://{}/ <<<<<'.format(app.config['SERVER_NAME']))

    app.run(debug=True)

if __name__ == '__main__':
    main()