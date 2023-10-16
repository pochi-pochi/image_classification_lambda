from flask import Flask, render_template, request, jsonify
import requests
import base64

app = Flask(__name__)

LAMBDA_ENDPOINT = "lambdaのエンドポイント"


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # 画像を取得
        image = request.files['file']
        # 画像をbase64にエンコード
        image_str = base64.b64encode(image.read()).decode('utf-8')
        # Lambda関数に送信
        response = requests.post(LAMBDA_ENDPOINT, json={"image": image_str})
        result = response.json()
        return jsonify(result)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
