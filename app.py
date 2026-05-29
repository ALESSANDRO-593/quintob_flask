from flask import Flask, render_template_string

app = Flask(__name__)

# Usamos render_template_string para que todo esté en un solo archivo
HTML_PAGE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Mi Página Flask</title>
    <!-- Bootstrap desde CDN -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            background: linear-gradient(135deg, #74ebd5 0%, #9face6 100%);
            font-family: 'Segoe UI', sans-serif;
        }
        .card {
            margin-top: 50px;
            border-radius: 15px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.2);
        }
        h1 {
            color: #333;
        }
    </style>
</head>
<body>
    <div class="container text-center">
        <div class="card p-5">
            <h1>🌟 Bienvenido a Flask 🌟</h1>
            <p class="lead">Esta es una página bonita hecha con Python y Flask.</p>
            <a href="https://flask.palletsprojects.com/" target="_blank" class="btn btn-primary">
                Aprende más sobre Flask
            </a>
        </div>
    </div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_PAGE)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
