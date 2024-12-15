# Asteroids Game 

Classic asteroids game implemented in Python using the [Pygame](https://www.pygame.org/) library, with some features like explosions added on top of it.

## Features

* Ship that can move, shoot and accelerate
* Asteroids that break into smaller asteroids when hit by the player shot or collide with each other
* Explosions when asteroids are hit or collide
* Asteroids gradually speed up as the player score rises
* Random asteroid generation, with different sizes, shapes, colors and randomly placed craters
* Score counter
* Lives counter
* Pause and game over menus

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

## Assets

* [Background](https://www.behance.net/gallery/21896005/8-bit-Night)
* [Heart](https://static.vecteezy.com/system/resources/thumbnails/027/517/564/small/pixel-cartoon-heart-icon-illustration-png.png)
* [Spaceship](https://www.nicepng.com/downpng/u2q8a9y3a9r5i1r5_vector-spaces-ship-8-bit-spaceship-sprite/)

## License
This project is licensed under the MIT License - see [LICENSE](https://github.com/igorplebanczyk/asteroids-game/blob/main/LICENSE).

## Notes
* Recommended python version: `3.10` or higher
* Originally designed as part of a guided project on [boot.dev](https://www.boot.dev/lessons/5be3e3bd-efb5-4664-a9e9-7111be783271), but has since been significantly improved
* It was primarily built as a learning exercise