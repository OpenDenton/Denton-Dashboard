import csv
import pickledb
import base64
import json
from pprint import pprint
from pygeocoder import Geocoder
from pygeolib import GeocoderError

def getAddress(address, db):
  global cached_addresses
  # clean whitespace first
  address = address.strip().lower()
  
  # create base64 key from address
  # check for key
  base64_key = base64.b64encode(address)
  value = db.get(base64_key)
  
  # if key is returned, use cached address data
  if (value is not None):
    print "Cached addresses:", cached_addresses
    cached_addresses += 1
    return value

  else:
    try:
      address = Geocoder('AIzaSyALz8wDmVs2Fzx4gdMJtAlPWf_nUQjl5u8').geocode(address + ", Denton, Texas")
      
      # jsonify address object
      json_address = {}
      json_address['postal_code'] = address.postal_code
      json_address['formatted_address'] = address.formatted_address
      json_address['latitude'] = address.coordinates[0]
      json_address['longitude'] = address.coordinates[1]
      
      # stringify json
      json_data = json.dumps(json_address)
      # store in db by base64 key
      db.set(base64_key, json_data)
      print "New address added:", json_address['formatted_address']
      return json_data

    except GeocoderError:
      print "The address entered could not be geocoded"
      db.set(base64_key, None)
      return None

#######################################
# Main program
#######################################
db = pickledb.load('codeviolations.db', False)
cached_addresses = 0

with open('trakitciscodeviol.csv','r') as csvinput:
  with open('trakitciscodeviol-geo.csv', 'w') as csvoutput:
    writer = csv.writer(csvoutput, lineterminator='\n')
    reader = csv.reader(csvinput)

    row = next(reader)
    row.extend(['postal_code', 'formatted_address', 'latitude', 'longitude'])

    pprint(row)
    writer.writerow(row)

    count = 0
    for row in reader:
      street = row[3]
      address = getAddress(street, db)

      if (address is not None):
        print "Address: ", address
        pprint(address)

        address = json.loads(address)

        pprint(address)
        # append new data to row
        row.extend([address['postal_code'], address['formatted_address'], address['latitude'], address['longitude']])

      else:
        # add empty values
        row.extend(['no_zip', 'no_format', 'no_lat', 'no_lon'])
        # all.append(row)

      writer.writerow(row)
      # test for thing
      # count += 1
      # if count > 1:
      #   break

    # writer.writerows(all)
