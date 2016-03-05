[![Stories in Ready](https://badge.waffle.io/OpenDenton/Denton-Dashboard.png?label=ready&title=Ready)](https://waffle.io/OpenDenton/Denton-Dashboard)
# Denton-Dashboard
Static dashboard for open data in Denton.

## Project Resources

### <a href="http://docs.geoserver.org/stable/en/user/data/database/sqlview.html" target="_blank">Geo Server</a>

A geo server is being setup to access a postgresql database. Here's a test URL:

<a href="http://gis01.cloudapp.net:8080/geoserver/Private/wms?service=WMS&version=1.1.0&request=GetMap&layers=Private:parcel_unt_data&styles=&bbox=2374140.5,7119699.0,2388426.5,7128551.5&width=768&height=475&srs=EPSG:2276&format=image%2Fjpeg" target="_blank">http://gis01.cloudapp.net:8080/geoserver/Private/wms?service=WMS&version=1.1.0&request=GetMap&layers=Private:parcel_unt_data&styles=&bbox=2374140.5,7119699.0,2388426.5,7128551.5&width=768&height=475&srs=EPSG:2276&format=image%2Fjpeg</a>


### Parameter Breakdown
Key | Value | Description
--- | --- | ---------------
**service** | `WMS` | N/A
**version** | `1.1.0` | Assumed version of the Geo Server
**request** | `GetMap` | Type of data being returned
**layers** | `Private:parcel_unt_data` | Specific to the data hosted on the UNT Geo server.
**styles** | `bbox=2374140.5,7119699.0,2388426.5,7128551.5` | ¯\\\_(ツ)\_/¯
**width** | `768` | Width of image in px
**height** | `475` | Height of image in px
**srs** | `EPSG:2276` | ¯\\\_(ツ)\_/¯
**format** | `image%2Fjpeg` | Format of data, HTML encoded.

#### SQL View Parameters

The SQL view parameters are specified by adding the viewparams parameter to the WMS GetMap or the WFS GetFeature request. The viewparams argument is a list of key:value pairs, separated by semicolons:

`viewparams=p1:v1;p2:v2;...`

If the values contain semicolons or commas these must be escaped with a backslash (e.g. `\,` and `\;`).

For example, the `popstates` SQL View layer can be displayed by invoking the [Layer Preview](http://docs.geoserver.org/stable/en/user/webadmin/layerpreview/index.html#layerpreview). Initially no parameter values are supplied, so the defaults are used and all the states are displayed,

To display all states having more than 20 million inhabitants the following parameter is added to the GetMap request: `&viewparams=low:20000000`

![alt text](http://docs.geoserver.org/stable/en/user/_images/sqlview-20millions.png "20 million inhabitants")

To display all states having between 2 and 5 millions inhabitants the view parameters are: `&viewparams=low:2000000;high:5000000`

![alt text](http://docs.geoserver.org/stable/en/user/_images/sqlview-2m-5m.png "2 - 5 million inhabitants")

Parameters can be provided for multiple layers by separating each parameter map with a comma:

`&viewparams=l1p1:v1;l1p2:v2,l2p1:v1;l2p2:v2,...`

The number of parameter maps must match the number of layers (featuretypes) included in the request.