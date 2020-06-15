import krpc

connection = krpc.connect() #connection to the game

vessel = connection.space_center.active_vessel #connect to the vessel inside the space station

vessel.control.throttle = 1 #connect the controls within the vessel (rocket)
vessel.control.sas = True #sas is the control panel
vessel.control.activate_next_stage()

landing = False

while True:
    altitude = vessel.flight().mean_altitude
    
    
    if landing == False:
        if altitude > 1000 and altitude < 1500:
            print("left")
            vessel.control.yaw = 1 # 1 = full to the left
        elif altitude > 1500 and altitude < 2000:
            vessel.control.yaw = 0.5
            print("left")
        else:
            vessel.control.yaw = 0

        if altitude > 5000:
            print("turn off engine")
            vessel.control.throttle = 0 #turn off the engine

        if altitude > 5200:# detach from engine
            print("detaching")
            vessel.control.activate_next_stage()
            landing = True
        if landing == True and altitude < 2000:
            print("parachute")
            vessel.control.activate_next_stage()
