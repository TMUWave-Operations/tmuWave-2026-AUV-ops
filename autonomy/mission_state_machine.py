class StateMachine:

    """
    Objective: 
    - create basic AUV mission state transitions

    Args:
    - vision data
    - telemetry data
    - mission parameters

    Returns:
    - update the mission state
    
    Notes:
    - expand a bit about cose here 
    """
    # define the states of the AUV mission
    def Initial(self):
        self.state = "Initial" # this is the initial state of the AUV, where it is ready to start the mission. The AUV will transition to the "dive" state when it receives the command to start the mission.
    def next_state(self):
        if self.state == "Initial":
            self.state = "dive"
        elif self.state == "dive":
            self.state = "surface"
        return self.state
    
auv = StateMachine()
auv.Initial()

print(auv.next_state()) #print state
print(auv.next_state()) #print next state
