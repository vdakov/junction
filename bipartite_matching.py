from manim import *
import numpy as np

class WeightedBipartiteMatching(Scene):
    def construct(self):
        self.camera.background_color = "#191919"

        left_nodes = ["A", "B", "C"]
        right_nodes = ["1", "2"]

        # Edge weights: values between 0 and 1
        edges = {
            ("A", "1"): 0.91, ("A", "2"): 0.34,
            ("B", "2"): 0.72, 
            ("C", "1"): 0.45, ("C", "2"): 0.7,
        }

        # Example matching (note: only existing edges will be highlighted)
        matching = {("A", "1"), ("B", "2")}  # ("C","2") does NOT exist, will be ignored

        bottom_of_screen = -2

        def spaced_positions(n, top=3, bottom=-2):
            if n == 1:
                return [ORIGIN]
            step = (top - bottom) / (n - 1)
            return [UP * (top - i * step) for i in range(n)]

        left_positions = [p + LEFT * 3 for p in spaced_positions(len(left_nodes), top=2.2, bottom=bottom_of_screen)]
        right_positions = [p + RIGHT * 3 for p in spaced_positions(len(right_nodes), top=2.2, bottom=bottom_of_screen)]

        left_nodes_vg = VGroup(*[Circle(radius=0.3, color=ORANGE).move_to(p) for p in left_positions])
        right_nodes_vg = VGroup(*[Circle(radius=0.3, color=YELLOW).move_to(p) for p in right_positions])

        left_labels = VGroup(*[Text(n, font_size=26).move_to(node) for n, node in zip(left_nodes, left_nodes_vg)])
        right_labels = VGroup(*[Text(n, font_size=26).move_to(node) for n, node in zip(right_nodes, right_nodes_vg)])

        driver_label = Text("Driver", font_size=30).next_to(left_nodes_vg, UP, buff=0.6)
        passenger_label = Text("Passenger", font_size=30).next_to(right_nodes_vg, UP, buff=0.6)

        everything = VGroup(driver_label, passenger_label, left_nodes_vg, right_nodes_vg, left_labels, right_labels)
        everything.shift(DOWN * 0.5)

        # Animate headers and nodes
        self.play(Write(driver_label), Write(passenger_label))
        self.wait(0.5)

        self.play(
            LaggedStartMap(FadeIn, left_nodes_vg, lag_ratio=0.15),
            LaggedStartMap(FadeIn, right_nodes_vg, lag_ratio=0.15),
            LaggedStartMap(FadeIn, left_labels, lag_ratio=0.15),
            LaggedStartMap(FadeIn, right_labels, lag_ratio=0.15),
        )
        self.wait(0.5)

        # Draw edges with weights
        edge_objects = []
        placed_labels = []
        min_dist = 0.3

        for (u, v), w in edges.items():
            i = left_nodes.index(u)
            j = right_nodes.index(v)
            start = left_nodes_vg[i].get_center()
            end = right_nodes_vg[j].get_center()

            direction = end - start
            unit_dir = direction / np.linalg.norm(direction)
            offset = unit_dir * 0.31  # same as your circle radius
            line = Line(start + offset, end - offset, stroke_width=2, color=GRAY)   
            base_pos = (start + end) / 2 + UP * 0.3

            final_pos = np.copy(base_pos)
            for prev_pos in placed_labels:
                if np.linalg.norm(final_pos - prev_pos) < min_dist:
                    final_pos = (start + end) / 2 + DOWN * 0.3
                    break

            label = Text(f"{w:.2f}", font_size=22).move_to(final_pos)
            placed_labels.append(final_pos)
            edge_objects.append(((u, v), line, label))

            self.play(Create(line), FadeIn(label), run_time=0.3)

        self.wait(0.5)

        # Highlight only existing edges in the matching
        highlight_lines = []
        for (u, v) in matching:
            if (u, v) not in edges:
                continue  # skip nonexistent edges
            i = left_nodes.index(u)
            j = right_nodes.index(v)
            start = left_nodes_vg[i].get_center()
            end = right_nodes_vg[j].get_center()
            direction = end - start
            unit_dir = direction / np.linalg.norm(direction)
            offset = unit_dir * 0.32
            highlight_line = Line(start + offset, end - offset, stroke_width=6, color="#2dad5a")
            highlight_lines.append(highlight_line)
            self.play(Create(highlight_line), run_time=0.4)
            self.wait(0.2)

        # Fade out all non-matching edges and their labels
        fade_outs = []
        for (u, v), line, label in edge_objects:
            if (u, v) not in matching:
                fade_outs.append(FadeOut(line))
                fade_outs.append(FadeOut(label))

        self.play(*fade_outs, run_time=1.2)
        self.wait(2)
