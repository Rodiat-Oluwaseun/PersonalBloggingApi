from flask import Flask, request, jsonify

app = Flask(__name__)
blog_service = BlogRepository()


@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({"error": str(e)}), 500


@app.get("/posts")
def list_posts():
    posts = blog_service.fetch_all_posts()
    return jsonify(posts), 200


@app.post("/posts")
def create_post():
    data = request.get_json() or {}
    if not data.get("title") or not data.get("content"):
        return jsonify({"error": "Missing fields"}), 400

    new_id = blog_service.add_post(data['title'], data['content'])
    return jsonify({"id": new_id, "message": "Created"}), 201
