# TMU Wave AUV Software Repository Onboarding
Task Distribution Guide: https://docs.google.com/document/d/1PYVXZZVbqKc5l0N-4jWKEzgkkuRrkx8ZUTT8R2Tvwa4/edit?tab=t.0

Task Distribution Tracker: https://docs.google.com/spreadsheets/d/13jqPk8_FQUEE8H4M-rOIdoNeXM-QC-CMDc386ToPW-o/edit?gid=0#gid=0

NOTE: The current file structure was created as a base for the subteam to use, if additional files need to be created then please create them with clear intention and put them in their respective folders - same goes for creating additional folders. Make sure file/folder names are clear and that ALL folders you work in include a **README**. 

Guide for WSL: https://learn.microsoft.com/en-us/windows/wsl/setup/environment#file-storage

## Required Software

Before starting, install the following:

- WSL (Windows Subsystem for Linux)
- Ubuntu 
- Visual Studio Code - https://code.visualstudio.com/
- VS Extensions
  - WSL
  - Python
  - Python Debugger
  - Pylance
  - Dev Containers
- Python 3           - https://www.python.org/downloads/
- Docker Desktop     - https://docs.docker.com/desktop/setup/install/windows-install/


Latest versions are fine for all software.

---

# Initial Repository Setup (UBUNTU):

## Open ubuntu and make a project folder

mkdir -p ~/projects

## then go into folder: 

cd ~/projects

## Clone repo: 

git clone 'https clone link'

## Go into repo: 

cd tmuWave-2026-AUV-ops

## Configure Git (first time only): 

git config --global user.name "your username/email"

## Open VS code (still from ubuntu): 

code .

## Reopen in Container:

Ctrl + Shift + P

Reopen in container

---

# Workflow

## Before Starting Work

In Ubuntu:

cd ~/projects/tmuWave-2026-AUV-ops

git pull

code .

Reopen in container

---

# Uploading Changes Through Terminal

## 1. Check Changed Files

git status

## 2. Add Files

git add .

## 3. Commit Changes

git commit -m "Describe your changes here"

Example:

git commit -m "Added OpenCV gate detection script"

## 4. Push Changes to GitHub

git push

NOTE: Double check your work was uploaded properly in github 

---

## The repository uses:

- WSL (Ubuntu)
- Docker
- VS Code Dev Containers

*all team members use the same development environment and dependencies

## The development container includes:

- Python
- OpenCV
- pymavlink
- ArduPilot / ArduSub SITL tools

QGroundControl remains installed separately on Windows.

# Important Notes

- Always pull changes before starting work
- Keep documentation updated
- Commit frequently with clear commit messages
- Avoid modifying unrelated files

# Open-source AUV/underwater robotics repos + extra resources:

https://github.com/clydemcqueen/orca4

https://github.com/fkromer/awesome-ros2

https://github.com/bluerobotics/cockpit

https://github.com/bluerobotics/BlueOS

https://github.com/ArduPilot/ardupilot

https://github.com/TMU-Wave/bluesim

https://github.com/TMU-Wave/TMUWaveSim

https://github.com/vortexntnu/vortex-auv
