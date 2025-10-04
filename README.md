# junction


# Installation guide

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

`manim -pql bipartite_matching_old.py WeightedBipartiteMatching`
