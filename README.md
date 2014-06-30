pi-monitor
==========

scripts used in the pi monitor

This project I started is for a specific need, which is to monitor activity around my vehicle, especially at night, but given its portable design and, hopefully small package, it could be used anywhere remote monitoring is needed. Partial schematic shown 
The features: 
IR motion detector 
IR camera with fisheye lens 
Software triggered IR flashlight 
Uploads imagery to home server when in range of home wifi 
Deletes old imagery when preset file space limits are reached, when home wifi is not available for upload 
Time stamp overlay on each frame 
Battery Powered 

My current test setup has a 12 volt IR led array, but it doesn't have very good range and it requires 12 volts, so its going away in favor of the high intensity IR led. It runs on 3.7 volts and it illuminates nearly as far as the pir sensor can detect . I only need a few feet and I will have that range now.

I will have the battery, charger and converter in a few days. Updated schematic to follow after trials. 

Most of the scripting i did was shell. The python I used was for accessing the gpio.
