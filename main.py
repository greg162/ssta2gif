from datetime import date, timedelta, datetime
import urllib
import imageio #Can be installed with pip using the command 'pip install imageio'
import os.path 

fileList = [] #Used to store all the file paths for the final gif.
d1       = date(2018, 9, 1)  # start date: Change this to the date we should start looking from
d2       = date(2018, 11, 22)  # end date: Change this to the dat we should stop looking at.
delta    = d2 - d1 # timedelta

for i in range(delta.days + 1):
  #Set all variables needed to process an image.
  currentDateString = str(d1 + timedelta(i))
  urlFormatDateTime = datetime.strptime(currentDateString, '%Y-%m-%d').strftime("%-m.%-d.%Y")
  fileFormateDate   = datetime.strptime(currentDateString, '%Y-%m-%d').strftime("%Y-%m-%d")
  urlYear           = datetime.strptime(currentDateString, '%Y-%m-%d').strftime("%Y")
  url               = "https://www.ospo.noaa.gov/data/sst/anomaly/"+urlYear+"/anomnight."+urlFormatDateTime+".gif"
  fileName          = "_images/" + fileFormateDate + ".gif"

  #If the file already exists, don't import it.
  if(os.path.isfile(fileName) == False):
    print "Requesting URL: " + url
    request           = urllib.urlopen(url)
    if(request.getcode() == 200):
      print "Image found... saving to script directory."
      output = open(fileName,"wb")
      output.write(request.read())
      output.close()
      fileList.append(fileName)
    else:
      print "Could not open url."
  else:
    print "already exists, skipping!"
    fileList.append(fileName)


print "All relevant images saved... creating GIF"
#Imagio used to create a gif from all the images we imported.
with imageio.get_writer('ssta-animation.gif', mode='I', duration= 0.15) as writer:
  for fileName in fileList:
    image = imageio.imread(fileName)
    writer.append_data(image)
    
print "SCRIPT COMPLETE!"