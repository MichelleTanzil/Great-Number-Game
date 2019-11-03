from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'A secret makes a woman woman'
random_num = random.randint(1, 100)
print(f"The random number is {random_num}")
# attempts = 0

@app.route('/')
def index():
    display = "none"
    return render_template('index.html', bgColor=session['bgColor'], display=session['display'] or display, result_text=session['result_text'])
# , attempts = session['attempts'] or attempts

@app.route('/result', methods=['POST'])
def form_output():
    session['guess'] = int(request.form['guess'])
    # session['attempts'] += 1
    print(f"The guess is {session['guess']}")
    if session['guess'] == random_num:
        session['bgColor'] = "green"
        session['display'] = "block"
        session['result_text'] = f"{random_num} was the number!"
    elif session['guess'] > random_num:
        session['bgColor'] = "red"
        session['display'] = "block"
        session['result_text'] = "Too high!"
    elif session['guess'] < random_num:
        session['bgColor'] = "red"
        session['display'] = "block"
        session['result_text'] = "Too Low!"
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
