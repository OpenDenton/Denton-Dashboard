[![Stories in Ready](https://badge.waffle.io/OpenDenton/Denton-Dashboard.png?label=ready&title=Ready)](https://waffle.io/OpenDenton/Denton-Dashboard)
# Denton-Dashboard
Static dashboard for open data in Denton.

* [Geo Server](#geo-server)
  * [Geo Parameters](#parameter-breakdown)
  * [SQL View Parameters](#geo-server)
* [Sheetsu API](#sheetsu-api)

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
**srs** | `EPSG:2276` | standard projection encoding; 2276, e.g., is Texas State Plane, "<a href="http://spatialreference.org/ref/epsg/nad83-texas-north-central-ftus/">Texas North Central</a>", and would be standard for lots of City of Denton and Denton County GIS data sets, because it's quite precise compared to continental or geographic projections.
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

### Sheetsu API

View the [Sheetsu API docs (beta)](https://sheetsu.com/docs/beta).

Dataset | API URL | Description
------- | ------- | ---------------
Community Facilities | [https://sheetsu.com/apis/2705ee3b](https://sheetsu.com/apis/2705ee3b) | A list of facilities around town.
Code Violations | [https://sheetsu.com/apis/41293eb6](https://sheetsu.com/apis/41293eb6) | List of code violations filtered by GeoID (block)
Crime Reports | [https://sheetsu.com/apis/bb1d8d0d](https://sheetsu.com/apis/bb1d8d0d) | Aggregation of crime reports.
Homeless Survey (2013) | [https://sheetsu.com/apis/6208b1ef](https://sheetsu.com/apis/6208b1ef) | Survey of homelessness in City of Denton for 2013.
Crime Reports (Jan 2013) | [https://sheetsu.com/apis/bef664cf](https://sheetsu.com/apis/bef664cf) | List of crime report data for January 2013
