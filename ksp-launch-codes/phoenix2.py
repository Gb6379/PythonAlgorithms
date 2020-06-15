import time
import krpc

#orbital launch code
connection = krpc.connect() #connect to the game

vessel = connection.space_center.active_vessel # connect to the vessel (rocket)

countdown = ["ten", "nine" , "eight", "seven", "six", "five", "four", "three", "two", "one" , "Lift Off!"]

for i in range(len(countdown)):
    print(countdown[i])
    time.sleep(1)

vessel.control.throttle = 1 
print("Engine on")
vessel.control.activate_next_stage() #initiate the next stage

# 3 boolean variables for 3 diferentes flight phases
ascentPhase = True
cruisePhase = False
insertionPhase = False
apoapsis = vessel.orbit.apoapsis 

while ascentPhase or cruisePhase or insertionPhase:
    altitude = vessel.flight().mean_altitude #tell me how far we are
    heading = vessel.flight().heading #tell me which way am i ponting to
    apoapsis += apoapsis + 1
    
    if ascentPhase:               
        targetPitch = 90 * ((50000 - altitude)/50000) # the % of how far we are to guide trhough the pitch(distance of the horizon) and the turn
        pitchDiference = vessel.flight().pitch - targetPitch #how much we've pitched down, how much we are pitching above the horizon

        #Heading Control
        if heading < 180:               
            vessel.control.yaw = (pitchDiference / 90) #pitch(distance of the horizon) cotrol in this context, getting right to the point, it means that the space craft will turn gently to the horizon
        else:                       
            vessel.control.yaw = 0.5
            
        #Staging    
        if vessel.thrust == 0.0:
            print("staging")
            print("altitude %.2f" %altitude)
            vessel.control.activate_next_stage()
            
        #Main Engine Cut Off      
        if vessel.orbit.apoapsis > 690000: #when the spaceship gets to the orbit (69000 is the treshold bettwen atmosferes)
            print("%.2f" %apoapsis)
            vessel.control.throttle = 0
            print("Main Engine turned off")
            time.sleep(1)
            vessel.control.activate_next_stage()
            print("Main Engine Cutted off")
            vessel.control.sas = True #limits my control over the rocket if its on          
            #print("sas activated")            
            time.sleep(0.1)
            #vessel.control.sas_mode = connection.space_center.SASMode.prograde

            ascentPhase = False
            cruisePhase = True
            
    elif cruisePhase:       
        #print("cruise phase initiated")
        if altitude > 80000: #this value varies depending on the vessel launch, weigth and stuff
            print("insertion Phase")
            print("Secondary Engine on")
            cruisePhase = False
            insertionPhase = True
            vessel.control.sas = False
            vessel.control.throttle = 1          
            #print("secondary engine on")          
    elif insertionPhase:     
        #print("insetion phase initiated")          
        targetPitch = 0
        pitchDiference = vessel.flight().pitch - targetPitch

         #Heading Control on the insertionPhase
        if heading < 180:
            #print("Heading to get in orbit")                
            vessel.control.yaw = (pitchDiference / 90) #pitch(distance of the horizon) cotrol in this context, getting right to the point, it means that the space craft will turn gently to the horizon
            if vessel.flight().pitch < 1 and vessel.flight().pitch > -1:
                vessel.control.sas = True
            else:
                vessel.control.sas = False
        else:
            vessel.control.yaw = 0.5

        if vessel.orbit.periapsis > 690000: #priapsis is the distance of an object of the center of the planet
            vessel.control.throttle = 0
            insertionPhase = False

         #Staging    
        if vessel.thrust == 0.0:
            vessel.control.activate_next_stage()
            




        
