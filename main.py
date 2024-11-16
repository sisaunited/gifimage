from flask import Flask, request, jsonify
from hanspell import spell_checker

app = Flask(__name__)

@app.route('/check', methods=['POST'])
def check():
    sentence = request.form['sentence']
    checked_sentence = spell_checker.check(sentence)
    corrected_sentence = checked_sentence.checked 
    return corrected_sentence

if __name__ == '__main__':
    app.run()