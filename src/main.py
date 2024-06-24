'''
    Contains the server to run our application.
'''
from flask import Flask, render_template
from flask_failsafe import failsafe

app = Flask(__name__)


@failsafe
def create_app():
    '''
        Gets the underlying Flask server from our Dash app.

        Returns:
            The server to be run
    '''
    # the import is intentionally inside to work with the server failsafe
    from app import app  # pylint: disable=import-outside-toplevel
    return app.server

# Route to render the HTML template


if __name__ == "__main__":
    create_app().run(port="8050", debug=True)
