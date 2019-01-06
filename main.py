from os import listdir, getcwd, environ
from os.path import isfile, join
import PIL
from PIL import Image
import git

print('')
print("started")
print('')
# Get path to Folders
getcwd = getcwd()+"/cryptologo"
masterPath = getcwd+"/master"
smallerPath = getcwd+"/smaller"
smallPath = getcwd+"/small"
largePath = getcwd+"/large"
print('')
print(getcwd, " : Directery")
print('')
environ['GIT_ASKPASS'] = getcwd
environ['GIT_USERNAME'] = "Mrmetech-s-Bot"
environ['GIT_PASSWORD'] = "4a5e0a3bee39fb5eec93c3860a0650da7866351a"
#g = git.cmd.Git(getcwd)

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

print('')
print("made it to formating")
print('')
for smallerPhotosToFormat in missingSmaller:
    try:
        img = Image.open(masterPath+"/"+smallerPhotosToFormat)
        hpercent = (smallerSize / float(img.size[1]))
        wsize = int((float(img.size[0]) * float(hpercent)))
        img = img.resize((wsize, smallerSize), PIL.Image.ANTIALIAS)
        img.save(smallerPath+"/"+smallerPhotosToFormat, "PNG")
        print('')
        print("formating smaller ", smallerPhotosToFormat)
        print('')
    except IOError:
        print("cannot create thumbnail for '%s'" % smallerPhotosToFormat)

for smallPhotosToFormat in missingSmall:
    try:
        img = Image.open(masterPath+"/"+smallPhotosToFormat)
        hpercent = (smallerSize / float(img.size[1]))
        wsize = int((float(img.size[0]) * float(hpercent)))
        img = img.resize((wsize, smallerSize), PIL.Image.ANTIALIAS)
        img.save(smallerPath+"/"+smallPhotosToFormat, "PNG")
        print('')
        print("formating small ", smallPhotosToFormat)
        print('')
    except IOError:
        print("cannot create thumbnail for '%s'" % smallPhotosToFormat)

for largePhotosToFormat in missingLarge:
    try:
        img = Image.open(masterPath+"/"+largePhotosToFormat)
        hpercent = (smallerSize / float(img.size[1]))
        wsize = int((float(img.size[0]) * float(hpercent)))
        img = img.resize((wsize, smallerSize), PIL.Image.ANTIALIAS)
        img.save(smallerPath+"/"+largePhotosToFormat, "PNG")
        print('')
        print("formating large ", largePhotosToFormat)
        print('')
    except IOError:
        print("cannot create thumbnail for '%s'" % largePhotosToFormat)


print("done formatting")
try:
    repo.git.commit('-a', '-m', "Committed new logos or updates")
except Exception:
    print('')
    print('Already up to date no commit must be made')
    print('')
try:
    repo.git.push()
except Exception:
    print('')
    print('Already up to date no push must be made')
    print('')
print("FINISHED")
