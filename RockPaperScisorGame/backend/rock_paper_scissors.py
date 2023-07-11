from flask import Flask, request, jsonify
import random
from dotenv import load_dotenv
load_dotenv()
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

user_score = 0
computer_score = 0
draws = 0

@app.route('/play', methods=['POST'])
def play_game():
    try:
        # Get user's choice from the request body
        user_choice = request.json.get('choice')

        # Validate user's choice
        if not user_choice or user_choice not in ["rock", "paper", "scissors"]:
            error_message = "Invalid choice. Please choose rock, paper, or scissors."
            return jsonify({'error': error_message}), 400

        # Generate computer's choice randomly
        choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)
        
        # Compare the choices and determine the winner
        result = determine_winner(user_choice, computer_choice)
        
        # Update scores
        update_scores(result)
        
        # Prepare response data
        response_data = {
            'user_choice': user_choice,
            'computer_choice': computer_choice,
            'result': result,
            'user_score': user_score,
            'computer_score': computer_score,
            'draws': draws
        }
        
        # Return the response as JSON
        return jsonify(response_data), 200
    
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return jsonify({'error': error_message}), 500

@app.route('/resetgame')
def check():
    try:
        user_score=0
        draws=0
        computer_score=0
        response_data = {
             'user_score': user_score,
             'computer_score': computer_score,
             'draws': draws
        }
        return jsonify(response_data), 200

    except Exception as e:
        error_message=f"An error occured: {str(e)}"
        return jsonify({'error':error_message}), 500




def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "draw"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def update_scores(result):
    global user_score, computer_score, draws
    if result == "user":
        user_score += 1
    elif result == "computer":
        computer_score += 1
    else:
        draws += 1

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
