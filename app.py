from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Citim toate imaginile din folderul tablouri pentru galerie
    path = os.path.join(app.static_folder, "images/tablouri")
    images = [f"images/tablouri/{img}" for img in os.listdir(path) if img.lower().endswith(('.jpg', '.jpeg', '.png'))]
    return render_template('index.html', images=images)

if __name__ == '__main__':
    app.run(debug=True)
