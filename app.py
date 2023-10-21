from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    name = request.args.get('name', 'World')
    product_list = [
        {'name': 'iPhone', 'price': 999.99},
        {'name': 'Samsung Galaxy', 'price': 899.99},
        {'name': 'Google Pixel', 'price': 699.99},
    ]

    return render_template('index.html', name=name, products=product_list)


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
