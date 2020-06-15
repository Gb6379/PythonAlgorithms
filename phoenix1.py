import krpc
import time

countdonw = ["3", "2", "1", "lift off"]

connection = krpc.connect() #connection to the game

vessel = connection.space_center.active_vessel #connect to the vessel inside the space station

for i in range(len(countdonw):
    print(countdown[i])
    time.sleep(1)

vessel.control.throttle = 1 #connect the controls within the vessel (rocket)
vessel.control.sas = True #sas is the control panel
vessel.control.activate_next_stage()

landing = False
flying = True

while flying:
    altitude = vessel.flight().mean_altitude
   
    
    if landing == False:
        #if altitude > 1000 and altitude < 1500:
            #print("left")
            #vessel.control.yaw = 1 # 1 = full to the left
        #elif altitude > 1500 and altitude < 2000:
            #vessel.control.yaw = 0.5
            #print("left")
        #else:
        vessel.control.yaw = 0

        if vessel.thrust == 0.0: # it's gonna run this if till all the engines run out of fuel
            vessel.control.activate_next_stage()
            time.sleep(1)
            vessel.control.throttle = 1             

        if altitude > 40000: # detach from engine
            print("detaching")
            vessel.control.sas = False
            landing = True
            
    else:        
        if altitude < 2000:          
            vessel.control.activate_next_stage()
