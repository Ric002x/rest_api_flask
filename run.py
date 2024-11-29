import os

from app.main import app

if __name__ == '__main__':
    os.environ["FLASK_APP"] = "run.py"
    os.environ["FLASK_ENV"] = "development"
    app.run(host="0.0.0.0", port=5000, debug=True)
