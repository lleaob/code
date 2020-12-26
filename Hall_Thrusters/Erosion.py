#This code is an implementation of an algorithm to "draw" the resulting erosion of Hall thrusters. 
#1st - It imports heavyIonsDensity or BNAtomsDensity from VSIM [g/m^3]
#2nd - extrapolates the curve to 1000h of operation
#3rd - it transforms the input density into particles density (accounts for simulation's superparticles (10^5 particles) design)
#4th - calculates part/m3
#5th - accounts for Taccogna numeric density used by VSIM (dn' = dn/50)
#6th - draws erosion inside of the propulsion chamber

