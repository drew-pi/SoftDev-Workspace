# how-to :: Create a simple interactive map with Leaflet 
---
## Overview
Leaflet is a javascript, frontend, library that allows you to render an interactive map into a browser. It can be used to create markers, heat/choropleth maps, etc to visualize data.It is not the most complex library because each map is treated like a huge picture and there are no seperate objects like roads, buildings, etc, so you can't create bootleg google maps with this library. 

### Estimated Time Cost: 0.5 - 1.5 hrs


### Prerequisites:

- No pre-requisite. Literally nothing, only a clear purpose because there is a lot of things you can do with this, but much easier if you come in with a clear goal/vision.
- Nothing to install, everything is imported from the cloud. You probably can install it, but this is not recommended because the library is quick to import and compact.

### I will be showing a very simple tutorial on how to setup the map, then add a few markers and create a popup. The documentation is clear and extensive and there are many tutorials showing how to do other complex tasks. I would recommend taking a look at that, it can be found in the resources section.

1. First create an html file like this (the styling info is up to you, but the way it is below will create a map that takes up the entire webpage)
```html
<!DOCTYPE html>
<html>
    <head>        
        <style>
            html, body {
                height: 100%; 
            }

            #map { height: 100%; }
        </style>

    </head>

    <body>
        <div id="map"></div>
    </body>

</html>
```

2. Then you want to import the library (both css and js). You must import both because otherwise the map renders out in extremely random and weird ways (I recommend you try importing one and not the other just to see what will happen for fun).
```html
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.3/dist/leaflet.css"
     integrity="sha256-kLaT2GOSpHechhsozzB+flnD+zUyjE2LlfWPgU04xyI="
     crossorigin=""/>

 <!-- Make sure you put this AFTER Leaflet's CSS -->
 <script src="https://unpkg.com/leaflet@1.9.3/dist/leaflet.js"
     integrity="sha256-WBkoXOwTeyKclOHuWtc+i2uENFpDZ9YPdf5Hf+D7ewM="
     crossorigin=""></script>
```
3. Now we will work on the actual javascript
    - this can be in a seperate file or in the html file itself, in this tutorial I will show how to do it in the html file itself, but to change it just add a ```src="path/to/js/file/here``` attribute to the script tags and copy and paste all of the javascript over to that other file
```html
<script>
console.log("this works");
</script>
```
OR
```html
<script src="path/to/js/file"></script> // add console.log("this works"); to the the file linked
```
4. First let's create our map object and actually add a map layer to it (I am using the open street map tile map, but there are many other options you can use)
    - These options basically let you change how the map looks. For a cleaner look, try using mapbox
```javascript
var map = L.map('map').setView([40.70160994071748, -74.01258170404392], 13);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);
```
5. Next lets add a few objects onto our map
    - You will need coordinates for this so I would recommend using this [website](http://apps.headwallphotonics.com/) to get geodata
```javascript
var marker = L.marker([40.718149, -0.09]).addTo(map); // this will create a marker on the map

var circle = L.circle([40.75696897009173, -73.98608933749239], {
    color: 'red',
    fillColor: '#f03',
    fillOpacity: 0.5,
    radius: 500
}).addTo(map); // this will create a circle

var polygon = L.polygon([
    [40.80059002992757, -73.95819593824321],
    [40.79688334088943, -73.94924547916206],
    [40.764295526562094, -73.97300777321854],
    [40.76807491724968, -73.98190465305652],
]).addTo(map); //this will create a square



```
7. Step, with
    ```
    generic code block or terminal command
    ```
   and/or...
    ```javascript
    var foo = "this that JS tho";
    ```
   and/or...
    ```python
    print("this that Python tho")
    ```
   and/or...
1. Step, with [hyperlink](https://xkcd.com)s...


### Resources
* thing1
* thing2

---

Accurate as of (last update): 2022-mm-dd

#### Contributors:  
Clyde "Thluffy" Sinclair  
Thundercleese, pd2  
Buttercup, pd7  
Blossom, pd7  
Bubbles, pd7  
Fake Grimlock, pd8  

_Note: the two spaces after each name are important! ( <--burn after reading)  _
