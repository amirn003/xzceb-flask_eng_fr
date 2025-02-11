from machinetranslation import translator
from flask import Flask, render_template, request
import json
from machinetranslation import translator

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    e2f = translator.english_to_french(textToTranslate)
    return e2f

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    f2e = translator.french_to_english(textToTranslate)
    return f2e

@app.route("/")
def renderIndexPage():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
