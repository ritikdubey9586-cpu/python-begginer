# what is virtual environment ?
# a virtual environment is a tool is used to isolate python environment on a single machine allowing you to work on multiple project with different depandencies and packages without conflict .
# specially this env is used when there is conflict between two dependencies or two package means if we work on single dependencies and in that dependencies we write two program but both program cant satisfy there need in one dependencies 
# so from this reason we make virtual environment basically this dependencies is used create a multiple package .

# to create a virtual environment in python 

# python -m venv myenv

# this is used to create environment then we should do activate for use and for unused we used deactivate so for this we write code 

# for activation in linus and macos 
# source myenv/bin/activate

# for activation in windows we used 
# myenv\scripts\activate.bat

# in terminal we do practice firstly when we write pip install pandas so pandas will be install in global environment means normal 
# se we used python -m venv myenv 
# when we write this so we are able to create a virtual env but without activation when wehen we write pip install pandas then 