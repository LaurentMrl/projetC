import unittest
import pathlib as pl
import os
import time

# class TestCaseBase(unittest.TestCase):
#     def assertIsFile(self, path):
#         if not pl.Path(path).resolve().is_file():
#             raise AssertionError(f"File does not exist: {path}")

# class ActualTest(TestCaseBase):
#     def test(self):
#         path = pl.Path("a/b/c.txt")
#         self.assertIsFile(path)


# Je check si le csv à bien été modifié il y a moins de 10 secondes, si oui on le considère à jour, sinon non.
def checkCSVUpdateTime(fileName):
    path = fr"C:\Users\laure\Documents\GithubPro\PROJETC\{fileName}.csv"
    # open(path, 'w+')
    fileTime = os.path.getmtime(path)
    nowTime = time.time() #returns the unix timestamp
    print(f"fileTime : {fileTime}")
    print(f"nowTime : {nowTime}")
    lastUpdateTime =abs(nowTime - fileTime)
    if nowTime == fileTime:
        print(f"nowTime and fileTIme are the same : {fileTime}")
    if lastUpdateTime <= 10:
        print(f"The file {fileName} has been updated !")
    else:
        print(f"The file {fileName} has not been updated! Last time was {lastUpdateTime} secs ago")


checkCSVUpdateTime("ouais")