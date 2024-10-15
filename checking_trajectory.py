import numpy as np

class TrajectoryChecker:
    
    def __init__(self, alpha : float, epsilon : float, x_minmax : tuple, y_minmax : tuple, z_minmax : tuple):
        self.alpha      = alpha # EMA filter
        self.epsilon    = epsilon # DKL
        
        self.trajectory = None
        self.xyz_in_workspace = []
        self.min_max = (x_minmax, y_minmax, z_minmax)
        
        
        
    def ema(self, trajectory : np.ndarray):
        if self.trajectory is None:
            self.trajectory = trajectory
        else:
            self.trajectory = self.alpha*trajectory + (1-self.alpha) * self.trajectory # nova = alpha * nova + (1-alpha) * stara

    def check_if_in_workspace(self, trajectory : np.ndarray):
        """Checks if given trajectory is in defined workspace.
        If it is, append first XYZ that intersects the workspace to the list
        is later used for Multivariate gaussian and DKL

        Args:
            trajectory (np.ndarray): _description_
        """
        
        for i in range(len(trajectory)):
            # check each element of trajectory going backwards
            if self.min_max[0][0] < trajectory[i][0] < self.min_max[0][1]:
                if self.min_max[1][0] < trajectory[i][1] < self.min_max[1][1]:
                    if self.min_max[2][0] < trajectory[i][2] < self.min_max[2][1]:
                        self.xyz_in_workspace.append(trajectory[i])
                        return True
                    
        return False
            
    def multivariate_gaussian(self):
        cov = np.eye(3)
        mean = np.zeros(3)
        if len(self.xyz_in_workspace) > 10:
            mean = np.mean(self.xyz_in_workspace, axis=0)
            cov = np.cov(np.array(self.xyz_in_workspace).T, rowvar=True)
        return mean,cov
        
        
    def kl_divergence(self, old_mean, old_cov, new_mean, new_cov):
        raise NotImplementedError("\n\nKL_Divergence is not implemented!!!\n\n")
        return 10000
    
    
    def check(self, trajectory):
        """        
        1. primeniti EMA
        2. Proveriti da li je u workspace-u
        3. ako jeste, odradi MVG
        4. zatim odradi DKL
        
        Stavke 3. i 4. raditi samo ako imamo minimum 3 tacke u xyz_in_workspace
        
        """
        if (self.kl_divergence(0, 0, 0, 0)) < self.epsilon:
            return self.trajectory # vrati trajektoriju ukoliko je proces uspesan, odnosno DKL < epsilon
        else:
            return None
