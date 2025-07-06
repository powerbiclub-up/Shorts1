from manim import *
from random import choice, randint, uniform
import numpy as np

class MicrosoftFabricLove(Scene):
    def __init__(self):
        super().__init__()
        self.camera.background_color = "#121212"
        self.frame_width = 9
        self.frame_height = 16
        self.camera.frame_width = self.frame_width
        self.camera.frame_height = self.frame_height
    
    def construct(self):
        # Modern gradient background
        gradient = Rectangle(
            width=self.frame_width * 1.2, 
            height=self.frame_height * 1.2, 
            fill_opacity=1
        )
        gradient.set_fill([BLUE_D, "#0078D4", PURPLE_B])
        self.add(gradient)
        
        # Microsoft Fabric logo
        logo = Text("Microsoft Fabric", font="Segoe UI", weight=BOLD, font_size=2.5)
        logo.set_color_by_gradient(WHITE, "#FFB900")
        self.play(SpinInFromNothing(logo), run_time=1.5)
        self.wait(0.3)
        
        # Pulsing heart animation
        heart = Text("❤️", font_size=4)
        heart.next_to(logo, DOWN, buff=0.3)
        
        def pulse_heart(mob, dt):
            mob.scale(1 + 0.05 * np.sin(2 * np.pi * dt))
        
        heart.add_updater(pulse_heart)
        self.add(heart)
        
        # Fireworks show
        for _ in range(8):
            self.play(self.create_firework(), run_time=0.3)
        
        # Glowing particles background
        particles = VGroup(*[self.create_particle() for _ in range(30)])
        self.add(particles)
        
        # Trendy text reveal
        text = Text("I LOVE\nMICROSOFT FABRIC", font_size=3, weight=BOLD)
        text.set_color_by_gradient("#FFB900", "#D83B01")
        text.set_stroke(BLACK, 0.3, background=True)
        
        self.play(
            FadeOut(logo),
            Write(text, run_time=1.5),
            Flash(text.get_center(), color=YELLOW, line_length=0.5)
        )
        
        # Hashtag elements
        hashtags = VGroup(
            Text("#MicrosoftFabric", font_size=1.2),
            Text("#DataRevolution", font_size=1.2),
            Text("#TrendingTech", font_size=1.2)
        )
        hashtags.arrange(DOWN, buff=0.15)
        hashtags.next_to(text, DOWN, buff=0.5)
        
        self.play(
            LaggedStart(*[FadeIn(h, shift=UP*0.2) for h in hashtags], lag_ratio=0.2),
            run_time=1.5
        )
        
        self.wait(3)
    
    def create_firework(self):
        colors = ["#FFB900", "#D83B01", "#B4009E", "#008272", "#0078D4"]
        center = np.array([
            uniform(-self.frame_width/2, self.frame_width/2),
            uniform(-self.frame_height/3, self.frame_height/3),
            0
        ])
        
        particles = VGroup()
        for _ in range(20):
            p = Dot(radius=0.05)
            p.set_color(choice(colors))
            p.move_to(center)
            particles.add(p)
        
        animations = []
        for p in particles:
            end = center + np.array([
                uniform(-1, 1),
                uniform(-1, 1),
                0
            ])
            animations.append(p.animate.move_to(end).set_opacity(0))
        
        return AnimationGroup(
            Create(particles),
            LaggedStart(*animations, lag_ratio=0.05),
            run_time=1.2
        )
    
    def create_particle(self):
        p = Dot(radius=uniform(0.01, 0.06))
        p.set_color(choice([WHITE, "#FFB900", "#D83B01"]))
        p.set_opacity(uniform(0.3, 0.8))
        p.move_to(np.array([
            uniform(-self.frame_width/2, self.frame_width/2),
            uniform(-self.frame_height/2, self.frame_height/2),
            0
        ]))
        
        # Add floating animation
        p.original_pos = p.get_center()
        p.float_speed = uniform(0.5, 1.5)
        p.float_distance = uniform(0.05, 0.15)
        
        def update_particle(mob, dt):
            mob.move_to(mob.original_pos + np.array([
                0,
                mob.float_distance * np.sin(mob.float_speed * self.time),
                0
            ]))
        
        p.add_updater(update_particle)
        return p