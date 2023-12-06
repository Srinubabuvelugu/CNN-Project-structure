echo [$(date)]:"START"
echo [$(date)]: "creating env with python 3.8 version"
conda create --prefix ./CNN_project_structure_env python=3.8 -y
echo [S(date)]: "activating the environment"
source activate ./CNN_project_structure_env
echo [%(date)]: "instaling the dev requirements"
pip install -r requirements_dev.txt
echo [$(date)]:"END"