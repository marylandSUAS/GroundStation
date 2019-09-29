#!/usr/bin/env python

import os


Images_images = [f for f in os.listdir('/Images') if os.path.isfile(f)]
    
Images_sent = [f for f in os.listdir('/Sent') if os.path.isfile(f)]
    

for f in Images_images:
	os.rename(f, "Old/"+f.split('/')[-1])

for f in Images_sent:
	os.rename(f, "Old/"+f.split('/')[-1])
