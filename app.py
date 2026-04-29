from flask import Flask, request, render_template
import os
from main import scan_file

app = Flask(__name__)

os.makedirs("uploads", exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    results = []

    if request.method == "POST":
        file = request.files.get("file")

        if file and file.filename != "":
            filepath = os.path.join("uploads", file.filename)
            file.save(filepath)
            results = scan_file(filepath)

    # 🔥 Dashboard stats
    high_count = sum(1 for item in results if item.get("risk") == "HIGH")
    medium_count = sum(1 for item in results if item.get("risk") == "MEDIUM")
    total_count = len(results)

    return render_template(
        "index.html",
        results=results,
        high=high_count,
        medium=medium_count,
        total=total_count
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)