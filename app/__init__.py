from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.get("/")
    def home():
        return {
            "name": "FixIt",
            "description": "Apartment Maintenance Request System",
            "status": "running",
        }, 200

    @app.get("/health")
    def health():
        return {"status": "ok"}, 200

    return app
