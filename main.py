constants.py
U

main.py
M

requirements.txt
U
1
2
3
4
5
6
7
8
9
10
11
12
13
import pygame
from constants import *


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
import pygame
from constants import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        pygame.display.flip()


if __name__ == "__main__":
    main()

