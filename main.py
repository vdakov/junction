from manim import *
from Earner import Earner 
from Rider import Rider


# Riders
riders = [
    Rider("Yuu", location=np.array([0,0]), distance_to_travel=10, gender=1, rating=5),  # woman
    Rider("Georgi", location=np.array([3,0]), distance_to_travel=15, gender=0, rating=4)  # man
]

# Earner 1: wants only female
earner1 = Earner(
    "Maam",
    preferences=[lambda x:x, lambda x: 20 if x == 1 else 0, lambda x:x, lambda x:x],
    applicable_preferences=[True, True, True, True],
    location=(1.5,1.5),
    rating=5,
    worktime=4,
    constraints={"gender": lambda g: g == 1}  
)

# Earner 2: weights profit heavily
earner2 = Earner(
    "Stoyan",
    preferences=[lambda x:x, lambda x:x, lambda x: x*2, lambda x:x],
    applicable_preferences=[True, True, True, True],
    location=(1.5, -1.5),
    rating=5,
    worktime=2
)

# Earner 3: Work life balance - works more than 8 hours -> Has to chill
earner3 = Earner(
    "Chillio",
    preferences=[lambda x:x, lambda x:x, lambda x: x, lambda x:x],
    applicable_preferences=[True, True, True, True],
    location=(3, 3),
    rating=5,
    worktime=8,
    constraints={"worktime": lambda g: g < 8}  
)

earners = [earner1, earner2, earner3]

# Compute scores
for e in earners:
    print(f"Scores for {e.name}:")
    for r in riders:
        vector = e.compute_compatibility_vector(r)
        score = e.compute_compatibility_rider(vector)
        print(f"Rider {r.name}: {score:.2f}")
