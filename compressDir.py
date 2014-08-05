import os
import tarfile

if not os.path.exists("filez"):
  os.mkdir("filez")
  os.chdir("filez")

  for i in xrange(100):
    thing = open("test"+str(i)+".txt","w")
    thing.write("hello"+str(i))
    thing.close()

  os.chdir("../")
  compressed_folder = "helloK.tar.gz"
  if not os.path.exists(compressed_folder):
    tar = tarfile.open(compressed_folder,"w:gz")
    tar.add("filez/",arcname="hellok")
    tar.close()

  folder = "filez"
  for a_file in os.listdir(folder):
    file_path = os.path.join(folder, a_file)
    try:
      if os.path.isfile(file_path):
        os.unlink(file_path)
    except Exception, e:
      print e
  os.rmdir("filez")

else:
  folder = "filez"
  for a_file in os.listdir(folder):
    file_path = os.path.join(folder, a_file)
    try:
      if os.path.isfile(file_path):
        os.unlink(file_path)
    except Exception, e:
      print e
  os.rmdir("filez")
  
