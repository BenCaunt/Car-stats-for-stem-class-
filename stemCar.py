#change to your car
time = int(input("time in seconds: "))   # seconds 3.586
distance = int(input("distance in meters: "))   #meters 5.81
mass = 0.0198 #kg

#equation
velocity = distance/time
mph = (velocity*2.23)
acceleration = velocity/time
p = mass*velocity

#output
print("velocity")
print(velocity)
print("speed in mph")
print(mph)
print("acceleration")
print(acceleration)
print("momentum")
print(p)
