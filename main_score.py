from flask import Flask, render_template_string
import os
from utils import SCORES_FILE_NAME

# Initialize the Flask app
app = Flask(__name__)

@app.route('/')
def score_server():
    """
    Reads the score from the 'Scores.txt' file and serves it via HTTP with HTML.
    """
    try:
        # Check if the scores file exists
        if os.path.exists(SCORES_FILE_NAME):
            # Read the score from the file
            with open(SCORES_FILE_NAME, 'r') as file:
                score = file.read().strip()
        else:
            # If the file doesn't exist, set score to 0
            score = "0"

        # HTML template for displaying the score
        html_content = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>User Score</title>
        </head>
        <body>
            <h1>Your Current Score:</h1>
            <p><strong>{score}</strong></p>
        </body>
        </html>
        """
        return render_template_string(html_content)
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    app.run(debug=True)
