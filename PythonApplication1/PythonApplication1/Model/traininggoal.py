from Model.training import Training
from Model.goal import Goal

#multiple inheritance
class TrainingGoal(Training, Goal):
    def __init__(self, nm, des):
        Goal.__init__(self, nm)
        Training.__init__(self, nm, des)


    def __repr__(self):
        return "goal: " + self.get_g_name() + ", training desc: " + self.get_des()
    
    def __str__(self):
        return "goal: " + self.get_g_name() + "\ntraining description: " + self.get_des()