from manim import *

class WeightedSum(Scene):
    def construct(self):
        self.camera.background_color = "#191919"

        # Separate equation parts for easier alignment
        initial_equation_font_size = 60
        initial_label_font_size = 36
        part1 = Text("edge_score = Σ ", font_size=initial_equation_font_size)
        part2 = Text("w ·", font_size=initial_equation_font_size)
        i_w = Text("i", font_size=initial_label_font_size)
        part3 = Text("u", font_size=initial_equation_font_size)
        i_u = Text("i", font_size=initial_label_font_size)
        i_w.next_to(part2, DOWN, buff=0.02).shift(RIGHT * 2.75)
        i_u.next_to(part3, DOWN, buff=0.02).shift(RIGHT * 3.75)

        # Arrange parts horizontally
        equation = VGroup(part1, part2, part3).arrange(RIGHT, buff=0.15)

        # Create labels aligned to specific parts
        label_w = Text("(global) weights", font_size=initial_label_font_size)
        label_u = Text("user properties", font_size=initial_label_font_size)

        label_w.next_to(part2, DOWN, buff=0.4).shift(LEFT * 1.5)
        label_u.next_to(part3, DOWN, buff=0.4).shift(RIGHT * 1.5)

        # Group for easy movement later
        group = VGroup(equation, label_w, label_u, i_w, i_u)

        # Animations
        self.play(Write(equation))
        self.play(Write(i_w), Write(i_u))
        self.wait(0.5)
        self.play(Write(label_w), Write(label_u))
        self.wait(0.5)

        # Move everything up and scale down slightly
        self.play(
            group.animate.scale(0.7).to_edge(UP).to_edge(LEFT),
            run_time=1.5
        )
        self.wait(1)

        # Create arrows and sublabels for user properties
        categories = [
            "safety rating",
            "weather",
            "road conditions",
            "maximize profit"
        ]

        property_texts = VGroup(*[
            Text(cat, font_size=28) for cat in categories
        ]).arrange(RIGHT, buff=1.25)

        left_screen_edge_distance_categories = 0.1
        property_texts.next_to(label_u, DOWN, buff=1).to_edge(LEFT).shift(RIGHT * left_screen_edge_distance_categories)

        # Keep references to headings and indices
        category_map = {name: text for name, text in zip(categories, property_texts)}
        cat_to_idx = {name: i for i, name in enumerate(categories)}

        # Will be filled when we create bullet lists
        sub_groups = {}

        arrows = VGroup(*[
            Arrow(
                start=label_u.get_bottom() + DOWN * 0.1,
                end=text.get_top() + UP * 0.1,
                buff=0.1,
                stroke_width=2.5,
                tip_length=0.15,  # smaller than default (~0.2)
                # tip_width=0.15    # optional: narrows the tip slightly
            )
            for text in property_texts
        ])

        for arrow, text in zip(arrows, property_texts):
            self.play(GrowArrow(arrow), FadeIn(text, shift=UP), run_time=0.6)

        self.wait(1)

        # Define sub-items for each category
        sub_items = {
            "maximize profit": [
                "longer trips",
                "passenger nearby",
                "headed to a surge area",
                "prefers airport trips",
            ],
            "safety rating": [
                "cleanliness",
                "vandalism",
                "verbal abuse",
                "law non-compliance",
                "physical aggression"
            ],
            "weather": [
                "storm warnings",
                "temperature",
                "precipitation data",
                "wind speed"
            ],
            "road conditions": [
                "surface quality",
                "construction",
                "unpaved roads",
                "slope and elevation",
                "accident-prone zones"
            ]
        }

        # Animate enumerations under each category
        for category_name, category_text in zip(categories, property_texts):
            items = sub_items.get(category_name, [])
            if not items:
                continue

            # Create list below category
            list_group = VGroup(*[
                Text(f"• {item}", font_size=20, font="Arial")
                for item in items
            ]).arrange(DOWN, aligned_edge=LEFT, buff=0.2)

            list_group.next_to(category_text, DOWN, buff=0.2, aligned_edge=LEFT).shift(RIGHT * 0.15)

            # Save reference for later color animations
            sub_groups[category_name] = list_group

            # Animate items one by one
            for item_text in list_group:
                self.play(FadeIn(item_text, shift=UP * 0.2), run_time=0.2)



        self.wait(0.5)

        green = "#00FF00"
        yellow = "#FFFF00"

        # Safety rating: heading and all bullets to green
        self.play(
            # category_map["safety rating"].animate.set_color(green),
            *[item.animate.set_color(green) for item in sub_groups.get("safety rating", VGroup())],
            run_time=0.8
        )
        self.wait(0.2)

        # Weather: heading and all bullets to green
        self.play(
            # category_map["weather"].animate.set_color(green),
            *[item.animate.set_color(green) for item in sub_groups.get("weather", VGroup())],
            run_time=0.8
        )
        self.wait(0.2)

        # Road conditions: heading to green, bullets green except "slope and elevation" in yellow
        road_items = sub_groups.get("road conditions", VGroup())
        anims = []
        # anims = [category_map["road conditions"].animate.set_color(yellow)]
        for t in road_items:
            label = t.text.replace("•", "").strip()
            # print(label)
            print(label)
            print("slope and elevation".replace(" ", ""))
            print(label == "slope and elevation".replace(" ", ""))
            anims.append(t.animate.set_color(yellow if label == "slope and elevation".replace(" ", "") else green))
        self.play(*anims, run_time=0.9)


        # Maximize profit: fade out heading, arrow, and bullets
        mp_idx = cat_to_idx["maximize profit"]
        fadeouts = [
            FadeOut(category_map["maximize profit"]),
            FadeOut(arrows[mp_idx]),
        ]
        if "maximize profit" in sub_groups:
            fadeouts.append(FadeOut(sub_groups["maximize profit"]))
        self.play(*fadeouts, run_time=0.7)
        self.wait(0.2)

        self.wait(2)
