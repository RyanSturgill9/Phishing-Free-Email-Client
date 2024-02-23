from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_python_script', methods=['POST'])
def run_python_script():
    data = request.get_json()
    script_path = data.get('scriptPath', '')
    
    try:
        result = subprocess.check_output(['python', script_path], stderr=subprocess.STDOUT, text=True)
        return jsonify(result=result)
    except subprocess.CalledProcessError as e:
        return jsonify(error=str(e.output))

if __name__ == '__main__':
    app.run(debug=True)
