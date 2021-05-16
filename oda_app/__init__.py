from flask import Flask, render_template, request, flash, json
from oda_app.functions import plus, minus, multiply, division

app = Flask(__name__)
app.debug = True
app.secret_key = "mama"

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/healthz", methods=["GET"])
def healthCheck():
    return "", 200

# TODO(everyone): GET 메소드로 더하기, 빼기, 곱하기, 나누기 함수 라우트 완성하기
@app.route("/calculator", methods=["POST","GET"])
def calculator():
    op = request.values.get("op")
    arg1 = request.values.get("arg1")
    arg2 = request.values.get("arg2")

    
    if op == "plus":
        result = plus(arg1, arg2)
        flash(f"더하기 계산 결과 : {result}")
    elif op == "minus":
        result = minus(arg1, arg2)
        flash(f"빼기 계산 결과 : {result}")
    elif op == "multiply":
        result = multiply(arg1, arg2)
        flash(f"곱하기 계산 결과 : {result}")
    elif op == "division":
        result = division(arg1, arg2)
        flash(f"나누기 계산 결과 : {result}")
    else:
        if request.method == 'POST':
            flash("연산자가 없습니다.")
    
    return render_template("calculator.html")
