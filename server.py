from flask import Flask
from emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector?textToAnalyze=<string:prompt>')
def run_detector(prompt):
    emotions = emotion_detector(prompt)
    return f"For the given statement, the system response is 'anger': {emotions['anger']}, 'disgust': {emotions['disgust']}, 'fear': {emotions['fear']}, 'joy': {emotions['joy']} and 'sadness': {emotions['sadness']}. The dominant emotion is {emotions['dominant_emotion']}."

if __name__ == "__main__":
    app.run()