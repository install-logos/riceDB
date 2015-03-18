#!/bin/env python
from rice import search, new_rice, swap
import argparse
import json

# Main Script for running riceDB
# To install a new rice, rice.py will:
# Search for the specified rice/software using the search lib
# Process the results of the search call, organizing by a criteri
# such as popularity
# Call the rendering library which will take the sorted list and
# display the options to the user, as well as a way for the user
# to select a rice of their choosing
# Render.py should take a json and a string as arguments,
# and will render the json in a predetermined format and display
# the string at the bottom. It will also return the users input
# to the rice method, which will be the rice the user wants
# Rice.py will then call the download library which will fetch
# the github repo specified in the selected rice, unpack it
# into a new folder within the .[program-name]-rice folder,
# assuming that it doesn't already exist
# Rice.py will call the inspection library - this will look for
# existing configuration files for the software present in the system
# and their origin
# If the currently installed rice is from riceDB, it will run the
# Switchout.py script and move the files into the folder in the
# .[program-name]-rice folder in the users home directory
# Note: Read the wiki on config switching for more details about this
# In the event that the current config is not from riceDB, Switchout.py
# will ask the user for the name of their current configuration
# Switchout.py then creates a folder in the .[program-name]-rice folder
# that has the user specified name(assuming that the folder is valid
# and doesn't already exist). All default config files will be moved
# into this folder and the user will be asked for nondefault configuration
# files which may be part of the current rice. The user will specify
# the full path of these files and their name and this will be used to
# generate a sysinfo.json and move the respective files into the created
# folder.
# Rice.py then will call the setup library which will take arguments
# of a sysinfo.json, and a dictionary(of file names/locations) extracted from json.index.
# These will contain entries in the format:
# configname:location and Setup.py will move all config names specified in these two
# inputs to their respective locations
# Setup.py will finally modify the 'active' file in the .[programname]-rice
# directory to point to the correct folder
# Rice.py will now be completed and exit

# SUMMARY OF PROCESS:
# Rice.py calls Search.py which returns a JSON
# Rice.py processes this JSON and calls Render.py
# Rice.py calls Download.py to download selected rice
# Rice.py calls Switchout.py to move out the current configs
# Rice.py calls Setup.py to move files into correct locations
# Rice.py exits

parser = argparse.ArgumentParser(
    description="""
    RiceDB is an universal configuration file manager designed to make
    it easy to obtain configurations for any application that fit your
    individual needs.
    """
)

parser.add_argument(
    '-s', '--swap', nargs=2, type=str,
        help="""
        This swaps out the current rice for [program] with the specified rice.
        USAGE: rice.py --swap or -s [program] [rice]
        """
)

parser.add_argument(
    'rice', nargs='*', type=str,
    help="""
    Optionnal positionnal argument, used to look for packages with specified
    keywords for a specified program.

    USAGE: rice <program_name> [keyword1, keyword2, ...]]
    """
)

parser.add_argument(
    '-S', '--sync', nargs=2, type=str,
    help="""
    Unlike the default positionnal argument this one won't search for a
    a package using your keywords, you have to specify directly the name
    of the package.

    USAGE: rice -S <program_name> <package_name>
    """
)

args = parser.parse_args()
if args.sync:
    # -S option used,
    search_return = search.search_packages(args.sync[0],
                                           args.sync[1],
                                           search.get_package)
    new_rice.install(search_return)
elif args.swap:
    # -s option used,
    swap.swap(args.swap[0], args.swap[1])
elif len(args.rice) > 1:
    # Program name + keyword specified
    search_return = search.search_packages(args.rice[0],
                                           args.rice[1:],
                                           search.search_keywords)
    new_rice.install(search_return)
elif len(args.rice) == 1:
    # Only the program name is mentionned
    # Trying to get the package list of the specified program name
    search_return = search.get_software(args.rice[0])
    new_rice.install(search_return)
else:
    print("You must run rice.py with inputs. Try rice.py -h if you're unsure how to use the program")
    exit()
