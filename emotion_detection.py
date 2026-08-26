import requests

def emotion_detector(text_to_analyze):
    response = requests.post(url="https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict", headers={"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}, json={"raw_document": { "text": text_to_analyze }});
    emotions = response.json()["emotionPredictions"][0]["emotion"]
    dominant_emotion_val = max(emotions.values())
    emotions["dominant_emotion"] = [key for (key, value) in emotions.items() if value == dominant_emotion_val][0]
    return emotions
