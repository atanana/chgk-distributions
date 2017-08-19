from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import os

app = Flask(__name__)
socketio = SocketIO(app)
selected_asset = ''


@app.route('/')
def main():
    return render_template('main.html', selected_asset=selected_asset)


@app.route('/dist_control')
def admin():
    assets = os.listdir(os.path.join(app.root_path, 'static', 'assets'))
    return render_template('admin.html', assets=assets, selected_asset=selected_asset)


@socketio.on('asset select')
def handle_asset_select(data):
    global selected_asset
    selected_asset = data['name']
    print('select ' + data['name'])
    emit('asset change', {'name': selected_asset}, broadcast=True)


if __name__ == '__main__':
    socketio.run(app)
