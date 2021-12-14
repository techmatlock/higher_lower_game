from game_data import data
import random
from art import logo, vs

print(logo)
score = 0
while True:
    a = random.choice(data)
    b = random.choice(data)
    if a == b:
        b = random.choice(data)
    print(f"Compare A: {a['name']}, {a['description']}, from {a['country']}.")
    print(vs)
    print(f"Against B: {b['name']}, {b['description']}, from {b['country']}.")
    response = input("Who has more followers? Type 'A' or 'B': ")
    if response == 'A':
        if a['follower_count'] > b['follower_count']:
            score += 1
            print(f"You're right. Current score: {score}.")
        elif a['follower_count'] < b['follower_count']:
            print(f"Sorry, that's wrong. Final score: {score}.")
            break
    if response == 'B':
        if b['follower_count'] > a['follower_count']:
            score += 1
            print(f"You're right. Current score: {score}.")
        elif b['follower_count'] < a['follower_count']:
            print(f"Sorry, that's wrong. Final score: {score}.")