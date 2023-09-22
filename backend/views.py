from flask import Blueprint, render_template, request
import json
from difflib import get_close_matches
views = Blueprint(__name__,"views")

@views.route("/")
def home():
    return render_template("index.html",ipc="loda")

@views.route("/",methods=['post'])
def profile():
    #args = request.args
    name = request.form['u']
    
    def load_knowledge_base(file_path : str):
        with open(file_path, 'r') as file:
            data : dict = json.load(file) 
            return data


    def save_knowledge_base(file_path : str, data : dict) :
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=2)

    def find_best_match(user_question : str, questions : list[str]):
        matches : list = get_close_matches(user_question, questions, n=2, cutoff=0.0)
        return matches if matches else None

    def get_answer(question, knowledge_base):
        for q in knowledge_base['IPC']:
            if q['number'] == question:
                return q['section']
            

    def chat_bot(name):
        knowledge_base = load_knowledge_base('knowledgebase.json')
        cnt = 0
        while cnt<1:
            cnt+=1
            user_input = name

            if user_input.lower() == 'q':
                break

            best_match = find_best_match(user_input, [q['number'] for q in knowledge_base['IPC']])

            if best_match:
                for i in range(2):
                    section = get_answer(best_match[i], knowledge_base)
                    
                    return section
    output = chat_bot(name)
    #print(output)
    return render_template("index.html",ipc = output)
        


                
                # print()
        # else:
        #     print('Bot: I dunno')
        #     new_answer = input('type ans')

        #     if new_answer.lower() != 'skip':
        #         knowledge_base['IPC'].append({'section': user_input, '': new_answer})
        #         save_knowledge_base('knowledgebase.json', knowledge_base)
        #         print('Bot: Okiedokie dickhead')

                                                           

