from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

openai.api_key = "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"

def generate_answer(level, task, additional_requirements):
    if level == "excellent":
        prompt = f"作为一名优等生，{task}。{additional_requirements}"
    elif level == "average":
        prompt = f"作为一名中等水平的学生，{task}。{additional_requirements}"
    else:
        prompt = f"作为一名差等生，{task}。{additional_requirements}"
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1000
    )
    return response.choices[0].message.content

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    student_level = request.form['student_level']
    task = request.form['task']
    additional_requirements = request.form['additional_requirements']
    answer = generate_answer(student_level, task, additional_requirements)

    return jsonify({"response": answer})

if __name__ == '__main__':
    app.run(debug=True)
