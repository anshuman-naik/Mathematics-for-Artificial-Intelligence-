import matplotlib.pyplot as plt

#We take in input for the user for the 1st and 2nd vector


vector_one_x = float(input("Please enter x value of vector 1 : "))

vector_one_y = float(input("Please enter y value of vector 1 : "))

vector_two_x = float(input("Please enter x value of vector 2 : "))

vector_two_y = float(input("Please enter y value of vector 2 : "))

print("Please enter float values")

#We calculate the resultant vector

r_vect_x = vector_one_x + vector_two_x
r_vect_y = vector_one_y + vector_two_y


#printing the result 


print(f'''Your vectors
      vector 1 = ({vector_one_x},{vector_one_y})
      vector 2 = ({vector_two_x},{vector_two_y})''')
print(f"The resultant vector would be coordinated as ({r_vect_x},{r_vect_y})")

#representing the vectors on a graph
plt.figure()
plt.plot([0,vector_one_x],[0, vector_one_y], color='blue', marker='>', linewidth=2, label="Vector 1")
plt.plot([0,vector_two_x],[0,vector_two_y], color='green', marker='>', linewidth=2, label= "Vector 2")
plt.plot([0,r_vect_x],[0, r_vect_y], color='red', linestyle='--', marker='>', linewidth=2,label="Resultant Vector")
plt.xlim(left=0)
plt.ylim(bottom=0)
plt.title("Your Resultant Vector")
plt.xlabel("X - Axis")
plt.ylabel("Y - Axis")
plt.legend()
plt.grid(True)
plt.show()
