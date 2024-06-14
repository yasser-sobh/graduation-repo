from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

mood_card = [
    {
        "id": 5,
        "mood": "مذعور",
        "photo": "/storage/images/xSvLqiTfMjAPE0hYEwB0v93ZETTrln2It0h1lplg.jpg",
        "description": "مذعور",
        "created_at": "2024-04-01 21:07:38",
        "updated_at": "2024-04-01 21:07:38"
    },
    # (البقية هنا)
]

Users = [
    {
        "id": 1,
        "name": "محمد الدسوقي",
        "age": 7,
        "phone": "01258749635",
        "email": "moha@klhilhih",
        "email_verified_at": None,
        "password": "$2y$12$QinOEaJL94Xt6kCCz8uwkeo7EmcYuQwViqEeSAVsJQB/I1sOS1Xd6",
        "remember_token": None,
        "created_at": "2024-04-01 21:07:38",
        "updated_at": "2024-04-01 21:07:38"
    },
    # (البقية هنا)
]

current_date = datetime.now().date()

def get_user_mood(user_id, current_date):
    user_mood = None
    for mood_entry in mood_card:
        mood_created_date = datetime.strptime(mood_entry["created_at"], "%Y-%m-%d %H:%M:%S").date()
        if mood_created_date == current_date and mood_entry["id"] == user_id:
            user_mood = mood_entry["mood"]
            break
    return user_mood

@app.route('/users/<int:user_id>/mood', methods=['GET'])
def user_mood(user_id):
    user = next((u for u in Users if u['id'] == user_id), None)
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    
    mood = get_user_mood(user_id, current_date)
    if mood:
        return jsonify({'user_id': user_id, 'mood': mood})
    else:
        return jsonify({'user_id': user_id, 'mood': 'لم يُسجل'}), 404

if __name__ == '__main__':
    app.run(debug=True)
