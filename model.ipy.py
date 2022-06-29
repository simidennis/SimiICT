

import pickle
model = pickle.load(open('model.pkl', 'rb'))

app = Flask(__name__)
@app.route('/')
def home():
      return render_template('index.html')

  
@app.route('/predict',methods=['POST'])
def predict():
    
if __name__ == "__main__":
    app.run(debug=True)   