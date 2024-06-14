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
    {
        "id": 6,
        "mood": "مشمئز",
        "photo": "/storage/images/tdruUCuQYpMp2sSvNeZlaMYfsR4S7MiSFtWRjbE6.jpg",
        "description": "مشمئز",
        "created_at": "2024-04-01 21:07:38",
        "updated_at": "2024-04-01 21:07:38"
    },
    {
        "id": 7,
        "mood": "غضبان",
        "photo": "/storage/images/zfFIiVxqdiLt9WPajXilzqPXzUxYRNhwDiMwBrik.jpg",
        "description": "غضبان",
        "created_at": "2024-04-01 21:07:38",
        "updated_at": "2024-04-01 21:07:38"
    },
    {
        "id": 8,
        "mood": "متوتر",
        "photo": "/storage/images/EJzOgi9l5gqNesNgELqBXKShbOqda9HLOHM3YrX4.jpg",
        "description": "متوتر",
        "created_at": "2024-04-01 21:07:38",
        "updated_at": "2024-04-01 21:07:38"
    },
    {
        "id": 14,
        "mood": "متحير",
        "photo": "/storage/images/9hV06H3g0j2reFE6lp7Ark3h6YikZqB09AmLuphx.jpg",
        "description": "متحير",
        "created_at": "2024-04-01 21:07:38",
        "updated_at": "2024-04-01 21:07:38"
    },
    {
        "id": 15,
        "mood": "متحمس",
        "photo": "/storage/images/LwPkGUkHtE7OJHcfO8va1ZL5YdwwzrD0mn3awxTA.jpg",
        "description": "متحمس",
        "created_at": "2024-04-01 21:07:38",
        "updated_at": "2024-04-01 21:07:38"
    },
    {
        "id": 16,
        "mood": "خجول",
        "photo": "/storage/images/QpEWPAD2p9EdQFhNzF7jaSuSvLDstMhzAxqIrdAF.jpg",
        "description": "خجول",
        "created_at": "2024-04-01 21:07:38",
        "updated_at": "2024-04-01 21:07:38"
    },
    {
        "id": 18,
        "mood": "سعيد",
        "photo": "/storage/images/6HhXp12haPEFpauevhxoI2FhODb05Ir4qgoU2lzG.jpg",
        "description": "سعيد",
        "created_at": "2024-04-01 21:07:38",
        "updated_at": "2024-04-01 21:07:38"
    }
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
