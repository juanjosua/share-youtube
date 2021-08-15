from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/share', methods=['POST'])
def share():
    video_code = request.form['youtube_link'].partition("v=")[2]
    thumbnail = 'https://i.ytimg.com/vi_webp/{}/sddefault.webp'.format(
        video_code)

    return render_template('display.html', thumbnail=thumbnail)


if __name__ == '__main__':
    app.run(debug=True)
