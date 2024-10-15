from vector_generator import VectorData
from estimate_trajectory import estimate_trajectory
from checking_trajectory import TrajectoryChecker
import numpy as np

if __name__ == "__main__":
    
    vector_generator = VectorData()
    t_checker = TrajectoryChecker(alpha=0.7, epsilon=0.03, x_minmax=(-0.2, 0.2), y_minmax=(0.3, 0.5), z_minmax=(0.1, 0.8))
    

    if len(vector_generator) > 10:
        
        # dodati estimate_trajectory i dobijenu trajektoriju proslediti u t_checker.check()
        
        trajectory = np.empty()
        ret = t_checker.check()
        
        if ret is not None:
            print("Dobili smo zadovoljavajucu trajektoriju!")
