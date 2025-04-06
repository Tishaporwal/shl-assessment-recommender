from flask import Flask, request, jsonify
import mysql.connector
from flask_cors import CORS
from sentence_transformers import SentenceTransformer, util

app = Flask(__name__)
CORS(app)

model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # Set if you use one
        database="shl_db"
    )

@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.get_json()
    query = data.get("query")

    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM assessments")
    rows = cursor.fetchall()

    assessments = []
    for row in rows:
        combined_text = f"{row['name']} {row['type']}"
        score = util.cos_sim(model.encode(query), model.encode(combined_text))[0][0].item()
        row['score'] = score
        assessments.append(row)

    top = sorted(assessments, key=lambda x: x['score'], reverse=True)[:5]
    return jsonify(top)

if __name__ == "__main__":
    app.run(debug=True)
