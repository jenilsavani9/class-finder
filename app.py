from logging import debug
from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/heart', methods=['POST', 'GET'])
def heart():
   return render_template('heart.html')

@app.route('/heart/pred', methods=['POST', 'GET'])
def heart_pred():
    if request.method == "POST":
        try:
            age = int(request.form.get('age'))
            sex_cat = request.form.get('sex')
            if sex_cat == "male":
                sex = 1
            else:
                sex = 0
            exang_cat = request.form.get('exang')
            if exang_cat == "Yes":
                exang = 1
            else:
                exang = 0
            ca = int(request.form.get('ca'))
            cp_cat = request.form.get('cp')
            if cp_cat == "Typical Angina":
                cp = 0
            elif cp_cat == "Atypical Angina":
                cp = 1
            elif cp_cat == "Non-anginal Pain":
                cp = 2
            else:
                cp = 3
            trtbps = int(request.form.get('trtbps'))
            chol = int(request.form.get('chol'))
            fbs_cat = int(request.form.get('fbs'))
            if fbs_cat >= 120:
                fbs = 1
            else:
                fbs = 0
            rest_ecg_cat = request.form.get('rest_ecg')
            if rest_ecg_cat == "hypertrophy":
                rest_ecg = 0
            elif rest_ecg_cat == "Normal":
                rest_ecg = 1
            else:
                rest_ecg = 2
            thalach = int(request.form.get('thalach'))
            oldpeak = float(request.form.get('oldpeak'))
            slp_cat = request.form.get('slp')   
            if slp_cat == "Downsloping":
                slp = 0
            elif slp_cat == "Flat":
                slp = 1
            else:
                slp = 2

            thall = 1
            col = [age, sex, cp, trtbps, chol, fbs, rest_ecg, thalach, exang, oldpeak, slp, ca, thall]
            model = pickle.load(open('pkl/heart.pkl', 'rb'))
            prediction = model.predict([col])
            print(prediction)
            return render_template('heart_pred.html', ans=prediction)
        except:
            return render_template('error.html')
    else:
        return render_template('error.html')

@app.route('/bank', methods=['GET', 'POST'])
def bank():
    return render_template('bank.html')

@app.route('/bank/pred', methods=['GET', 'POST'])
def bank_pred():
    if request.method == 'POST':
        try:
            length = float(request.form.get('length'))
            left = float(request.form.get('left'))
            right = float(request.form.get('right'))
            bottom = float(request.form.get('bottom'))
            top = float(request.form.get('top'))
            diagonal = float(request.form.get('diagonal'))
            col = [length, left, right, bottom, top, diagonal]
            model = pickle.load(open('pkl/note.pkl', 'rb'))
            prediction = model.predict([col])    
            return render_template('bank_pred.html', ans=prediction)
        except:
            return render_template('error.html')
    else:
        return render_template('error.html')
        
if __name__ == "__main__":
    app.run(debug=True)
