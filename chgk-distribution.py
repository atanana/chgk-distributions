from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route('/')
def main():
    return app.send_static_file('main.html')


@app.route('/dist_control')
def admin():
    assets = os.listdir(os.path.join(app.root_path, 'static', 'assets'))
    return render_template('admin.html', assets=assets)


if __name__ == '__main__':
    app.run()
