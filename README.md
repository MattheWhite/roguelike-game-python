<a name="readme-top"></a>


[![Contributors][contributors-shield]][contributors-url]




<!-- PROJECT LOGO -->
<br />
<div align="center">
    <img src="Pygame_logo.png" alt="Logo" width="auto" height="80">
  </a>

  <h2 align="center">Roguelike Game with Pygame</h2>

  <!-- <p align="center" style="display: none;">
    An awesome README template to jumpstart your projects!
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template">View Demo</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Report Bug</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Request Feature</a>
  </p> -->
</div>

[![Pygame][Pygame.com]][Pygame-url]


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <!-- <li><a href="#roadmap">Roadmap</a></li> -->
    <!-- <li><a href="#contributing">Contributing</a></li> -->
    <!-- <li><a href="#license">License</a></li> -->
    <li><a href="#contact">Contact</a></li>
    <!-- <li><a href="#acknowledgments">Acknowledgments</a></li> -->
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

`You are the hero we waited for ! ! !`

`During your journey, you will meet a lot of evil creatures, by defeating them you can save our world. But be careful, if you get too close to their line of sight, they will follow you and attack you.`
`If you defeat all the monsters and ghosts getting in your way, at the end you have to fight the main enemy. It won't be an easy journey, but good luck! The fate of our world depends on you` 


* An old-fashioned RPG games from the days when graphics didn't matter that much, and the most important things were gameplay and a story.

* Advanced OOP concepts are used in the project inheritance, implemented classes, all source code (every module) is written in Python and using Pygame.
Pygame is a set of Python modules designed for writing video games. Pygame adds functionality on top of the excellent SDL library. This allows you to create fully featured games and multimedia programs in the python language.

* All code is pushed to GitHub repository by atomic commits.


<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

This section list major frameworks/libraries used to build and develop the project.
As you can see, the whole project was written in Python, using Pygame modules, a big advantage of Pygame is that it is free.

[![Python][Python.org]][Python-url]
[![Pygame][Pygame.org]][Pygame-url]


_For more about Pygame, visit: [About Pygame](https://www.pygame.org/wiki/about)_


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

* python

Open up your terminal and update your local system's repository list by entering the following command:
```sh
 sudo apt update
```

Download the latest version of Python:
```sh
sudo apt install python3
```

APT will automatically find the package and install it on your computer.

### Installation
If you have Python version 3.4 or later, PIP is included by default, which is the package manager of Python.
After you have succesfully installed Python on your computer, the essential packages must be installed, and you need to clone the repo.

Below you can see the workflow of the installation:

1. Clone the repo
```sh
   git clone https://github.com/your_username_/Project-Name.git
```

2. Install Pygame
```sh
  python3 -m pip install -U pygame --user
```
   After this step you have to install some Python and Pygame specific packages.

3. Install screeninfo
   - Screeninfo package is responsible to fetch location and size of physical screens. With screeninfo the game can run on fullscreen.
```sh
   python3 -m pip install screeninfo
```

4. Install pyTMX
   - PyTMX is a map loader for python/pygame designed for games. It provides smart tile loading with a fast and efficient storage base.
```sh
   python3 -m pip install PyTMX
```
  
5. Install UI
   - UI is a simple menu-driven user interface for the terminal.
```sh
   python3 -m pip install ui
```

6. `Start the game and have fun :-)`
```sh
   python3 main.py
```
  **main.py is placed in your local repo where you cloned it**


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Here you can find the information about the control of the game.


    - Character movement:

<kbd>W</kbd>  ->  Forward

<kbd>A</kbd>  ->  Backward

<kbd>S</kbd>  ->  Left

<kbd>D</kbd>  ->  Right


    – Damages and change currently selected weapon or magic:

<kbd>Left Mouse Click</kbd> ->  Attack with weapon

<kbd>Right Mouse Click</kbd> ->  Activate magic power

<kbd>Q</kbd>  ->  Weapon change

<kbd>E</kbd>  ->  Magic change


    - Control the gameflow:

<kbd>U</kbd>  ->  Pause menu

<kbd>ESC</kbd>  ->  Quit game


    - a little extra if you are in a too hot situation

<kbd>O</kbd> + <kbd>P</kbd> ->  OP / Super mode (more healt, more speed, more damage)

<kbd>ALT</kbd>  ->  Nack to normal


_For more examples, please refer to the [Documentation](https://example.com)_


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

MattheWhite - Fehér Mátyás

[![LinkedIn][linkedin-shield]][linkedin-url]
[![GitHub][github-shield]][github-url]

Project Link: [https://github.com/MattheWhite/roguelike-game-python](https://github.com/MattheWhite/roguelike-game-python)


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/MattheWhite/roguelike-game-python.svg?style=for-the-badge
[contributors-url]: https://github.com/MattheWhite/roguelike-game-python/graphs/contributors
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=349
[linkedin-url]: https://www.linkedin.com/in/matyas-feher/
[github-shield]: https://img.shields.io/badge/-GitHub-black.svg?style=for-the-badge&logo=github&colorB=947
[github-url]: https://github.com/MattheWhite
[Python.org]: https://img.shields.io/badge/Python-black.svg?style=for-the-badge&logo=python&colorB=yellow
[Python-url]: https://python.org
[Pygame.com]: https://www.pygame.org/ftp/pygame-badge-SMA.png
[Pygame.org]: https://img.shields.io/badge/Pygame-green.svg?style=for-the-badge&logo=python&colorB=grey
[Pygame-url]: https://www.pygame.org/
