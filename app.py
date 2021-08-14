from flask import Flask, render_template
from flask_flatpages import FlatPages, pygments_style_defs


DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_MARKDOWN_EXTENSIONS = ['codehilite']
FLATPAGES_EXTENSION = '.md'


app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)


@app.route('/')
def index():
    return render_template('index.j2', pages=pages)


@app.route("/<path:path>/")
def page(path):
    ctx = pages.get_or_404(path)
    return render_template("page.j2", page=ctx)


@app.route('/pygments.css')
def pygments_css():
    return pygments_style_defs('tango'), 200, {'Content-Type': 'text/css'}


if __name__ == '__main__':
    app.run(port=8000)
