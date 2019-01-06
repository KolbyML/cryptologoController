from os import listdir, getcwd, environ
from os.path import isfile, join
import PIL
from PIL import Image
import git


# Get path to Folders
getcwd = getcwd()+"/cryptologo"
masterPath = getcwd+"/master"
smallerPath = getcwd+"/smaller"
smallPath = getcwd+"/small"
largePath = getcwd+"/large"

environ['GIT_ASKPASS'] = getcwd
environ['GIT_USERNAME'] = "Mrmetech-s-Bot"
environ['GIT_PASSWORD'] = "4a5e0a3bee39fb5eec93c3860a0650da7866351a"
#g = git.cmd.Git(getcwd)

repo = git.Repo(getcwd)
repo.git.stash()
repo.git.pull()


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

for smallerPhotosToFormat in missingSmaller:
    try:
        img = Image.open(masterPath+"/"+smallerPhotosToFormat)
        hpercent = (smallerSize / float(img.size[1]))
        wsize = int((float(img.size[0]) * float(hpercent)))
        img = img.resize((wsize, smallerSize), PIL.Image.ANTIALIAS)
        img.save(smallerPath+"/"+smallerPhotosToFormat, "PNG")
    except IOError:
        print("cannot create thumbnail for '%s'" % smallerPhotosToFormat)

for smallPhotosToFormat in missingSmall:
    try:
        img = Image.open(masterPath+"/"+smallPhotosToFormat)
        hpercent = (smallerSize / float(img.size[1]))
        wsize = int((float(img.size[0]) * float(hpercent)))
        img = img.resize((wsize, smallerSize), PIL.Image.ANTIALIAS)
        img.save(smallerPath+"/"+smallPhotosToFormat, "PNG")
    except IOError:
        print("cannot create thumbnail for '%s'" % smallPhotosToFormat)

for largePhotosToFormat in missingLarge:
    try:
        img = Image.open(masterPath+"/"+largePhotosToFormat)
        hpercent = (smallerSize / float(img.size[1]))
        wsize = int((float(img.size[0]) * float(hpercent)))
        img = img.resize((wsize, smallerSize), PIL.Image.ANTIALIAS)
        img.save(smallerPath+"/"+largePhotosToFormat, "PNG")
    except IOError:
        print("cannot create thumbnail for '%s'" % largePhotosToFormat)

repo.git.commit('-a', '-m', "Committed new logos or updates")
repo.git.push()
