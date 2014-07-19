#!/bin/bash

homedir='/opt/pi-monitor/'
imgdir='/opt/img-dir/'

cd $imgdir
python -m SimpleHTTPServer 8001 & > /dev/null 2>&1
