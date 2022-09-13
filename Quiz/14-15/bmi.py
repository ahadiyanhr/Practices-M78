from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    string = "<p>Enter HEIGHT-WEIGHT after /bmi (Example: /bmi/175-75)</p>"
    return string


@app.route('/user/<string>')
def show_bmi(string):
    values = string.split("-")
    bmi = int(values[0])*int(values[1])
    return f'<p>BMI = {str(bmi)}<p>'

if __name__ == '__main__':
   app.run(debug = True)