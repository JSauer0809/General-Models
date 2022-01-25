sectionWidth = 0.171 #width of segment (mm)
sectionLength = 0.190 #length of segment (mm)
sectionHeight = 0.050 #height of segment (mm)
flowRateLPM = 0.5 #liter per min headspace flow
flowRateLPs = flowRateLPM/60 #liters per second headspace flow
flowRatems = flowRateLPs/1000 #cubic meters per second headspace flow
time = 0
emissionRate = 0.1 #micrograms /s
chamber1mass = 0
c1conc = 0
chamber2mass = 0
c2conc = 0
chamber3mass = 0
c3conc = 0
chamber4mass = 0
c4conc = 0
chamber5mass = 0
c5conc = 0

while time < 20000:
    if time == 120:
        emissionRate = 0
    chamber1mass = chamber1mass + emissionRate -  (flowRatems*c1conc)
    c1conc = chamber1mass/(sectionWidth*sectionLength*sectionHeight)
                                  
    chamber2mass = chamber2mass + (flowRatems*c1conc) - (flowRatems*c2conc)
    c2conc = chamber2mass/(sectionWidth*sectionLength*sectionHeight)
                                  
    chamber3mass = chamber3mass + (flowRatems*c2conc) - (flowRatems*c3conc)
    c3conc = chamber3mass/(sectionWidth*sectionLength*sectionHeight)
                                  
    chamber4mass = chamber4mass + (flowRatems*c3conc) - (flowRatems*c4conc)
    c4conc = chamber4mass/(sectionWidth*sectionLength*sectionHeight)
                                  
    chamber5mass = chamber5mass + (flowRatems*c4conc) - (flowRatems*c5conc)
    c5conc = chamber5mass/(sectionWidth*sectionLength*sectionHeight)
    time = time+1
                                  
    #print(headspaceMass,time)
    f = open("WBA_ChamberedBox_0_5LPM_EmissionStop2", "a")
    f.write(str(chamber1mass))
    f.write(",")
    f.write(str(chamber2mass))
    f.write(",")
    f.write(str(chamber3mass))
    f.write(",")
    f.write(str(chamber4mass))
    f.write(",")
    f.write(str(chamber5mass))
    f.write(",")
    f.write(str(time))
    f.write("\n")
    f.close()
   
