from apps import app


@app.route('/')
def index():
    return "<h1>EMS Homepage</h1>"
