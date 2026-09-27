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
# when we write this so we are able to create a virtual env but without activation when wehen we write pip install pandas then again it will install pandas global not virtual because we create virtual env but we not write the code for activation 
# so we write a code 
# myenv\scripts\activate.bat

# now  when we write  pip install pandas then it will install virtual then we do one test 
# firstly when we write pandas(--version--) without activate virtual then they will give some version but when we activate our virtual and then asked same question then they woill give diferent version ok
# 
# now for deactivate or for leaving that virtual we write python -venv % deactivate 
# 
# when we used pip freeze then it will give the whatver we install  the package in that virtual env that means it will give all list of packages 
# when we write pip freeze > requirements.txt then pip freeze ka matlab to pura list hai to hoga aise ki ki puri list ek requirements.txt karke ek file banegi or usmein pyure list  ajjayegnge 
# or agar hame requirements mein jitne likhe hai matlab pandas ,xml,fir or bhi library agar install na ho to ham ek sath jo jo likha hpga sab ko install kar sakte hai 
#  uske liye hame pip install -r requirements.txt likhna hoga 
#  