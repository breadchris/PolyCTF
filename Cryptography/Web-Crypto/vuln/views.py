from flask import render_template

def init_views(app):
    @app.route('/')
    def index():
        return render_template('index.html')
