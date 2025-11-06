"""Flask application entry point."""
from flask import Flask, jsonify


def create_app() -> Flask:
    """Create and configure the Flask application instance."""
    app = Flask(__name__)

    @app.get("/")
    def home():
        """Return a friendly greeting."""
        return jsonify(message="Hello, World!")

    @app.get("/about")
    def about():
        """Return basic information about the service."""
        return jsonify(
            service="Flask Hello World",
            description="A minimal API showcasing a simple Flask application.",
        )

    return app


app = create_app()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
