from manim import *
from Earner import Earner 
from Rider import Rider


earners = [
    Earner("Yuu", [lambda x: x, lambda x: x, lambda x: x, lambda x: x], [False, False, False, False], (0,0), 5),
    Earner("Francesco", [lambda x: x, lambda x: x, lambda x: x, lambda x: x], [False, False, False, False], (0,0), 5),
]

riders = [
    Rider("Maam", (1,1), 10, 1, 5),
    Rider("Ana", (2,2), 20, 0, 4),
]


class BipartiteMatching(Scene):
    def construct(self, num_pairs=4):
        x_scale = 1.0
        y_scale = 1.0

        # Positions for nodes
        left_nodes = [(-3*x_scale, i*y_scale, 0) for i in range(2, 3 - num_pairs*2, -2)]
        right_nodes = [(3*x_scale, i*y_scale, 0) for i in range(2, 3 - num_pairs*2, -2)]

        # Create node circles
        left_circles = [Circle(radius=0.3, color=BLUE).move_to(pos) for pos in left_nodes]
        right_circles = [Circle(radius=0.3, color=ORANGE).move_to(pos) for pos in right_nodes]

        # Create labels
        left_labels = [Text(earners[i].name, font_size=24).next_to(c, LEFT) for i, c in enumerate(left_circles)]
        right_labels = [Text(riders[i].name, font_size=24).next_to(c, RIGHT) for i, c in enumerate(right_circles)]

        # Draw nodes and labels
        self.play(*[Create(c) for c in left_circles + right_circles],
                  *[Write(l) for l in left_labels + right_labels])

        # Define edges
        edges = [
            (0, 0), (0, 1),
            (1, 1),
            (2, 1), (2, 2)
        ]

        edge_lines = []
        edge_labels = []

        for i, j in edges:
            # Draw the line
            line = Line(left_circles[i].get_center(), right_circles[j].get_center(), color=GRAY, stroke_opacity=0.3)
            edge_lines.append(line)

            # Compute compatibility score using Earner method
            vector = earners[i].compute_rider_vector(riders[j])
            score = earners[i].compute_compatibility_rider(vector)

            # Place score text at midpoint
            midpoint = (left_circles[i].get_center() + right_circles[j].get_center()) / 2
            label = Text(f"{score:.2f}", font_size=18).move_to(midpoint)
            edge_labels.append(label)


        # Draw edges and labels
        self.play(*[Create(e) for e in edge_lines])
        self.play(*[Write(l) for l in edge_labels])

        # Highlight a matching path (example)
        match = [(0, 0), (1, 1), (2, 2)]
        match_lines = [Line(left_circles[i].get_center(), right_circles[j].get_center(), color=GREEN, stroke_width=6)
                       for i, j in match]

        self.wait(1)
        for ml in match_lines:
            self.play(Create(ml))
            self.wait(0.5)
