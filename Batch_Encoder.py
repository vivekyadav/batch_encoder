"""
A script to Batch-encode Video files using HandbrakeCLI.
Takes a folder path as it's argument and encodes all the video files in it.
NOTE : HandbrakeCLI is required to be in the same folder as this script.
       http://handbrake.fr
       Change the "setting" variable to modify encoding details.
"""


import os
import sys

def main():
    if len(sys.argv) < 2:
        print "\nUsage : "+sys.argv[0]+" [folder name]"
        exit(0)
    files = os.listdir(sys.argv[1])
    dir = sys.argv[1] + "\\"
    setting = "-t 1 -c 1 -f mkv --strict-anamorphic  -e x264 -S 190 -2  -a 1 -E faac -6 dpl2 -R Auto -B 48 -D 0.0 -x ref=2:bframes=2:subq=6:mixed-refs=0:weightb=0:8x8dct=0:trellis=0 --verbose=1"
    print files
    for i in range(0,len(files)):
        print "\nEncoding "+files[i]
        inname = "\""+dir+files[i]+"\""
        outname = ".".join(files[i].split(".")[:-1]) + "-1." + files[i].split(".")[-1]
        outname = "\""+dir+outname+"\""
        print "\nOutput file : "+outname
        os.system("HandBrakeCLI.exe -i "+inname+" -o "+ outname + setting)

main()