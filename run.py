from extensions import app
from app.controller.service_controller import api

app.register_blueprint(api)

@app.route('/')
def home():
    return "hello"

if __name__ == "__main__":
    app.run(port=80, debug=True)


