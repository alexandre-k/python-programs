import os
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('layout.html')

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 9500))
    if os.environ.get('APP_MODE', 'development') == 'development':
        debug = True
    else:
        debug = False
    app.run(host='0.0.0.0', port=port, debug=debug)
