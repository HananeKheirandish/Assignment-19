import random

choices = ['✋' ,'✌']
score_user = 0
score_computer1 = 0
score_computer2 = 0

for i in range(5):
    user = input('Please choose between ✋ or ✌ :\n')
    computer1 = random.choice(choices)
    print(computer1)
    computer2 = random.choice(choices)
    print(computer2)
    
    if user == computer1 == computer2 :
        print('Draws!!!')
        continue
    elif user == computer1:
        score_computer2 += 1
        print('score_user:', score_user, ', score_computer1: ', score_computer1, ', score_computer2:' , score_computer2)
    elif user == computer2:
        score_computer1 += 1
        print('score_user:', score_user, ', score_computer1: ', score_computer1, ', score_computer2:' , score_computer2)
    elif computer1 == computer2 :
        score_user += 1
        print('score_user:', score_user, ', score_computer1: ', score_computer1, ', score_computer2:' , score_computer2)

winner = max(score_user, score_computer1, score_computer2)
if winner == score_user:
    print('Yuo Win!!')
elif winner == score_computer1:
    print('Computer1 Win!!')
elif winner == score_computer2 :
    print('Computer2 Win!!')
else:
    print('Draws!!')