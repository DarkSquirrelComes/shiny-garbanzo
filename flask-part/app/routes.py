from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Vue! Hello from Flask!"
