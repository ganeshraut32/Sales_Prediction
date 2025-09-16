from flask import Flask, render_template, request
from model import regressor_model

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def sales_view():
    if request.method == 'GET':
        return render_template("sales.html")

    elif request.method == 'POST':
        tv = float(request.form["tv"])
        radio = float(request.form["radio"])
        newspaper = float(request.form["newspaper"])
        op_array=regressor_model.predict([[tv,radio,newspaper]])
        y_pred =round(op_array[0],2)
        return render_template("output.html",predicted_sales = y_pred)
app.run(debug=True)