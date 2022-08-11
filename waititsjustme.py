from flask import Flask,render_template
app = Flask(__name__, static_url_path='/static')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/writing', methods=['POST'])
def writing():
    return render_template('writing.html')

@app.route('/reviews', methods=['POST'])
def reviews():
    return render_template('reviews.html')

@app.route('/reports', methods=['POST'])
def reports():
    return render_template('reports.html')

@app.route('/about', methods=['POST'])
def about():
    return render_template('about.html')

@app.route('/home', methods=['POST'])
def homepg():
    return render_template('index.html')

@app.route('/ladymid', methods=['POST'])
def ladymid():
    return render_template('ladymidnight.html')