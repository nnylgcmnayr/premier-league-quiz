import base64
import json
from google.cloud import firestore
from datetime import datetime, timezone

def score_to_firestore(event, context):
    """Cloud Function triggered by Pub/Sub to write score to Firestore."""
    
    # Decode Pub/Sub message
    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    score_data = json.loads(pubsub_message)
    
    # Write to Firestore
    db = firestore.Client()
    doc_ref = db.collection('scores').document()
    doc_ref.set({
        'player_name': score_data.get('player_name'),
        'score': score_data.get('score'),
        'game_duration': score_data.get('game_duration'),
        'correct_answers': score_data.get('correct_answers'),
        'wrong_answers': score_data.get('wrong_answers'),
        'total_questions': score_data.get('total_questions'),
        'timestamp': score_data.get('timestamp'),
        'scenario': score_data.get('scenario'),
        'processed_at': datetime.now(timezone.utc).isoformat()
    })
    
    print(f"Score written to Firestore for player: {score_data.get('player_name')}")
