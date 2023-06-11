import copy
import random

class Hat:
    contents = list()
    def __init__(self, **balls):
        self.contents = list()
        for color, number in balls.items():
            for i in range(number):
                self.contents.append(color)
    def draw(self, number):
        drawn_balls = list()
        if number > len(self.contents):
            pass
        else:
            for i in range(number):
                drawn_balls.append(self.contents.pop(random.randint(0, (len(self.contents)-1))))
        return drawn_balls
        

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    sucess_count = 0
    for experiments in range(num_experiments):
        balls = copy.deepcopy(hat)
        drawn_balls_dict = dict()
        drawn_balls = balls.draw(num_balls_drawn)
        for item in drawn_balls:
            drawn_balls_dict[item] = drawn_balls_dict.get(item, 0) + 1
        set = True
        for key in expected_balls.keys():
            if drawn_balls_dict.get(key, 0) < expected_balls.get(key, 0):
                set = False
        if set == True:
            sucess_count += 1
    probability = sucess_count / num_experiments if sucess_count != 0 else 1
    return probability   
                
               

            

        

hat = Hat(yellow=5,red=1,green=3,blue=9,test=1)
probability = experiment(hat=hat, expected_balls={"yellow":2,"blue":3,"test":1}, num_balls_drawn=20, num_experiments=100)
print(probability)