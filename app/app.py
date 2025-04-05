from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    names = ["Emmanuel A", "Oliseh Gift", "Ruth Ekiyor"]
    return f"<h2>I am almost a DevOps Engineer</h2><p>Team Members: {', '.join(names)}</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0')

