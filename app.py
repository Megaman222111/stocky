from flask import Flask, render_template, request
from scraper import getData

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        symbol = request.form.get('symbol', '').strip()
        want_history = request.form.get('history')  # e.g. '1mo', '1d', or None

        data = getData(symbol, history=want_history)
        return render_template('result.html', data=data['info'], history=data.get('history'))

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
