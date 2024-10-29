from manim import *
import numpy as np

from manim import *
import numpy as np

class SimplifiedWaveVisualization(Scene):
    def construct(self):
        # Set up the wave
        full_width = 20
        frame = self.camera.frame

        # Create a light source
        source = GlowDot(ORIGIN, color=WHITE)
        source.set_radius(0.5)
        
        # Create a light wave slice
        wave = LightWaveSlice(source)
        wave.set_width(full_width)
        wave.move_to(ORIGIN)

        # Add the wave and source to the scene
        self.add(wave, source)

        # Create and animate the vector field
        linear_field = self.create_vector_field(wave)
        self.play(Create(linear_field), run_time=2)

        # Animate the wave
        self.play(wave.animate.set_uniform(time_rate=0.5), run_time=5)
        self.wait(2)

        # Update and show a sample vector
        sample_vect = self.create_sample_vector()
        self.play(GrowArrow(sample_vect, run_time=2))
        self.wait(3)

        # Final animation of wave
        self.play(FadeOut(sample_vect), run_time=2)
        self.play(FadeOut(wave), run_time=2)
        self.wait(2)

    def create_vector_field(self, wave):
        """Create a vector field based on the wave function."""
        def field_func(points):
            result = np.zeros_like(points)
            result[:, 2] = 0.5 * wave.wave_func(points)
            return result

        return VectorField(
            field_func,
            sample_points=np.linspace(ORIGIN, 10 * UP, 100),
            max_vect_len=1.0,
            stroke_width=1.5,
            opacity=0.75
        )

    def create_sample_vector(self):
        """Create a sample vector for demonstration."""
        sample_vect = Vector(OUT, thickness=1.0)
        sample_vect.set_fill(WHITE, 1, border_width=0.5)
        sample_vect.base_point = Dot(0.5 * UP, fill_color=BLUE, radius=0.02)
        
        # Updater function to dynamically update the sample vector
        def update_sample_vect(vect):
            point = vect.base_point.get_center()
            vect.put_start_and_end_on(point, point + 0.95 * np.array([0, 0, 0.5]))  # Example update
            vect.set_perpendicular_to_camera(self.camera)

        update_sample_vect(sample_vect)  # Initial update
        sample_vect.add_updater(update_sample_vect)  # Add updater
        return sample_vect

if __name__ == "__main__":
    scene = SimplifiedWaveVisualization()
    scene.render()
