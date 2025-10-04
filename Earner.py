import numpy as np

class Earner:
    def __init__(self, name, preferences, applicable_preferences, location, rating, worktime, constraints=None):
        self.name = name
        self.preferences = preferences  # list of functions
        self.applicable_preferences = applicable_preferences  # list of bools
        self.location = np.array(location)
        self.rating = rating
        self.constraints = constraints if constraints else {}
        self.worktime = worktime

    def compute_compatibility_vector(self, rider):
        """Convert rider attributes into a vector for compatibility computation"""
        distance = np.linalg.norm(self.location - rider.location) # distance between earner and rider
        gender = rider.gender # gender of rider 
        money = rider.distance_to_travel + distance # dcost of ride
        rating = rider.rating # rating of driver 
        worktime = self.worktime # worktime of rider
        
        
        return {
            "distance": distance,
            "gender": gender,
            "money": money,
            "rating": rating,
            "worktime": worktime  
        }
          
    def compute_compatibility_rider(self, vector_dict):
        # Check constraints first
        for attr, rule in self.constraints.items():
            if not rule(vector_dict[attr]):
                return 0.0  # dealbreaker violated

        u = self.compute_preference_score(vector_dict)
        w = np.ones(len(u))  # simple uniform weights
        score = np.dot(w, u)
        return score
    
    def compute_preference_score(self, vector_dict):
        u = []
        features = ["distance", "gender", "money", "rating"]
        for i, feature in enumerate(features):
            x = vector_dict[feature]
            if self.applicable_preferences[i]:
                u.append(self.preferences[i](x))
            else:
                u.append(x)
        return np.array(u)
