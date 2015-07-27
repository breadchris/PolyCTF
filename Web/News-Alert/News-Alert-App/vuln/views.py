from flask import render_template, request

def init_views(app):
    @app.route('/', methods=['POST', 'GET'])
    def index():
        if request.method == 'POST':
            if request.form and 'comment' in request.form.keys():
                return render_template('index.html', comment=request.form['comment'])

        return render_template('index.html')
