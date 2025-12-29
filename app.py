from flask import Flask, jsonify, request

app = Flask(__name__)

users = []

@app.route("/")
def home():
    return "REST API is running"

# GET – Read users
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)

# POST – Create user
@app.route("/users", methods=["POST"])
def create_user():
    data = request.json
    user = {
        "id": len(users) + 1,
        "name": data["name"],
        "email": data["email"]
    }
    users.append(user)
    return jsonify(user), 201

# PUT – Update user
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    for user in users:
        if user["id"] == user_id:
            user.update(request.json)
            return jsonify(user)
    return jsonify({"error": "User not found"}), 404

# DELETE – Delete user
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    global users
    users = [u for u in users if u["id"] != user_id]
    return jsonify({"message": "User deleted"})

if __name__ == "__main__":
    app.run(debug=True)
