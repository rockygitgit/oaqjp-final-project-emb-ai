""" Module service for emotion detection"""
import json
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    """Function index page."""
    return render_template("index.html")


@app.route('/emotionDetector', methods=['GET'])
def emotion_detector_funcion():
    """Function emotion detector"""
    text_to_analyze=request.args.get('textToAnalyze')
    result_1 = json.loads(emotion_detector(text_to_analyze))
    print(result_1)
    if result_1['dominant_emotion'] is None:
        result= "Invalid text! Please try again!."
    else :
        result= "For the given statement, the system response is "\
            + f"'anger': {result_1['anger']}, "\
            + f"'disgust': {result_1['disgust']}, "\
            + f"'fear': {result_1['fear']},  "\
            + f"'joy': {result_1['joy']}  "\
            + f"and 'sadness': {result_1['sadness']}.  "\
            + f"The dominant emotion is {result_1['dominant_emotion']}. "
    print(result)
    return result

if __name__ == '__main__':
    app.run(host='localhost', port=5000,debug=True)
