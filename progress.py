from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

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

Tasks = [
    {
        "t_insert_text": "اذهب الى المسجد",
        "t_id": 22,
        "user_id": 7,
        "is_completed": True,
        "created_at": "2024-04-01 21:07:38",
        "updated_at": "2024-04-01 21:07:38"
    },
    # (البقية هنا)
]

Games = [
    {
        "id": 1,
        "score": 40,
        "level": 12,
        "start_time": "00:00:00",
        "user_id": 7,
        "admin_game_id": 1,
        "is_completed": True,
        "created_at": "2024-04-01 21:07:38",
        "updated_at": "2024-04-01 21:07:38"
    },
    # (البقية هنا)
]

def calculate_completion_percentage(user_id):
    total_tasks = sum(1 for task in Tasks if task["user_id"] == user_id and task["is_completed"])
    total_games = sum(1 for game in Games if game["user_id"] == user_id and game["is_completed"])
    total_completed = total_tasks + total_games
    total_available = len([task for task in Tasks if task["user_id"] == user_id]) + len([game for game in Games if game["user_id"] == user_id])

    if total_available == 0:
        return 0
    else:
        return (total_completed / total_available) * 100

@app.route('/users/<int:user_id>/completion', methods=['GET'])
def user_completion(user_id):
    user = next((u for u in Users if u['id'] == user_id), None)
    if user is None:
        return jsonify({'error': 'User not found'}), 404

    completion_percentage = calculate_completion_percentage(user_id)
    return jsonify({'user_id': user_id, 'completion_percentage': completion_percentage})

if __name__ == '__main__':
    app.run(debug=True)
