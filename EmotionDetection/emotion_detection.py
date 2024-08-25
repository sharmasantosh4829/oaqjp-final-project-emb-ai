import requests
import json

def emotion_detector(text_to_analyze):

    # Define the URL for the sentiment analysis API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Create the payload with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyze } }

    # Set the headers with the required model ID for the API
    header =  {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json=myobj, headers=header)
    print(response.status_code)

    # Parse the response from the API
    formatted_response = json.loads(response.text)

    # If the response status code is 200, extract the emotion and score from the response
    if response.status_code == 200:
        emotions = {}
        for emotions_dict in formatted_response['emotionPredictions']:
            for key, values in emotions_dict.items():
                if "emotion" in emotions_dict.keys():
                    emotions = emotions_dict["emotion"]
                    emotions["dominant_emotion"] = max(emotions, key=emotions.get)
                break
    # If the response status code is 500, set label and score to None
    elif response.status_code == 400:
        emotions = {'anger': None, 'disgust': None, 'fear': None,
         'joy': None, 'sadness': None, 'dominant_emotion': None}

    # Return the text from response
    return emotions