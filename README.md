# Asteroids Game 

Classic asteroids game implemented in Python using the [Pygame](https://www.pygame.org/) library, with some features like explosions added on top of it.

## Features

* Ship that can move and shoot
* Asteroids that break into smaller asteroids when hit
* Explosions when asteroids are hit
* Random asteroid generation, with different sizes, shapes and colors
* Score counter
* Lives counter

## Installation

1. Clone the repository
    ```bash
    git clone https://github.com/igorplebanczyk/asteroids-game.git
     ```
   
2. Confirm that Python 3 is installed
    ```bash
    python3 --version
    ```
   
3. Install the required packages
    ```bash
    pip install -r requirements.txt
    ```

## Usage
* Run the game
    ```bash
    python -m asteroids-game
    ```
* Controls:
  * `W` `S` - Move forward/backward 
  * `A` `D` - Rotate left/right
  * `Space` - Shoot
  * `Shift` - Accelerate

* Game properties can be modified in the `constants.py` file

## Notes
* Recommended python version: `3.10` or higher
* Originally designed as part of a guided project on [boot.dev](https://www.boot.dev/lessons/5be3e3bd-efb5-4664-a9e9-7111be783271), but has since been significantly improved
* It was primarily built as a learning exercise
* TODO:
    * Make hitboxes match the actual shape
    * Add a nicer background
    * Make asteroids bounce off each other