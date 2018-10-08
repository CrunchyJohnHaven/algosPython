# algosPython

# Setting Up Python3 Virtual Environment for Mac

Upgrade the pip version that comes with your mac -> 
  curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
  
# Install Python 3.7 -> 
  https://www.python.org/downloads/mac-osx/
  
# Clone repo -> 
  git clone https://github.com/CrunchyJohnHaven/algosPython/
  
# Create an alias in .bash_profile to run python 3.7 -> 
  alias python="python3"
 
# Create an alias in .bash_profile to create a python environment -> 
  alias pyenv="source /Users/johnbradley/env/bin/activate"

# Install python virtual env
python3 -m pip install --user virtualenv
(pyenv or -> )source /Users/johnbradley/env/bin/activate

# Install distribute -> 
curl -O http://python-distribute.org/distribute_setup.py

# Dependencies (pip freeze lists all installed packages)
  pip install nose
  
# Run pycourse.py file with automatic reloading using nodemon -> 
  nodemon --exec "python3" pycourse.py
  
