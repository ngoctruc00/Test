#from flask import Flask, jsonify

#app = Flask(__name__)
bus = [
    { # 0
    'traloi':'ngu cmm'
    },

    { # 1
        'traloi':' thang 3d '
    },
    { # 2
        'traloi':'bo Huong nek '
    }
]
@app.route('/')
def hello():
    return{'HOME':' HELLO YOU'}

@app.route('/bus')
def get_bus():
    return jsonify(bus)

#@app.route('/bus/<int:index>')
#def get_qe(index):
    #qe = bus[index]
    #return jsonify(qe)

@app.route("/bus/<name>/")
def greet(name):
    msg =f'{name}'
    if (msg == "ngu"):
        return jsonify(bus[0])
    if msg == "hieu":
        return jsonify(bus[1])
    if ("phong" in msg) == True :
        return jsonify(bus[2])



    #return msg, 200, {'Content-Type': 'text/plain; charset=utf-8'}

app.run()
