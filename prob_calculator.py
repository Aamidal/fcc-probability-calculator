import copy
import random
# Consider using the modules imported above.

class Hat:
    """Create a hat oject with a variable number of colored balls as 'contents'"""
    def __init__(self, **kwargs):
        self.balls = kwargs
        self.contents = []
        for b, n in self.balls.items():
            for i in range(n):
                self.contents.append(b) 
            
    def get_contents(self):
        return self.contents

    def draw(self, x):
        """Draw balls from the hat, do not replace drawn balls
        if x > number of balls in hat, return all balls."""
        if x > len(self.contents):
            return self.contents
        else:
            self.drawn = []
            for d in range(x):
                d = random.choice(self.contents)
                self.drawn.append(d)
                self.contents.remove(d)
            return self.drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    """Calculate the probability of drawing at specified balls when a number of balls are drawn"""
    m = 0
    for e in range(num_experiments):
        x_hat = copy.deepcopy(hat)
        x_drawn = x_hat.draw(num_balls_drawn)
        x_balls = sum([1 for k, v in expected_balls.items() if x_drawn.count(k) >= v])
        m += 1 if x_balls == len(expected_balls) else 0
    
    return m / num_experiments


