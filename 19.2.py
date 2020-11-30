from flask import Flask, request, jsonify,redirect
import datetime
import random

time_1 = datetime.datetime.now()

app = Flask(__name__)
rep1 = {1: 'soi bu dit ',2: 'concac',3:'soi yeu yen',4:'love Yen forever', 5:'Soi TD18 MSSV 18151050066'}
rep2 = {1: 'Phong Hokage ',2: 'Neu ban khong biet thi phong la mot monster ',3:' que DOng Nai ',4:' ..... ', 5:'404 NOT FOUND'}
rep3 = {1: 'MOI RA TU ',2: 'BEDE BEDE BEDE Cai gi quan trong noi 3 lan ',3:' que Nghe An',4:' yeu con trai', 5:'404 NOT FOUND'}

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
        response["TRA LOI :"] = "cc"
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
@app.route('/question/', methods= ['GET'])
def ques_somthing():

    ques = request.args.get("ques", None)

    print(f"got name {ques}")

    response = {}
    if not ques:
        response["ERROR"] = "ask something ~~"
    if ("time" in str(ques)) == True:
         response["rep:"] = str(time_1)
    if ( "phong" in str(ques)) == True :
        response[ "rep:"] = random.choice(list(rep2.items()))
    if ("new" in str(ques)) == True:
        response["rep:"] = " nothing in here "
    if ("old" in str(ques)) == True:
        response["rep:"] =  " I am 3 years old"
    if ( "soi" in str(ques)) == True:
        response[ "rep:"] = random.choice(list(rep1.items()))
    if ("hieu" in str(ques)) == True:
            response["rep:"] = random.choice(list(rep3.items()))



    return jsonify(response)
#@app.route('/login', methods = ['GET', 'POST'])
#def login():



# A welcome message to test our server
@app.route('/')
def index():
    #return "<h1>Welcome to our server !!</h1>"
    return redirect('/question/')

if __name__ == '__main__':

    app.run(threaded=True, port=8888)