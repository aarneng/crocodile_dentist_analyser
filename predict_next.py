avg_change = 3
variance = 1

# TODO: whole algorithm

def predict_next(last_rolls):
    if not last_rolls:
        return [5]  # return a random number as it's impossible to predict
    prev = last_rolls[-1]
    if prev in (1, 2):
        return [prev + avg_change + i for i in range(-variance, variance + 1)]
    if prev in (6, 7, 8, 9):
        return [prev + 5 + avg_change + i for i in range(-variance, variance + 1)]
    
