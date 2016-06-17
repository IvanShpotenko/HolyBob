from __future__ import print_function
from flask import Flask, render_template, request, jsonify
import numpy as np
import os as os
from nltk.corpus import wordnet as wn

app = Flask(__name__)
past_names = dict()
adjectives =[synset.name().split('.')[0] for synset in list(wn.all_synsets('a'))]
adjs = {1: "holy",
        2: "godlike",
        3: "wise",
        4: "allowing me to go to interview",
        5: "stylish",
        6: "kind",
        7: "intellectual",
        8: "amazing",
        9: "cool"}


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/response', methods=['POST'])
def get_response():

    data = request.get_json(force=True)
    text = data.get('text', None)
    past_names.setdefault(text, get_adjective())
    greet_line = "I am glad to see you again,"
    # print(open(r'requirements.txt', 'r').read())
    # with open(os.path.abspath("HolyBob/russian.txt"), 'r') as f:
    #     first_line = f.readline()
    # with open("templates/russian.txt") as f:
    with app.open_resource('russian.txt') as f:
        for line in f:
            print(line)
    greeting = "{} {} {}!".format(greet_line, past_names[text], text).encode("utf-8")
    response = greeting.decode("utf-8")

    return jsonify({'response': response})


def get_adjective():
    randkey = np.random.randint(1, 10)
    forRet = ""
    for key, value in adjs.items():
        if key == randkey:
            forRet = adjs[key]
            adjs[key]= get_NLTK_adjective()

    print(adjs.items())
    return forRet

def get_NLTK_adjective():
    randkey = np.random.randint(len(adjectives))
    return adjectives.pop(randkey)

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
