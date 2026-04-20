from flask import Flask, render_template

app = Flask(__name__, template_folder="../templates", static_folder="../static")

@app.route("/")
def home():
    posts = [
        {"title": "첫 번째 글", "content": "안녕하세요! 블로그 시작입니다."},
        {"title": "두 번째 글", "content": "Flask + Vercel 배포 성공!"}
    ]
    return render_template("index.html", posts=posts)

# Vercel 서버리스 핸들러
def handler(request):
    return app(request.environ, lambda status, headers: None)
