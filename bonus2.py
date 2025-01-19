filenames = ["1.Raw Data.txt", "2.Reports.txt", "3.Presentations.txt"]

# for filename in filenames:
#     print(filename.replace(".","-",1))

new_filenames = [filename.replace(".","-",1) for filename in filenames]

print(new_filenames)