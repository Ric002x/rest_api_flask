import os

from dotenv import load_dotenv

from application import create_app

load_dotenv()

config_type = os.getenv("CONFIG_TYPE")
app = create_app(config_type)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
