from flask import Flask, render_template, request, jsonify
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, SentimentOptions

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods = ['POST'])
def analyze_sentiment():

    #replace with your Watson API credentials
    api_key = 'API_KEY'
    url = 'API_URL'

    authenticator = IAMAuthenticator(api_key)
    natural_language_understanding = NaturalLanguageUnderstandingV1(
        version = '2022-04-07',
        authenticator = authenticator
    )

    natural_language_understanding.set_service_url(url)

    try:
        data = request.json
        if 'text' in data:
            response = natural_language_understanding.analyze(
                text = data['text'],
                features = Features(sentiment=SentimentOptions())).get_result()
        elif 'url' in data:
            response = natural_language_understanding.analyze(
                url = data['url'],
                features = Features(sentiment = SentimentOptions())).get_result()
        else:
            return jsonify({'error': 'No input provided'})

        return jsonify(response)

    except Exception as e:
        if 'not enough text for language id' in str(e).lower():
            return jsonify({'error': 'Input text is too short for language identification'})
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug = True)