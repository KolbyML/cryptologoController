from os import listdir, getcwd, remove, rename
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
replacePath = getcwd + "/replaceOldLogo"
listOfPaths = [masterPath, smallerPath, smallPath, largePath]
multiUseListOfPaths = [smallerPath, smallPath, largePath]

print('')
print(getcwd, " : Directery")
print('')

repo = git.Repo(getcwd)
repo.git.stash()
repo.git.pull()

print('')
print("stashed and pulled repos")
print('')
replaceList = [f for f in listdir(replacePath) if isfile(join(replacePath, f))]

for listToReplace in replaceList:
    try:
        if listToReplace == "delete":
            pass
        else:
            for listsPaths in listOfPaths:
                try:
                    remove(listsPaths + "/" + listToReplace)
                    print('')
                    print("deleted smaller ", listToReplace)
                    print('')
                except Exception:
                    print("cannot 1 find logo for '%s'" % listToReplace)
            rename(replacePath + "/" + listToReplace, masterPath + "/" + listToReplace)
    except Exception:
        print("cannot 2 find logo for '%s'" % listToReplace)

print("done formatting")
try:
    repo.git.add('-A')
    repo.git.commit('-m Committed replaced old logos')
except Exception:
    print('')
    print('Already up to date no commit must be made')
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
sizes = [smallerSize, smallSize, largeSize]

# Find what logos are missing in the folder
missingSmaller = set(masterList).difference(smallerList)
missingSmall = set(masterList).difference(smallList)
missingLarge = set(masterList).difference(largeList)
missing = [missingSmaller, missingSmall, missingLarge]
# Find what logos are logos to delete
toDeleteSmaller = set(smallerList).difference(masterList)
toDeleteSmall = set(smallList).difference(masterList)
toDeleteLarge = set(largeList).difference(masterList)
toDelete = [toDeleteSmaller, toDeleteSmall, toDeleteLarge]

print('')
print("made it to formating")
print('')

for i in range(len(missing)):
    try:
        for ii in range(len(missing[i])):
            try:
                img = Image.open(masterPath + "/" + missing[i][ii])
                hpercent = (sizes[i] / float(img.size[1]))
                wsize = int((float(img.size[0]) * float(hpercent)))
                img = img.resize((wsize, sizes[i]), PIL.Image.ANTIALIAS)
                img.save(multiUseListOfPaths[i] + "/" + missing[i][ii], "PNG")
                print('')
                print("formating smaller ", missing[i][ii])
                print('')
            except Exception:
                print("cannot 1 create thumbnail for '%s'" % missing[i][ii])
    except IOError:
        print("cannot 2 create thumbnail for '%s'" % missing[i])

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

# deleteListOfPaths = [smallerPath, smallPath, largePath]

for i in range(len(toDelete)):
    try:
        for ii in range(len(toDelete[i])):
            try:
                remove(multiUseListOfPaths[i] + "/" + toDelete[i][ii])
                print('')
                print("deleted smaller ", toDelete[i][ii])
                print('')
            except Exception:
                print("cannot 1 find logo for '%s'" % toDelete[i][ii])
    except Exception:
        print("cannot  2 find logo for '%s'" % toDelete[i])

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
