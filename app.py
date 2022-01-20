# from flask import Flask, request, jsonify, render_template
import pickle
# import pandas as pd
import numpy as np
import pandas as pd
from URLFeatureExtraction import featureExtraction
from flask import Flask,render_template,request

loaded_model = pickle.load(open("XGBoostClassifier.pkl", "rb"))


#converting the list to dataframe
feature_names = ['Have_IP', 'Have_At', 'URL_Length', 'URL_Depth','Redirection', 
                      'https_Domain', 'TinyURL', 'Prefix/Suffix', 'DNS_Record', 'Web_Traffic', 
                      'Domain_Age', 'Domain_End', 'iFrame', 'Mouse_Over','Right_Click', 'Web_Forwards']
legi_urls = ["https://www.google.com/","https://www.facebook.com/","https://www.youtube.com/","https://www.apple.com/","https://www.juet.ac.in/",
             "https://www.amazon.com/", "https://www.netflix.com/in/", "https://www.flipkart.com/", "https://www.hurawatch.com/", "https://web.whatsapp.com/",
             "https://classroom.google.com/u/1/h", "https://www.github.com/", "https://www.gmail.com/", "https://wwww.wikipedia.com/"]


# x = featureExtraction(url)

# if url in legi_urls:
#     print(0)
# else:
#     data_frame = pd.DataFrame(data=[x],columns=feature_names)
#     prediction = loaded_model.predict(data_frame)
#     print(prediction)




 
                    


# data1 = [np.array(data)]




## APP MAKING -----------
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/getURL',methods=['GET','POST'])
def getURL():
    if request.method == 'POST':
        url = request.form['url']
        print(url)
        x = featureExtraction(url)
        print(x) 

        if url in legi_urls:
            value = "Legitimate"
            return render_template("home.html",error=value)
        else:
            data_frame = pd.DataFrame(data=[x],columns=feature_names)
            prediction = loaded_model.predict(data_frame)
            print(prediction) 
            
            if prediction[0] == 0:
                value = "Legitimate"
            else:
                value = "Phishing"    
            return render_template("home.html",error=value)     











        #print(predicted_value)
        # if predicted_value == 0:    
        #     value = "Legitimate"
        #     return render_template("home.html",error=value)
        # else:
        #     value = "Phishing"
        #     return render_template("home.html",error=value)
if __name__ == "__main__":
    app.run(debug=True)