# Upgrade pip to the latest version
python3 -m pip install --upgrade pip

# Only use this if not in GitHub Codespaces
sudo apt-get install git
sudo apt-get update

# Install ffmpeg (necessary for rendering videos)
sudo apt-get install ffmpeg

# Optional: Install required LaTeX and graphics libraries (for rendering LaTeX in Manim, if needed)
# sudo apt-get install texlive texlive-latex-extra texlive-fonts-recommended dvipng dvisvgm

# Install cairo and GObject dependencies for pycairo
sudo apt-get install libcairo2-dev libgirepository1.0-dev

# Install Pango (needed for pangocairo)
sudo apt-get install libpango1.0-dev

# Install additional software properties (for CMake or other dependencies)
sudo apt-get install -y software-properties-common

# (Optional) Add PPA for CMake and update it to a newer version, only if needed
sudo apt-add-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install cmake

# Install pangocairo library (needed for Manim)
sudo apt-get install libpangocairo-1.0-0

# Install pycairo for Python (handles graphics)
pip install pycairo

# Clone the Manim repository and install the required Python packages
git clone https://github.com/ManimCommunity/manim.git
cd manim

# Install the dependencies from the correct path
pip install -r docs/requirements.txt

# Install Manim in editable mode
pip install -e .

#run script line main.py
manim -ql main.py TestScene --output_file=test_movie.mp4

#where main.py is
from manim import *

class TestScene(Scene):
    def construct(self):
        # Create a circle
        circle = Circle()

        # Set the color and stroke width of the circle
        circle.set_stroke(color=BLUE, width=6)

        # Animate the creation of the circle
        self.play(Create(circle))

        # Add a pause at the end
        self.wait(2)
