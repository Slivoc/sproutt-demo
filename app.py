from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)

# Load demo data
def load_demo_data():
    try:
        with open('demo_data.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

demo_data = load_demo_data()

@app.route('/')
def index():
    return render_template('demo/index.html', data=demo_data)

@app.route('/demo')
def demo():
    return render_template('demo/index.html', data=demo_data)

@app.route('/demo/dashboard')
def dashboard():
    return render_template('demo/dashboard.html', data=demo_data)

@app.route('/demo/sales')
def sales():
    return render_template('demo/sales.html', data=demo_data)

@app.route('/demo/purchasing')
def purchasing():
    return render_template('demo/purchasing.html', data=demo_data)

@app.route('/demo/operations')
def operations():
    return render_template('demo/operations.html', data=demo_data)

@app.route('/demo/reports')
def reports():
    return render_template('demo/dashboard.html', data=demo_data)

@app.route('/demo/prospecting')
def prospecting():
    return render_template('demo/prospecting.html', data=demo_data)

@app.route('/demo/ai-analysis')
def ai_analysis():
    return render_template('demo/ai_analysis.html', data=demo_data)

@app.route('/demo/price-lists')
def price_lists():
    return render_template('demo/price_lists.html', data=demo_data)

@app.route('/demo/portal')
def portal():
    return render_template('demo/portal.html', data=demo_data)

@app.route('/demo/mailbox')
def mailbox():
    return render_template('demo/mailbox.html', data=demo_data)

@app.route('/demo/tickets')
def tickets():
    return render_template('demo/tickets.html', data=demo_data)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    app.run(debug=False, host='0.0.0.0', port=port)
