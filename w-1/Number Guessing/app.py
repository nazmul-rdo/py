from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        guess = int(request.form.get('guess'))
        number_to_guess = 42  # Replace with your random number logic
        if guess < number_to_guess:
            message = "Too low!"
        elif guess > number_to_guess:
            message = "Too high!"
        else:
            message = "Congratulations! You guessed the number."
        return render_template('index.html', message=message)
    return render_template('index.html', message='Guess a number between 1 and 100')

if __name__ == "__main__":
    app.run(debug=True)
