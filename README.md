# AR Keyboard and Mouse

The objective is to create an augmented reality interface for keypad and mousepad function.
<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Tech Stack](#tech-stack)
  * [File Structure](#file-structure)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Results and Demo](#results-and-demo)
* [Future Work](#future-work)
* [Troubleshooting](#troubleshooting)
* [Contributors](#contributors)
* [Acknowledgements and Resources](#acknowledgements-and-resources)
* [License](#license)


<!-- ABOUT THE PROJECT -->
## About The Project
![Final Scene](final.png)  

We have created a program of hand gesture recognition using OpenCV different function such as swiping, zooming and typing are performed at the required interface.
Screen of the computer is mirrored on the screen of smart phone and so the user can get the exact processing required, the main motive of using phone as input device is to make it portable. Thus, all the functions can be controlled using hand gesture

Refer this [documentation](report.pdf).

### Tech Stack
Software used for this project :  
   [V-REP/CoppeliaSim (specifically, V-REP PRO EDU 3.6.2 version has been used)](https://www.coppeliarobotics.com/)

### File Structure
    .
    ├── PickAndPlace.ttt        # Project file - Open it in V-REP and start the simulation
    ├── ExtractCoordinates.ttt  # Future work - Extracts X, Y and Z coordinates of white boxes
    ├── report.pdf              # Project report
    ├── final.png               # Screenshot of scene before simulation starts
    ├── scene.png               # Screenshot of scene during simulation
    ├── LICENSE
    └── README.md  
    

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

 CoppeliaSim/V-REP

  You can visit the [Coppelia Robotics website](https://www.coppeliarobotics.com/previousVersions) for the installation. We have used V-REP PRO EDU Version 3.6.2 for our project.
  

### Installation
Clone the repo
```sh
git clone https://github.com/Tejal-19/simbotix.git
```

<!-- USAGE EXAMPLES -->
## Usage
```
Open PickAndPlace.ttt in V-REP and start the simulation.
```


<!-- RESULTS AND DEMO -->
## Results and Demo
Scene before starting the simulation:  
  
![**Before Starting Simulation**](final.png)  
  
Scene during the simulation:  
  
![**During Simulation**](scene.png)  
  
  
[**Video of Final Scene**](https://youtu.be/Pa8bjl16Gbc)  




<!-- FUTURE WORK -->
## Future Work
* Extracting coordinates of white boxes
- [x] Add Vision Sensor
- [x] Add Blob Detection Filter
- [x] Add Vision Sensor script
- [x] Convert all coordinates to metres  
* Other possible modifications:
- [ ] Adding camera/vision sensors to detect object
- [ ] Changing the robot and gripper, or designing one
- [ ] Make the robot mobile
- [ ] Obstacle avoidance and end-to-end planning

<!-- TROUBLESHOOTING -->
## Troubleshooting
* The robotic arm moves erratically  
  Change position of target dummy. If that doesn't work, adjust the pos angles.
* The arm does not follow the path  
  Make sure all the joints are set to Inverse Kinematics mode. Also check the code to see whether path is created correctly.
* Gripper does not work  
  Disable or delete the default script of the gripper and replace it with the one used in PickAndPlace.ttt.
  


<!-- CONTRIBUTORS -->
## Contributors

* MENTORS
  1. Mr. Harshvardhan
  2. Mr. Chetan
* MEMBERS
  1. [Ms. Priti Jain](https://github.com/preetijain7681) : preetijain7681ail.com
  2. [Ms. Harshada Patil](https://github.com/Reshmika-Nambiar) : harshadapatil372@gmail.com 
<!-- ACKNOWLEDGEMENTS AND REFERENCES -->
## Acknowledgements and Resources
* [SRA VJTI](http://sra.vjti.info/) Eklavya 2019  
* 
* [Inverse Kinematics tutorial](https://youtu.be/JUiSZinyH1c)


<!-- LICENSE -->
## License
  MIT License  
  
  Copyright (c) 2020 Tejal Bedmutha and Reshmika Nambiar  
  Go to [License](LICENSE) for full license. 
 
 
