from flask import Flask, jsonify

app = Flask(__name__)

# بيانات المستخدمين والمخرجات الفائتة
users = [
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
    }
]

@app.route('/', methods=['GET'])
def get_users():
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)
