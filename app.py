from flask import Flask, render_template

app = Flask(__name__)

@app.context_processor
def inject_categories():
    categories = ['Around the World', 'Quick & Easy', 'Healthy Food', 'Sweet Treats']
    return dict(categories=categories)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/category/<category>')
def category(category):
    return render_template('categories.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/my_book')
def my_book():
    return render_template('my_book.html')

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
