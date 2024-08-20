from app import app

@app.routes('/')
def index():
    return "Hello, Flask!"