import os
import subprocess  

####################
#
# Functions
#
####################
        
####################
#
# Main
#
####################

print("Uninstalling project")
        
subprocess.call("adb uninstall tv.nopper.VKTS_Example06", shell=True)  
