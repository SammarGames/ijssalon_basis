from flask import Flask

app=Flask(__name__)

@app.route('/')
def home():
    return "Welkom op mijn eerste Falsk-website"


@app.route('/prijzen')
def prijzen():
    return "Binnenkort verschijnen hier onze actuele prijzen"

@app.route('/recepten')
def recepten():
    return "Binnenkort verschijnen hier enkele recepten"

if __name__ == '__main__':
    app.run(port=5000,debug=True)