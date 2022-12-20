from flask import Flask, app, request


def edge(s):
    result, i, m = 0, 1, len(s)
    while i != len(s):
        result = i if s[0: i] == s[m - i: m] else result
        i += 1

    return result


def prefix_function(pattern):
    m = len(pattern)
    # TO-DO


app = Flask(__name__)


@app.route('/prova', methods=['POST'])
def prova():
    text = request.json["text"]
    pattern = request.json["pattern"]

    return {"result": edge(request.json["s"])}
    # return {"text": text, "pattern": pattern}


if __name__ == '__main__':
    # port = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0", port=5000, debug=True)
