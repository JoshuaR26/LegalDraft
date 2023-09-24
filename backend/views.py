from difflib import get_close_matches 

import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

import re
from flask import Blueprint, render_template, request
import json

views = Blueprint(__name__,"views")

data_path = 'a.json'

with open(data_path,'r') as file:
    data = json.load(file)

@views.route("/")
def home():
    return render_template("chatbot.html",ipc="dictionary")

@views.route("/",methods=['post'])
def profile():
    #args = request.args
    name = request.form['u']
    
   



    def find_best_match(user_query, keywords):
        matches = get_close_matches(user_query, keywords, n=3, cutoff=0.3)
        return matches if matches else None

    def get_section(keyword, data):
        for s in data['sections']:
            if s['keywords'] == keyword:
                return [s['number'], s['section']]

    def clean_input(user_input):

        stop_words = stopwords.words('english')
        
        lem = WordNetLemmatizer()
        
        user_input= re.sub(r'[^\w]', ' ', user_input)
        user_input = re.sub(r'\s\s*', ' ', user_input)

        user_input = lem.lemmatize(user_input)
        user_input = nltk.word_tokenize(user_input.lower())
        
        for word in user_input:
            if word in stop_words:
                user_input.remove(word)
                
        user_input = sorted(set(user_input))
        user_input = ' '.join(user_input)

        return user_input

    def chatbot(data,name: str):
        count = 0 
        while count<1:
            count +=1
            user_input = name
        
            if user_input == 'exit':
                break
            else:
                user_input = clean_input(user_input)
            
            best_match = find_best_match(user_input, [s['keywords'] for s in data['sections']])

            for i in range(3):
                cnt = 1
                if best_match:
                    law = get_section(best_match[i], data)
                    output =  f'BOT: {law[0]}:\n{law[1]}' 
                    return output #print()
                else:
                    break
            
            print('Kindly enter a more detailed report that contains strong keywords to help you out in your case.')

    chatbot(data, name)

