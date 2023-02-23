from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    videos = ['britney.mp4','jap_speech.mp4','performance.mp4', 'first_fight.mp4', 'second_fight.mp4', 'prozacs_grenades.mp4', 'proZaC_slaps.mp4', 'rail.mp4','prozac_czm.mp4','prozac_zero4.mp4']
    return render_template('index.html', videos=videos)

if __name__ == '__main__':
    app.run(debug=True)