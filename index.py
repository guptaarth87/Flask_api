from flask import Flask
from flask import jsonify
from home import home_bp

app = Flask(__name__)
@app.route('/hello/', methods=['GET', 'POST'])
def welcome():
    return "Hello User!"

@app.route('/<string:name>/')
def hello(name):
    return "Hello " + name

@app.route('/<int:number>/')
def incrementer(number):
    return "Incremented number is " + str(number+1)

@app.route('/person/')
def hello1():
    return jsonify({'name':'Arth gupta',
                    'address':'India'})

def appRun():
  if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)
  else:
      app.logger.error('This is an ERROR message')

app.register_blueprint(home_bp, url_prefix='/home')

appRun()