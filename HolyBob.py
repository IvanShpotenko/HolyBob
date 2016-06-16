from flask import Flask, render_template, request, jsonify
import numpy as np

app = Flask(__name__)
past_adjectives = set()


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/response', methods=['POST'])
def get_response():
    try:
        data = request.get_json(force=True)
        text = data.get('text', None)
        print(text)
        adjective = get_adjective()
        while adjective in past_adjectives:
            adjective = get_adjective()
        past_adjectives.add(adjective)
        greeting = "Рад тебя видеть снова, {} {}!".format(adjective, text)
        response = str(greeting)
    except:
        response = 'Errors... We don\'t need more errors, huh? Do something with it.'

    return jsonify({'response': response})


def get_adjective():
    adjs = {1:"красивый",
            2:"божественный",
            3:"премудрый",
            4:"разрешающий мне пройти на собеседование",
            5:"стильный",
            6:"добрый",
            7:"интеллектуальный",
            8:"многогранный",
            9:"классный"}
    randkey = np.random.randint(1, 10)
    print(randkey)
    return adjs.get(randkey)


if __name__ == '__main__':
    app.run()
