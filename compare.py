#place file 1 on here. 
file1name = 'maclist'
#add file 2 on here.
file2name = 'knownGoodMacs'

#this will open those files.
file1 = open(file1name, 'r')
file2 = open(file2name, 'r')

#this dictates at which line it will start reading
lineNumber = 0

success = True

#reads each line then adds +1 to move to the next line.
for line in file1:
   lineNumber += 1
   file1String = line
   file2String = file2.readline()

   if file1String != file2String:
       print('lines are different on line: ' + str(lineNumber))
       print(file1name + ': ' + file1String)
       print(file2name + ': ' + file2String)
       success = False
       
if success == True:
   print('files are equal')
   
file1.close()
file2.close()
