import random 
def shayq():
	mat=random.randint(1,100)
	key=False
	
	rise=1
	
	
	
	while not key:
		dd=int(input("Enter ,num ber : "))
		rise+=1
		
		
		if mat==dd:
			key=True
			print("you want ")
				
		else:
			if dd>mat:
				print("dd is uppee")
				
			else:
				print("dd is lwer")
	print(f"{rise}")
		
shayq()