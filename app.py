from flask import Flask, render_template, request
from scraper import getData

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        symbol = request.form['symbol']
        history = request.form.get('history')

        try:
            data = getData(symbol, history=history)

            # Ensure 'info' is always at least an empty dict
            info = data.get('info', {}) if data else {}
            history_data = data.get('history', []) if data else []

            return render_template('result.html', data=info, history=history_data)

        except Exception as e:
            print(f"Error fetching data: {e}")
            return render_template('error.html')

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
