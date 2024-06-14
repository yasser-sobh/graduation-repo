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
    {
        "id": 2,
        "name": "هاله محمد احمد",
        "age": 12,
        "phone": "01254796325",
        "email": "yyyyyyyy@fff.com",
        "email_verified_at": None,
        "password": "$heldhliajlijkCCz8uwkeo7EmcYuQwViqEeSAVsJQB/I1sOS1Xd6",
        "remember_token": None,
        "created_at": "2024-04-01 21:07:38",
        "updated_at": "2024-04-01 21:07:38"
    },
    {
        "id": 3,
        "name": "محمد احمد محمد",
        "age": 9,
        "phone": "01258749654",
        "email": "ddffy2005ff@gamile.com",
        "email_verified_at": None,
        "password": "$heldhliajlijkCCz8uwkeo7EmcYuQwViqEeSAVsJQB/I1sOS1Xd6",
        "remember_token": None,
        "created_at": "2024-04-01 21:07:38",
        "updated_at": "2024-04-01 21:07:38"
    },
    {
        "id": 4,
        "name": "عبده خالد",
        "age": 4,
        "phone": "01478536987",
        "email": "abido2002@gamile.com",
        "email_verified_at": None,
        "password": "$heldhliajlijkCCz8uwkeo7EmcYuQwViqEeSAVsJQB/I1sOS1Xd6",
        "remember_token": None,
        "created_at": "2024-04-01 21:07:38",
        "updated_at": "2024-04-01 21:07:38"
    },
    {
        "id": 5,
        "name": "عبد العزيز خالد دسوقي",
        "age": 4,
        "phone": "01254789543",
        "email": "abdo2002@gmail.com",
        "email_verified_at": None,
        "password": "$heldhliajlijkCCz8uwkeo7EmcYuQwViqEeSAVsJQB/I1sOS1Xd6",
        "remember_token": None,
        "created_at": "2024-04-01 21:07:38",
        "updated_at": "2024-04-01 21:07:38"
    },
    {
        "id": 6,
        "name": "محمد خطاب",
        "age": 9,
        "phone": "01254789584",
        "email": "mohek2002@gmail.com",
        "email_verified_at": None,
        "password": "$heldhliajlijkCCz8uwkeo7EmcYuQwViqEeSAVsJQB/I1sOS1Xd6",
        "remember_token": None,
        "created_at": "2024-04-01 21:07:38",
        "updated_at": "2024-04-01 21:07:38"
    },
    {
        "id": 7,
        "name": "محمد علي",
        "age": 9,
        "phone": "01254789654",
        "email": "moheww2002@gmail.com",
        "email_verified_at": None,
        "password": "$$2y$12$xK1ADwSjjF5KjmNnn.8UReEmewLM0BqkC8/Cd6ll9/mKed4Iw8Vdq/I1sOS1Xd6",
        "remember_token": None,
        "created_at": "2024-04-01 21:07:38",
        "updated_at": "2024-04-01 21:07:38"
    },
    {
        "id": 8,
        "name": "الدسوقي الدسوقي",
        "age": 12,
        "phone": "00587463398",
        "email": "ddess200555@gmail.com",
        "email_verified_at": None,
        "password": "$$2y$12$xK1ADwSjjF5KjmNnn.8UReEmewLM0BqkC8/Cd6ll9/mKed4Iw8Vdq/I1sOS1Xd6",
        "remember_token": None,
        "created_at": "2024-04-01 21:07:38",
        "updated_at": "2024-04-01 21:07:38"
    }
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
    {
        "t_insert_text": "احفظ قران اليوم",
        "t_id": 13,
        "user_id": 2,
        "is_completed": True,
        "created_at": "2024-04-01 21:07:38",
        "updated_at": "2024-04-01 21:07:38"
    },
    {
        "t_insert_text": "ذاكر اليوم ",
        "t_id": 11,
        "user_id": 4,
        "is_completed": False,
        "created_at": "2024-04-01 21:07:38",
        "updated_at": "2024-04-01 21:07:38"
    },
    {
        "t_insert_text": "اذهب الى المدرسة",
        "t_id": 8,
        "user_id": 5,
        "is_completed": False,
        "created_at": "2024-04-01 21:07:38",
        "updated_at": "2024-04-01 21:07:38"
    }
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
    {
        "id": 2,
        "score": 40,
        "level": 12,
        "start_time": "00:02:19",
        "user_id": 7,
        "admin_game_id": 1,
        "is_completed": True,
        "created_at": "2024-04-01 21:07:38",
        "updated_at": "2024-04-01 21:07:38"
    }
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
