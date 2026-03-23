import random

traits = {
    "tall": 1,
    "lanky": 2,
    "glasses": 2,
    "nerd_vibe": 3,
    "cute_face": 1,
    "rolled_up_sleeves":a 2,
    "messy_blonde_hair" : 4
    "bikes_to_work": 2,
    " reads' : 2
    "single": 2,
}

def generate_person():
    return {trait: random.choice([True, False]) for trait in traits}

def evaluate(person):
    score = sum(traits[t] for t in person if person[t])

    if score >= 7:
        return "Category C: Elite nerd specimen"
    elif score >= 4:
        return "Category B: Promising nerd"
    else:
        return "Category A: False alarm"

person = generate_person()

print(person)
print(evaluate(person))
