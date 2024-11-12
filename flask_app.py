from flask import Flask

app=Flask(__name__)

@app.route('/')
def home():
    return "Welkom op mijn eerste Falsk-website"

if __name__ == '__main__':
    app.run(port=5000,debug=True)
