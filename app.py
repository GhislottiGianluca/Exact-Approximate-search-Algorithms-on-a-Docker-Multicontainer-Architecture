from flask import Flask, app, request


def edge(s):
    result, i, m = "", 0, len(s) - 1
    while s[i] == s[m - i]:
        if s[i] == s[m - i]:
            i += 1

    i = 1 if i == 0 else i

    return i


def prefix_function(pattern):
    m = len(pattern)
    # TO-DO


app = Flask(__name__)


@app.route('/prova', methods=['POST'])
def prova():
    text = request.json["text"]
    pattern = request.json["pattern"]

    return {"text": text, "pattern": pattern}


if __name__ == '__main__':
    # port = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0", port=5000, debug=True)
