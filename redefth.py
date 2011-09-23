# -*- coding: utf-8 -*-

# redefth.py v0.2
# Date: 23.09.2011r
# Author: Piotr Tynecki <piotr@tynecki.pl>

import sys
import os
import shutil

# Sets mml directory path
mmlPath = "/usr/local/share/mizar/mml"

# Sets everylab program path
everylabPath = "./everylab"

# Sets text directory path
textPath = "/home/katharsis/UwB/Mizar/text"

def sortBySize(mmllist):
    """Sorts the files from mml directory according to their size and returns a new list of files"""
    sortedMML = []

    for x in mmllist:
        size = os.path.getsize("%s/%s" % (mmlPath, x))
        sortedMML.append((size, x))

    sortedMML.sort()

    return sortedMML

def redefineTh(mmlFile):
    """Sets unique (label) number for all theorems in *.miz file"""
    elfPath = mmlFile.replace(".miz", ".$-$")

    shutil.copyfile("%s/%s" % (mmlPath, mmlFile), "%s/%s" % (textPath, mmlFile))

    os.system("accom text/%s" % mmlFile)
    os.system("%s text/%s" % (everylabPath, mmlFile))
    os.system("edtfile text/%s" % mmlFile)
    os.rename("%s/%s" % (textPath, elfPath), "%s/%s" % (textPath, mmlFile))
    os.system("renthlab text/%s" % mmlFile)
    os.system("edtfile text/%s" % mmlFile)
    os.rename("%s/%s" % (textPath, elfPath), "%s/%s" % (textPath, mmlFile))

def cleanup():
    """Deletes all files from text directory without *.miz files"""
    currentDirectory = os.listdir(textPath)

    tempfiles = [x for x in currentDirectory if x.split(".")[1] == "miz"]

    for x in tempfiles:
        currentDirectory.remove(x)

    for x in currentDirectory:
        os.remove("%s/%s" % (textPath, x))

    os.system("clear")

if __name__=="__main__":
    os.system("clear")

    try:
        value = sys.argv[1]

        mml = os.listdir(mmlPath)

        # If text directory doesn't exists then it's created
        if not os.path.exists("text"):
            os.mkdir("text")

        # For all *.miz files from mml database
        if value == "-a":
            for x in sortBySize(mml):
                redefineTh(x[1])
                cleanup()

        # For a single *.miz file
        elif value == "-f":
            path = "%s.miz" % sys.argv[2]
            redefineTh(path)
            cleanup()

        # For a number of *.miz files
        elif int(value) > 0:
            for x in sortBySize(mml)[:int(value)]:
                redefineTh(x[1])
                cleanup()

        else:
            raise ValueError

    except (IndexError, ValueError):
        print "redefth v0.2\nCopyright (C) 2011 by Piotr Tynecki <piotr@tynecki.pl>\n\nExamples:\n\tpython redefth.py 10\n\tpython redefth.py -a\n\tpython redefth.py -f filename"

    except IOError:
        print "redefth v0.2\nCopyright (C) 2011 by Piotr Tynecki <piotr@tynecki.pl>\n\nError:\n\tFile %s is corrupted or doesn't exist" % path
