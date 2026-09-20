from flask import Flask
from flask import Flask
import pandas
import numpy

def create_app():
    app = Flask(__name__)
    print("inside create_app function")

    @app.route('/')
    def home():
        print("inside home function")
        for i in range(10):
            print("inside home function")
        return 'Hi hi GFG48 19-09-2026 Hi hello1234'

    @app.route('/')
    def home():
        print("inside home function")
        while True:
            print("inside home function")
        return 'Hi hi GFG48 19-09-2026 Hi hello1234'

    @app.route('/test')
    def home1():
        print("inside home1 function")
        while True:
            print("inside home1 function")
        return 'Hi hi GFG48 19-09-2026 Hi hello1234'

    return app


if __name__ == '__main__':
    app = create_app()

    app.run(host='0.0.0.0', port=80, debug=True)
