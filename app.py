from flask import Flask, app, request


def edge(s):
    result, i, m = 0, 1, len(s)
    while i != len(s):
        result = i if s[0: i] == s[m - i: m] else result
        i += 1

    return result


def prefix_function(pattern, j):
    m = len(pattern)
    if j == 0:
        return -1
    if 1 <= j <= m:
        return edge(pattern[0:j - 1])
    else:
        return -10


app = Flask(__name__)


@app.route('/KMP', methods=['POST'])
def prova():
    text, pattern, j, q = request.json["text"], request.json["pattern"], 0, 0

    # Checking if text or pattern are empty.
    if text is None or pattern is None:
        return {"Pattern or Text": "are empty."}

    # KMP algorithm
    for q in range(0, len(text)):
        while j >= 0 and pattern[j] != text[q]:
            j = prefix_function(pattern, j)
        j += 1
        if j == len(pattern):
            return {"Result": q - len(pattern) + 1}

    return {"Result": "There isn't matching."}


if __name__ == '__main__':
    # port = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0", port=5000, debug=True)
