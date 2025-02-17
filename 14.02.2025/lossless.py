import zlib 
import bz2 
def zlibrary():
 data = b"hello world" * 100 
 compress = zlib.compress(data)
 decompress = zlib.decompress(compress)

 print(f"Original Size of Data :{len(data)}")
 print(f"Compressed Size of Data : {len(compress)}")

 if data == decompress :
    print("this is the lossless data compression done by zlib") 

def bz2library():
  data = b"hello world" * 100 
  compress = bz2.compress(data)
  decompress = bz2.decompress(compress)

  print(f"Original Size of Data :{len(data)}")
  print(f"Compressed Size of Data : {len(compress)}")

  if data == decompress :
    print("this is the lossless data compression done by bz2") 
def zipFile():
 import zipfile

 with zipfile.ZipFile("test.zip", "w", zipfile.ZIP_DEFLATED) as zipf:
   zipf.write("C:\Training Finsurge\iterators.py")

   print("File zipped successfully!")
 with zipfile.ZipFile("test.zip", "r") as zipf:
    zipf.extractall("output_folder")

 print("File extracted successfully!")

zlibrary()
bz2library()
zipFile() 
