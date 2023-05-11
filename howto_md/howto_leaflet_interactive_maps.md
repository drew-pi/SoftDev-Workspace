# how-to :: Create a simple interactive map with Leaflet 
---
## Overview
Leaflet is a javascript, frontend, library that allows you to render an interactive map into a browser. It can be used to create markers, heat/choropleth maps, etc to visualize data.It is not the most complex library because each map is treated like a huge picture and there are no seperate objects like roads, buildings, etc, so you can't create bootleg google maps with this library. 

### Estimated Time Cost: 0.5 - 1.5 hrs


### Prerequisites:

- No pre-requisite. Literally nothing, only a clear purpose because there is a lot of things you can do with this, but much easier if you come in with a clear goal/vision.
- Nothing to install, everything is imported from the cloud. You probably can install it, but this is not recommended because the library is quick to import and compact.

### I will be showing a very simple tutorial on how to setup the map, then add a few markers and create a popup. The documentation is clear and extensive and there are many tutorials showing how to do other complex tasks. I would recommend taking a look at that, it can be found in the resources section.

1. First create an html file like this (the styling info is up to you, but this will create a map that takes up the entire webpage)
```
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

2. Then you want to import the library (both css and js). You must import both because otherwise the map renders in extremely random and weird ways (I recommend you try importing one and not the other just to see what will happen).
```
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.3/dist/leaflet.css"
     integrity="sha256-kLaT2GOSpHechhsozzB+flnD+zUyjE2LlfWPgU04xyI="
     crossorigin=""/>

 <!-- Make sure you put this AFTER Leaflet's CSS -->
 <script src="https://unpkg.com/leaflet@1.9.3/dist/leaflet.js"
     integrity="sha256-WBkoXOwTeyKclOHuWtc+i2uENFpDZ9YPdf5Hf+D7ewM="
     crossorigin=""></script>
```
3. Next in the html file, create an
4. Step, with `inline code`, and/or...
5. Step, with
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
