import csv
import pickledb
import base64
import json
import ipdb
from pygeocoder import Geocoder
from pygeolib import GeocoderError

def getAddress(address, db):
  # clean whitespace first
  address = address.strip().lower()
  
  # create base64 key from address
  base64_key = base64.b64encode(address)

  # check for key
  value = db.get(base64_key)
  
  if (value is not None):
    data = json.loads(value)
    json_address = data['data'][0]
    print "value exists: ", json_address['formatted_address']
    return json_address
  else:
    try:
      address = Geocoder('AIzaSyALz8wDmVs2Fzx4gdMJtAlPWf_nUQjl5u8').geocode(address + ", Denton, Texas")
      # jsonify address object
      json_address = json.dumps(vars(address))
      # store in db by base64 key
      db.set(base64_key, json_address)
      data = json.loads(json_address)
      json_address = data['data'][0]
      print "New address added:", json_address['formatted_address']
      return json_address
    except GeocoderError:
      print "The address entered could not be geocoded"
      db.set(base64_key, None)
      return None

#######################################
# Main program
#######################################
db = pickledb.load('codeviolations.db', False)

with open('trakitciscodeviol.csv','r') as csvinput:
  with open('trakitciscodeviol-geo.csv', 'w') as csvoutput:
    writer = csv.writer(csvoutput, lineterminator='\n')
    reader = csv.reader(csvinput)

    all = []
    row = next(reader)
    row.append('zip')
    row.append('formatted_address')
    row.append('latitude')
    row.append('longitude')
    all.append(row)
    count = 0
    for row in reader:
      street = row[3]
      address = getAddress(street, db)
      if (address is not None):
        print "Address: ", address
        # ipdb.set_trace()

        # append new data to row
        row.append(address['address_components'][6]['short_name'])
        row.append(address['formatted_address'])
        row.append(address['geometry']['location']['lat'])
        row.append(address['geometry']['location']['lng'])

        # add row to new csv
        all.append(row)
      else:
        # add empty values
        row.append("no_zip")
        row.append("no_format")
        row.append("no_lat")
        row.append("no_lon")
        all.append(row)

      # test for thing
      # count = count + 1
      # if count > 1:
      #   break

    writer.writerows(all)
