from flask import Flask,request,render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/run-python-script', methods=['POST'])
def run_python_script():
    script_name=request.json['scriptName']
    script_path = f"{script_name}"
    os.system(f"python {script_path}")

    return {'message': 'Script executed sucessfully'}

if __name__=='__main__':
    app.run()