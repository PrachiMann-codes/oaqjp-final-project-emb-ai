from flask import Flask, request, jsonify, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector", methods=["GET"])
def emotion_detect():  
    # Get text from query parameter
    text_to_analyze = request.args.get("text", "")

    # Run emotion detector
    emotions = emotion_detector(text_to_analyze)

    # Build formatted sentence
    formatted_sentence = (
        f"For the given statement, the system response is "
        f"'anger': {emotions['anger']}, "
        f"'disgust': {emotions['disgust']}, "
        f"'fear': {emotions['fear']}, "
        f"'joy': {emotions['joy']} and "
        f"'sadness': {emotions['sadness']}. "
        f"The dominant emotion is **{emotions['dominant_emotion']}**."
    )

    if "emotionPredictions" not in formatted_response:
        return {"error": "No emotion predictions found", "response": formatted_response}


    # Return formatted sentence directly
    return formatted_sentence

@app.route("/") 
def render_index_page(): 
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
