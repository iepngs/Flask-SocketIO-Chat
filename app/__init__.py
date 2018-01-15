from flask import Flask
from flask_socketio import SocketIO
import eventlet
eventlet.monkey_patch(socket=True)

# No Redis (works)
socketio = SocketIO(async_mode='eventlet')

# With Redis (bug)
# socketio = SocketIO(message_queue='redis://', async_mode='eventlet')


def create_app(debug=False):
    """Create an application."""
    app = Flask(__name__)
    app.debug = debug
    app.config['SECRET_KEY'] = 'gjr39dkjn344_!67#'

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    socketio.init_app(app)
    return app
