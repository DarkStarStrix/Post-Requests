import flask as fl

app = fl.Flask(__name__)


@app.route('/')
def index():
    # link to index.html
    return fl.render_template('index.html')


@app.route('/contact')
def contact():
    # link to contact.html
    return fl.render_template('contact.html')


@app.route('/form-entry')
def form_entry():
    # link to form-entry.html
    return fl.render_template('form-entry.html')


@app.route('/form-display')
def form_display():
    # link to form-display.html
    return fl.render_template('form-display.html')


@app.route('/form-entry')
def receive_data():
    # receive data from form-entry.html
    return fl.render_template('form-entry.html')


