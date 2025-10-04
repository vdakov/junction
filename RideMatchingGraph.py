import numpy as np
from Earner import Earner
from Rider import Rider

class RideMatchingGraph:
    def __init__(self, riders, earners):
        self.riders = riders  
        self.earners = earners  
        # edges stored as dict: (earner_index, rider_index) -> raw score
        self.raw_edges = {}  
        # normalized edges: (earner_index, rider_index) -> score in [0,1]
        self.edges = {}
        self.initialize_edges()
        self.print_edges()

    def initialize_edges(self):
        """Initialize edges for all current earners and riders"""
        for i, e in enumerate(self.earners):
            for j, r in enumerate(self.riders):
                score = e.compute_compatibility_rider(e.compute_compatibility_vector(r))
                if score > 0:
                    self.raw_edges[(i, j)] = score
        self._normalize_edges()

    def _normalize_edges(self):
        """Normalize all edges to 0-1 range"""
        if not self.raw_edges:
            self.edges = {}
            return
        max_score = max(self.raw_edges.values())
        if max_score == 0:
            self.edges = {k: 0 for k in self.raw_edges}
        else:
            self.edges = {k: v / max_score for k, v in self.raw_edges.items()}

    def calculateEdgeScoresNewEarner(self, earner):
        """Add edges from new earner to all existing riders"""
        i = len(self.earners)
        self.earners.append(earner)
        for j, r in enumerate(self.riders):
            score = earner.compute_compatibility_rider(earner.compute_compatibility_vector(r))
            if score > 0:
                self.raw_edges[(i, j)] = score
        self._normalize_edges()
        return { (i, j): self.edges[(i,j)] for j in range(len(self.riders)) if (i,j) in self.edges }

    def calculateEdgeScoreNewRider(self, rider):
        """Add edges from all existing earners to new rider"""
        j = len(self.riders)
        self.riders.append(rider)
        for i, e in enumerate(self.earners):
            score = e.compute_compatibility_rider(e.compute_compatibility_vector(rider))
            if score > 0:
                self.raw_edges[(i, j)] = score
        self._normalize_edges()
        return { (i, j): self.edges[(i,j)] for i in range(len(self.earners)) if (i,j) in self.edges }

    def print_edges(self):
        print("Current normalized edges (earner_index, rider_index) -> score [0-1]:")
        for key, val in self.edges.items():
            i, j = key
            print(f"  {self.earners[i].name} -> {self.riders[j].name} : {val:.2f}")
