


from flask import Flask, request, jsonify, render_template
import projectbi3 

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index2.html')

@app.route('/detect', methods=['POST'])
def detect():
  url = request.form.get('url')  
  is_phishing = not projectbi3.detect_phishing(url)  
  if is_phishing:
    result = "Phishing site detected!"
  else:
    result = "This site seems safe."

  return jsonify({'result': result})  

if __name__ == '__main__':
  app.run(debug=True)