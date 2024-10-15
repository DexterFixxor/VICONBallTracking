import numpy as np


class VectorData:
    
    def __init__(self):
        self.trajectory = []
         
    def add(self, xyz : np.ndarray):
        self.trajectory.append(xyz)
        
        
    def get_trajectory(self):
        return np.array(self.trajectory)
    
    def get_velocities(self):
        return np.array(self.trajectory[1:]) - np.array(self.trajectory[:-1])


    def __len__(self):
        return len(self.trajectory)
