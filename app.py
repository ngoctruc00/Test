from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/getmsg/', methods=['GET'])
def respond():

    name = request.args.get("name", None)


    print(f"got name {name}")

    response = {}


    if not name:
        response["ERROR"] = "hoi gi di nao ^^."

    elif str(name).isdigit():
        response["ERROR"] = "cau hoi nek."

    #else:
        #response["MESSAGE"] = f"Welcome {name} to our awesome platform!!"
    if str(name) == "xinchao":
        response["TRA LOI :"]= "CHAO CON ME MAY"
    if str(name) == "soi":
        response["TRA LOI :"] = "soi crush Yen nek"


    return jsonify(response)

@app.route('/post/', methods=['POST'])
def post_something():
    param = request.form.get('name')
    print(param)

    if param:
        return jsonify({
            "Message": f"Welcome {name} to our awesome platform!!",
            # Add this option to distinct the POST request
            "METHOD" : "POST"
        })
    else:
        return jsonify({
            "ERROR": "no name found, please send a name."
        })

# A welcome message to test our server
@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"

if __name__ == '__main__':

    app.run(threaded=True, port=8888)