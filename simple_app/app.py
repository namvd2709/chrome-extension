from flask import Flask
from predict import summarize
from time import time
from flask import jsonify, request
import os
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def api_exec():
    if request.method == 'POST':
        text = request.values.get('text')
    else:
        text = request.args.get('text')
    if text == None:
        print('Scoring Sample Description')
        text = os.environ['SAMPLE_TEXT']

    response = {'status': 'ok'}
    try:
        start_time = time()
        summary = summarize(text)
        infer_time = time() - start_time
    except Exception as e:
        print("Error when predicting", e)
        response = {"status": "fail", "message": "Error when summarizing: {}".format(str(e))}

    if response["status"] == "ok":
        response.update({
            "text": text,
            "summary": summary,
            "infer_time": infer_time
        })

    return jsonify(response)


if __name__ == '__main__':
    app.run()
