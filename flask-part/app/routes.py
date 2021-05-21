from app import app

@app.route('/')
def index():
    return "Vue! Hello from Flask!"
