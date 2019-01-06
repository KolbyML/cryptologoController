from os import listdir, getcwd, remove
from os.path import isfile, join
import PIL
import git
from PIL import Image

print('')
print("started")
print('')
# Get path to Folders
getcwd = getcwd() + "/cryptologo"
masterPath = getcwd + "/master"
smallerPath = getcwd + "/smaller"
smallPath = getcwd + "/small"
largePath = getcwd + "/large"
print('')
print(getcwd, " : Directery")
print('')

# g = git.cmd.Git(getcwd)

repo = git.Repo(getcwd)
repo.git.stash()
repo.git.pull()

print('')
print("stashed and pulled repos")
print('')

# Get list of photos in the folder
masterList = [f for f in listdir(masterPath) if isfile(join(masterPath, f))]
smallerList = [f for f in listdir(smallerPath) if isfile(join(smallerPath, f))]
smallList = [f for f in listdir(smallPath) if isfile(join(smallPath, f))]
largeList = [f for f in listdir(largePath) if isfile(join(largePath, f))]

# Base Height Size
smallerSize = 25
smallSize = 50
largeSize = 250

# Find what logos are missing in the folder
missingSmaller = set(masterList).difference(smallerList)
missingSmall = set(masterList).difference(smallList)
missingLarge = set(masterList).difference(largeList)

# Find what logos are logos to delete
toDeleteSmaller = set(smallerList).difference(masterList)
toDeleteSmall = set(smallList).difference(masterList)
toDeleteLarge = set(largeList).difference(masterList)

print('')
print("made it to formating")
print('')
for smallerPhotosToFormat in missingSmaller:
    try:
        img = Image.open(masterPath + "/" + smallerPhotosToFormat)
        hpercent = (smallerSize / float(img.size[1]))
        wsize = int((float(img.size[0]) * float(hpercent)))
        img = img.resize((wsize, smallerSize), PIL.Image.ANTIALIAS)
        img.save(smallerPath + "/" + smallerPhotosToFormat, "PNG")
        print('')
        print("formating smaller ", smallerPhotosToFormat)
        print('')
    except IOError:
        print("cannot create thumbnail for '%s'" % smallerPhotosToFormat)

for smallPhotosToFormat in missingSmall:
    try:
        imgS = Image.open(masterPath + "/" + smallPhotosToFormat)
        hpercent = (smallSize / float(imgS.size[1]))
        wsize = int((float(imgS.size[0]) * float(hpercent)))
        imgS = imgS.resize((wsize, smallSize), PIL.Image.ANTIALIAS)
        imgS.save(smallPath + "/" + smallPhotosToFormat, "PNG")
        print('')
        print("formating small ", smallPhotosToFormat)
        print('')
    except IOError:
        print("cannot create thumbnail for '%s'" % smallPhotosToFormat)

for largePhotosToFormat in missingLarge:
    try:
        imgL = Image.open(masterPath + "/" + largePhotosToFormat)
        hpercent = (largeSize / float(imgL.size[1]))
        wsize = int((float(imgL.size[0]) * float(hpercent)))
        imgL = imgL.resize((wsize, largeSize), PIL.Image.ANTIALIAS)
        imgL.save(largePath + "/" + largePhotosToFormat, "PNG")
        print('')
        print("formating large ", largePhotosToFormat)
        print('')
    except IOError:
        print("cannot create thumbnail for '%s'" % largePhotosToFormat)

print("done formatting")
try:
    repo.git.add('-A')
    repo.git.commit('-m Committed new logos or updates')
except Exception:
    print('')
    print('Already up to date no commit must be made')
    print('')
print('')
print("made it to removing old logos")
print('')
for smallerToDelete in toDeleteSmaller:
    try:
        remove(smallerPath + "/" + smallerToDelete, "PNG")
        print('')
        print("deleted smaller ", smallerToDelete)
        print('')
    except Exception:
        print("cannot find logo for '%s'" % smallerToDelete)

for smallerToDelete in toDeleteSmaller:
    try:
        remove(smallerPath + "/" + smallerToDelete, "PNG")
        print('')
        print("deleted smaller ", smallerToDelete)
        print('')
    except Exception:
        print("cannot find logo for '%s'" % smallerToDelete)

for smallToDelete in toDeleteSmall:
    try:
        remove(smallPath + "/" + smallToDelete, "PNG")
        print('')
        print("deleted smaller ", smallToDelete)
        print('')
    except Exception:
        print("cannot find logo for '%s'" % smallToDelete)

for largeToDelete in toDeleteLarge:
    try:
        remove(largePath + "/" + largeToDelete, "PNG")
        print('')
        print("deleted smaller ", largeToDelete)
        print('')
    except Exception:
        print("cannot find logo for '%s'" % largeToDelete)

try:
    repo.git.add('-A')
    repo.git.commit('-m Committed deleted old logos')
except Exception:
    print('')
    print('Already up to date no commit must be made 2')
    print('')
try:
    repo.git.push()

except Exception:
    print('')
    print('Already up to date no push must be made')
    print('')
print("FINISHED")
