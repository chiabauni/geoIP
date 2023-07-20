class Statistic: 
    def __init__(self, min_distance, max_distance, mean_distance, total_invocations):
        self.min_distance = min_distance
        self.max_distance = max_distance
        self.mean_distance = mean_distance
        self.total_invocations = total_invocations

    def get_min_distance(self):
        return self.min_distance

    def get_max_distance(self):
        return self.max_distance

    def get_mean_distance(self):
        return self.mean_distance

    def get_total_invocations(self):
        return self.total_invocations
    
    def set_min_distance(self, min_distance):
        self.min_distance = min_distance

    def set_max_distance(self, max_distance):
        self.max_distance = max_distance

    def set_mean_distance(self, new_distance):
        self.mean_distance = ((self.mean_distance * (self.total_invocations-1)) + new_distance) / self.total_invocations
    
    def add_total_invocations(self):
        self.total_invocations += 1
