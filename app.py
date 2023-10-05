from flask import Flask,Response

app=Flask(__name__)

@app.route('/')
def home():
    return Response("First Docker application with flask!")

if __name__ =="__main__":
    app.run(debug=True,host="0.0.0.0",port=5000)