planets = ["mercury", "venus", "earth", "mars", "jupiter", "saturn","uranus","neptune"]


q_planets = [planet.upper() for planet in planets ]

show_99 = [99 for planet in planets]




def count_negatives(nums):
    n_negatives = 0
    for num in nums:
        if num < 0:
            n_negatives = n_negatives + 1
            print(n_negatives)
            return n_negatives
        
count_negatives([1, 2, -1, -3])