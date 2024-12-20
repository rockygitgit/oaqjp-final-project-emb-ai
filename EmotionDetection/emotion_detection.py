import requests
import json

def emotion_detector(text_to_analyze) :
    url='https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers={"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj= { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers=headers)
    jo=json.loads(response.text)

    emo=jo["emotionPredictions"][0]["emotion"]

    highest_score=0
    dominat_emo=""
    for emotion, score in emo.items() :
        if score > highest_score :
            highest_score=score
            dominat_emo=emotion
    emo["dominant_emotion"]=dominat_emo
    return json.dumps(emo, indent=1)

#emotion_detector("I love this new technology")
