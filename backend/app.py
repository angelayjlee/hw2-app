from flask import Flask, jsonify, send_from_directory
import requests
import os
from flask_cors import CORS

static_path = os.getenv('STATIC_PATH','static')
template_path = os.getenv('TEMPLATE_PATH','templates')

app = Flask(__name__, static_folder=static_path, template_folder=template_path)
CORS(app)

# route to get NYT API key
@app.route('/api/key')
def get_key():
    return jsonify({'apiKey': os.getenv('NYT_API_KEY')})

@app.route('/api/articles')
def get_articles():
    nyt_api_key = os.getenv('NYT_API_KEY')
    url = f'https://api.nytimes.com/svc/search/v2/articlesearch.json?q=davis+or+sacramento&api-key={nyt_api_key}'

    try:
        response = requests.get(url)
        data = response.json()

        #filter articles that mention "davis" or "sacramento"
        filtered_articles = [
            article for article in data.get('response', {}).get('docs', [])
            if 'davis' in article.get('headline', {}).get('main', '').lower() or
               'sacramento' in article.get('headline', {}).get('main', '').lower()  
        ]
        return jsonify({'results': filtered_articles})
            
    except Exception as e:
        print('Error fetching NYT data:', e)
        return jsonify({'results': [], 'error': str(e)})


@app.route('/')
@app.route('/<path:path>')
def serve_frontend(path=''):
    if path != '' and os.path.exists(os.path.join(static_path,path)):
        return send_from_directory(static_path, path)
    return send_from_directory(template_path, 'index.html')

if __name__ == '__main__':
    debug_mode = os.getenv('FLASK_ENV') != 'production'
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8000)),debug=debug_mode)