from manim import *
from random import choice, randint, uniform
import numpy as np

class MicrosoftFabricLove(Scene):
    def construct(self):
        # Modern gradient background
        gradient = Rectangle(width=14, height=24, fill_opacity=1)
        gradient.set_fill([BLUE_D, "#0078D4", PURPLE_B])
        self.add(gradient)
        
        # Microsoft Fabric logo (text fallback)
        logo = Text("Microsoft Fabric", font="Segoe UI", weight=BOLD, font_size=64)
        logo.set_color_by_gradient(WHITE, "#FFB900")
        self.play(SpinInFromNothing(logo), run_time=1.5)
        self.wait(0.3)
        
        # Pulsing heart animation
        heart = Text("❤️", font_size=120)
        heart.next_to(logo, DOWN, buff=0.5)
        
        # Continuous heart pulse using add_updater instead of Updater
        def pulse_heart(mob, dt):
            mob.scale(1 + 0.05 * np.sin(2 * np.pi * dt))
        
        heart.add_updater(pulse_heart)
        self.add(heart)
        
        # Fireworks show
        for _ in range(12):
            self.play(self.create_firework(), run_time=0.3)
        
        # Glowing particles background
        particles = VGroup(*[self.create_particle() for _ in range(50)])
        self.add(particles)
        
        # Trendy text reveal
        text = Text("I LOVE\nMICROSOFT FABRIC", font_size=72, weight=BOLD)
        text.set_color_by_gradient("#FFB900", "#D83B01")
        text.set_stroke(BLACK, 5, background=True)
        
        self.play(
            FadeOut(logo),
            Write(text, run_time=1.5),
            Flash(text.get_center(), color=YELLOW, line_length=1.5)
        )
        
        # Hashtag elements
        hashtags = VGroup(
            Text("#MicrosoftFabric", font_size=32),
            Text("#DataRevolution", font_size=32),
            Text("#TrendingTech", font_size=32)
        )
        hashtags.arrange(DOWN, buff=0.3)
        hashtags.next_to(text, DOWN, buff=1)
        
        self.play(
            LaggedStart(*[FadeIn(h, shift=UP*0.5) for h in hashtags], lag_ratio=0.2),
            run_time=2
        )
        
        self.wait(3)
    
    def create_firework(self):
        colors = ["#FFB900", "#D83B01", "#B4009E", "#008272", "#0078D4"]
        center = np.array([randint(-5,5), randint(-3,3), 0])
        
        particles = VGroup()
        for _ in range(25):
            p = Dot(radius=0.08)
            p.set_color(choice(colors))
            p.move_to(center)
            particles.add(p)
        
        animations = []
        for p in particles:
            end = center + np.array([uniform(-2,2), uniform(-2,2), 0])
            animations.append(p.animate.move_to(end).set_opacity(0))
        
        return AnimationGroup(
            Create(particles),
            LaggedStart(*animations, lag_ratio=0.05),
            run_time=1.5
        )
    
    def create_particle(self):
        p = Dot(radius=uniform(0.02, 0.1))
        p.set_color(choice([WHITE, "#FFB900", "#D83B01"]))
        p.set_opacity(uniform(0.3, 0.8))
        p.move_to(np.array([uniform(-7,7), uniform(-12,12), 0]))
        
        # Add floating animation
        p.original_pos = p.get_center()
        p.float_speed = uniform(0.5, 1.5)
        p.float_distance = uniform(0.1, 0.3)
        
        def update_particle(mob, dt):
            mob.move_to(mob.original_pos + np.array([
                0,
                mob.float_distance * np.sin(mob.float_speed * self.time),
                0
            ]))
        
        p.add_updater(update_particle)
        return p