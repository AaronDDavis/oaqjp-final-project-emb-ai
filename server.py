"""
Flask server for Emotion Detection application.
"""

from flask import Flask, request
from emotion_detection import emotion_detector  # pylint: disable=import-error

app = Flask(__name__)

@app.route('/emotionDetector')
def run_detector():
    """
    Analyze text for emotions and return the formatted result.
    """
    emotions = emotion_detector(request.args.get('textToAnalyze'))
    if emotions['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is "
        f"'anger': {emotions['anger']}, 'disgust': {emotions['disgust']}, "
        f"'fear': {emotions['fear']}, 'joy': {emotions['joy']} "
        f"and 'sadness': {emotions['sadness']}. "
        f"The dominant emotion is {emotions['dominant_emotion']}."
    )

if __name__ == "__main__":
    app.run(debug=True)
