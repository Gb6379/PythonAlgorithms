import krpc
import time
import os

connection = krpc.connect()

vessel = connection.space_center.active_vessel

countdown = ["3", "2", "1", "Lift Off!"]

for i in range(len(countdown)):
    print(countdown[i])
    time.sleep(1)

print("Engine on")
vessel.control.trhottle = 1
vessel.control.sas = True
vessel.control.activate_next_stage()
apoapsis = vessel.orbit.apoapsis

ascentPhase = True
cruisePhase = False
insertionPhase = False

while ascentPhase or cruisePhase or insertionPhase:
    altitude = vessel.flight().mean_altitude
    heading = vessel.flight().heading
    apoapsis += apoapsis +1
    
    if ascentPhase:
       targetPitch = 90 * ((50000 - altitude)/50000)
       pitchDiff = vessel.flight().pitch - targetPitch
       print(targetPitch)
       if heading < 180:
           vessel.control.yaw = (pitchDiff / 90)
       else:
           vessel.control.yaw = 0.5

       if vessel.thrust == 0.0: # it's gonna run this if till all the engines run out of fuel
           vessel.control.activate_next_stage()
           time.sleep(1)
           vessel.control.throttle = 1
        
       if vessel.orbit.apoapsis > 690000: #apoapsis starts on 900000
           vessel.control.throttle = 0
           time.sleep(1)
           vessel.control.activate_next_stage()
           #vessel.control.sas = True
           time.sleep(0.1)
           #vessel.control.sas_mode = connection.space_center.SASMode.prograde


           ascentPhase = False
           cruisePhase = True
           
    elif cruisePhase:
        if altitude > 80000:
            cruisePhase: False
            insertionPhase: True
            #vessel.control.sas = False
            vessel.control.throttle = 1
    elif insertionPhase:
        targetPitch = 0
        pitchDiference = vessel.flight().pitch - targetPitch

         #Heading Control on the insertionPhase
        if heading < 180:
            #print("Heading to get in orbit")                
            vessel.control.yaw = (pitchDiference / 90) #pitch(distance of the horizon) cotrol in this context, getting right to the point, it means that the space craft will turn gently to the horizon
            if vessel.flight().pitch < 1 and vessel.flight().pitch > -1:
                #vessel.control.sas = True
                
            #else:
                #vessel.control.sas = False
        else:
            vessel.control.yaw = 0.5

        if vessel.orbit.periapsis > 690000: #priapsis is the distance of an object of the center of the planet
            vessel.control.throttle = 0
            insertionPhase = False

         #Staging    
        if vessel.thrust == 0.0:
            vessel.control.activate_next_stage()



        
   
