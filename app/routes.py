from flask import render_template, flash, redirect, request, redirect
from app import app
from googletrans import Translator
import arabic_reshaper
from bidi.algorithm import get_display



@app.route('/', methods=['GET', 'POST'])
@app.route('/home')
def home():
    if request.method == "POST":
        sentence = request.form.get("englishInput")
        #return sentence
        #return redirect(request.url)
        
        translator = Translator()
        #translate sentence
        translation_ar = translator.translate(sentence, dest='ar').text
        
        
        
        
        return render_template('home.html', title='Home', sentence=sentence, translation_ar=translation_ar)




    return render_template('home.html', title='Home')

@app.route('/about')
def about():
    return render_template('about.html', title='About')

