# Driven by Preferences

This is a proof-of-concept project for the JunctionXDelft 2025 Hackathon. The topic improving Earners; (Drivers') experience. We have chosen to take an approach to try giving them agency in termos of their safety, profits and work-life balance in a computationally efficient manner. 

Link to the YT Pitch Here: [Link](https://youtu.be/7uvhT0awkrw)

This repository features abstract Earner and Rider structures, as well as a structure using a basic version of bipartite matching to connect drivers with each other, based on some preference features. Comments are welcome!

## Installation guide

Both these guides should work for Windows, chocolatey is supposed to be more reliable. Try both if one doesn't work!

## OptionA: Install with Conda
````
conda create -n manim_env python=3.10
conda activate manim_env

# Core math libs from conda (binary-safe)
conda install -c conda-forge numpy scipy

# Manim from pip
pip install manim
````

## OptionB: Install with Chocolatey
https://willhoffer.com/2024-10-23/how-to-install-manim-on-windows/

1. Open Windows Powershell as administrator
2. Run `Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))`

### Notes
- If using VScode, install the `Manim Sideview` extension.
- Test if working on file `square_to_circle.py`


## Run the file
`manim -pql bipartite_matching.py WeightedBipartiteMatching`
`manim -pql sum_of_weights.py WeightedSum`
`manim -pql alices_match.py WeightedSum`

