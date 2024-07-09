from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        purchase_price = float(request.form['purchase_price'])
        commission_rate = 0.075  # Example: 7.5%
        vat_rate = 0.15  # Example: 15% VAT
        commission = purchase_price * commission_rate
        vat = commission * vat_rate
        net_commission = commission - vat
        agent_share = net_commission / 2

        return render_template('index.html', commission=commission, vat=vat, net_commission=net_commission, agent_share=agent_share)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
