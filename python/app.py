from flask import Flask, request, jsonify
app = Flask(__name__)
students = [{"name":"Ajeet","Roll":"12"},
{"name":"Ajeet","Roll":"12"},
{"name":"Ajeet","Roll":"12"},
{"name":"Ajeet","Roll":"12"}]
@app.route('/')
def helloWorld():
    return "Hello World"

@app.route('/students')
def students_fun():
    return students

@app.route('/add/<numbera>/<numberb>')
def add_two_num(numbera,numberb):
    numc = int(numbera) + int(numberb)
    return str(numc)

@app.route('/sub/<numa>/<numb>')
def sub_two_num(numa,numb):
    numc = int(numa) - int(numb)
    return str(numc)

@app.route('/div/<numa>/<numb>')
def div_two_num(numa,numb):
    numc = int(numa) / int(numb)
    return str(numc)

@app.route('/mul/<numa>/<numb>',methods=['GET','POST'])
def mul_two_num(numa,numb):
    numc = int(numa) * int(numb)
    return str(numc)

@app.route('/calculate/<numa>/<numb>/<operator>')
def calculatator(numa,numb,operator):
    if operator == '+':
        return str(int(numa) + int(numb))
    elif operator == '-':
        return str(int(numa) - int(numb))
    elif operator == '*':
        return str(int(numa) * int(numb))
    elif operator == '%':
        return str(int(numa) / int(numb))

if __name__ == '__main__':
    app.run(debug=True)