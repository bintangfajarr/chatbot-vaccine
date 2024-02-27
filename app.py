from flask import Flask,render_template,request,jsonify
from flask_cors import CORS
from chat import get_response

app = Flask(__name__)
CORS(app)
@app.get("/")
def index_get():
    return render_template("base.html")

@app.post("/predict")
def predict():
    data = request.get_json()
    message = data.get("message")

        # Call get_response function
    response = get_response(message)
    print({"response": response})
        # Return response as JSON
    return jsonify({"response": response})
    
if __name__ == "__main__":
    app.run(debug=True)