from flask import Flask, render_template, request
import secrets
import random

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)  # Generates a secure random key


@app.route('/', methods=['GET', 'POST'])
def index():
    number_to_guess = random.randint(1, 100)  # Random number for guessing
    if request.method == 'POST':
        try:
            guess = int(request.form.get('guess'))
        except ValueError:
            return render_template('index.html', message='Please enter a valid number.')

        if guess < number_to_guess:
            message = "Too low!"
        elif guess > number_to_guess:
            message = "Too high!"
        else:
            message = "Congratulations! You guessed the number."
        days_remaining = abs(number_to_guess - guess)  # Example: Days based on the guess
        return render_template('index.html', message=message, days_remaining=days_remaining)

    return render_template('index.html', message='Guess a number between 1 and 100')


if __name__ == "__main__":
    app.run(debug=True)
