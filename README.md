# Sentiment Analysis Web App

This web application utilizes Flask and IBM Watson Natural Language Understanding (NLU) to conduct sentiment analysis on text input or URLs. It provides a sentiment score reflecting the overall emotional tone of the input text, ranging from -100 (very negative) to +100 (very positive).

## Features

- **Text Input:** Analyze sentiment from user-provided text.
- **URL Input:** Analyze sentiment from web page content by entering a URL.
- **Sentiment Analysis:** Calculates sentiment score and provides interpretation based on the score.
- **Visualization:** Visual representation of sentiment scores through a progress bar.

## Prerequisites

Before running the application, ensure you have the following:

- **Python 3.x**
- **Flask:** Install Flask using `pip install flask`.
- **IBM Cloud Account:** Obtain API Key and URL for IBM Watson NLU.
- **IBM Watson SDK:** Install IBM Watson Python SDK using `pip install ibm-watson`.

## Setup

1. Clone or download the repository.
2. Replace `'API_KEY'` and `'API_URL'` placeholders in `app.py` with your IBM Watson NLU credentials.

## Running the Application

1. Run the Flask application:
    ```
    python app.py
    ```
2. Access the application via a web browser at `http://localhost:5000`.

## Usage

1. **Text Input:**
   - Enter text in the provided box and click "Analyze Sentiment."
2. **URL Input:**
   - Enter a URL in the respective field and click "Analyze Sentiment."

The application will display the sentiment score, interpretation, and a progress bar indicating the emotional intensity of the analyzed text or URL content.

## Error Handling

- **Invalid URL:** Displays an error message for invalid URLs.
- **Unsupported Text Language:** Notifies if the text language is unsupported.
- **Other Errors:** Displays detailed error messages for any other issues encountered during analysis.

## Contributing

Feel free to contribute by creating issues or submitting pull requests.

## License

This project is licensed under the [MIT License](LICENSE).