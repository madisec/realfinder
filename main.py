import os 
import requests
import argparse
import pyfiglet

#  Make Filet tool
def tool_figlet():
    figlet = pyfiglet.figlet_format("Huntcon")
    print(figlet)

# make tool argument
parser = argparse.ArgumentParser(usage="realfinder", description="Real IP discovery tool")
parser.add_argument("-d", "--domain", dest="domain", default=None, help="Get doamin for finding real IP")
parser.add_argument("-c", "--cidr", dest="cidr", default="", help="Add CIDR to flow")
parser.add_argument("-o", "--output", dest="output", default="output.txt", help="Saving result to file")
parser.add_argument("-V", "--version", dest="version", action="store_true", default=False, help="version")
args = parser.parse_args()
domain = args.domain
cidr = args.cidr
output = args.output
version = args.version
