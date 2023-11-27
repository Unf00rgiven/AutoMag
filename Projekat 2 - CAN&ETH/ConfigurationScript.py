import win32com.client
import os
import msvcrt

# Path to the configuration file
cfg_path = r"C:\Users\nituser\Desktop\AUTOMAG - StojisavljevicPejkovic\P1\Project1.cfg"

def open_canoe_project(cfg_path):
    try:
        # Create a new instance of the CANoe COM application
        canoeApp = win32com.client.DispatchEx("CANoe.Application")

        # Open the configuration file
        canoeApp.Open(cfg_path)
        print("Successfully opened {}".format(cfg_path))

        # Access the measurement setup
        measurement = canoeApp.Measurement

        # Add test node
        canoeApp.Configuration.SimulationSetup.Nodes.Add("TestNode")
	print("Test node added")
	
	# Add test module
	#canoeApp.Configuration.SimulationSetup.Node.AddtestModule("TestModule")
	#print("Test module added")

        # Start the simulation
        measurement.Start()
	print("Measurement started")

	# Start the simulation
        print("Simulation started")	
	print("Press 'Q' to stop the measurement...")
        while True:
            if msvcrt.kbhit():  # Check if a key has been pressed
                key = msvcrt.getch()  # Get the pressed key
                if key in [b'Q', b'q']:  # Check if the key is 'Q' or 'q'
                    measurement.Stop()  # Stop the measurement
                    break  # Exit the loop
	print("Measurement stoped")


    except Exception as e:
        print("An error occurred: {}".format(e))

if __name__ == "__main__":
    # Call the function to open the Canoe project
    open_canoe_project(cfg_path)
