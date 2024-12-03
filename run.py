import os

from application import create_app

config_type = os.getenv("CONFIG_TYPE")
app = create_app(config_type)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
