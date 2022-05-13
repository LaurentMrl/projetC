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

# Check if csv got edited 10 seconds ago, yes == updated else not.
def check_csv_update_time(file_name: str):
    path = rf"C:\Users\laure\Documents\GithubPro\PROJETC\{file_name}.csv"
    # open(path, 'w+')
    file_time = os.path.getmtime(path)
    now_time = time.time()  # returns the unix timestamp
    print(f"file_time : {file_time}")
    print(f"now_time : {now_time}")
    last_update_time = abs(now_time - file_time)
    if now_time == file_time:
        print(f"now_time and file_time are the same : {file_time}")
    if last_update_time <= 10:
        print(f"The file {file_name} has been updated !")
    else:
        print(
            f"The file {file_name} has not been updated! Last time was {last_update_time} secs ago"
        )


check_csv_update_time("ouais")
