from flask import Flask, render_template, request, jsonify
import numpy as np
import os as os

app = Flask(__name__)
past_names = dict()


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/response', methods=['POST'])
def get_response():
    try:
        data = request.get_json(force=True)
        text = data.get('text', None)
        print(text)
        adjective = past_names.get(text, default=get_adjective())
        greeting = "Glad to meet you again, {} {}!".format(adjective, text)
        response = str(greeting)
    except:
        response = 'Errors... We don\'t need more errors, huh? Do something with it.'

    return jsonify({'response': response})


def get_adjective():
    adjs = {1:"holy",
            2:"godlike",
            3:"wise",
            4:"allowing me to go to interview",
            5:"stylish",
            6:"kind",
            7:"intellectual",
            8:"amazing",
            9:"cool"}
    randkey = np.random.randint(1, 10)
    print(randkey)
    return adjs.get(randkey)


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
