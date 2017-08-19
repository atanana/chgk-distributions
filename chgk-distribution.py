from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main():
    return app.send_static_file('main.html')


@app.route('/dist_control')
def admin():
    return render_template('admin.html')


if __name__ == '__main__':
    app.run()
