from flask import Flask, render_template
from flask_socketio import SocketIO
import os

app = Flask(__name__)
socketio = SocketIO(app)
selected_asset = ''


@app.route('/')
def main():
    return app.send_static_file('main.html')


@app.route('/dist_control')
def admin():
    assets = os.listdir(os.path.join(app.root_path, 'static', 'assets'))
    return render_template('admin.html', assets=assets)


@socketio.on('asset select')
def handle_asset_select(data):
    selected_asset = data['name']
    print('select ' + data['name'])


if __name__ == '__main__':
    socketio.run(app)
