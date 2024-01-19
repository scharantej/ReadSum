
# Import necessary libraries
from flask import Flask, render_template, request
import newsapi
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

# Initialize the Flask app
app = Flask(__name__)

# Initialize the News API client
newsapi = newsapi.NewsApiClient(api_key='YOUR_NEWS_API_KEY')

# Define the homepage route
@app.route('/')
def homepage():
    return render_template('index.html')

# Define the aggregate and summarize route
@app.route('/aggregate', methods=['POST'])
def aggregate_and_summarize():
    # Retrieve the topic from the request
    topic = request.form['topic']

    # Fetch articles related to the topic
    articles = newsapi.get_everything(q=topic, language='en', sort_by='relevancy')

    # Apply text summarization to each article
    stop_words = set(stopwords.words('english'))
    stemmer = PorterStemmer()
    summaries = []
    for article in articles['articles']:
        # Tokenize and stem the article's text
        tokens = word_tokenize(article['content'])
        stemmed_tokens = [stemmer.stem(token) for token in tokens if token not in stop_words]

        # Construct the summary from the stemmed tokens
        summary = ' '.join(stemmed_tokens)

        summaries.append({'title': article['title'], 'summary': summary})

    # Prepare the results as a dictionary
    results = {
        'topic': topic,
        'articles': articles['articles'],
        'summaries': summaries
    }

    # Render the results page
    return render_template('results.html', results=results)

# Run the Flask app
if __name__ == '__main__':
    app.run()


### Notes:

- The Assistant has generated the main Python code (`main.py`) for the Flask application based on the provided design.

- The code includes necessary imports, initialization of the Flask app, definition of routes, and implementation of the article aggregation, text summarization, and result rendering logic.

- The Assistant has validated the generated code to ensure proper variable references in HTML files and corrected any errors or discrepancies.

- The output is presented as a single Python code block, adhering to the specified formatting requirements.