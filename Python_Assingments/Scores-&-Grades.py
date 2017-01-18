

#Function Which shows Grade

def grade(score):
    if score > 100:
        return "wrong score"
    if score >= 90:
        return 'Score: ' + str(score)+":"+ 'You are grade A.'
    if score >= 80:
        return 'Score: ' + str(score)+":"+ 'You are grade B.'
    if score >= 70:
        return 'Score: ' + str(score)+":"+ 'You are grade C.'
    if score >= 65:
        return 'Score: ' + str(score)+":"+ 'You are grade D.'
    if score >=60:
        return 'Score: ' + str(score)+":"+ 'You are grade E.'
    else:
        return 'End of the program. Bye!'

score =64
print grade(score)
