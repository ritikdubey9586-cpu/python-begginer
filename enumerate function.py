ritik = [1,2,3,4,5,6,7,8]

index =0 

for marks in ritik :
    print(marks)
    if(index ==3):
     print( "hello my dear friends ")
    index +=1

# above code is used without any enumarate function now we used it so that will be easy 

ritik = [1,2,3,4,5,6,7,8]
 
for index,marks in enumerate(ritik) :
    print(marks)
    if(index ==3):
     print( "hello my dear friends ")
    