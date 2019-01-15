# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 16:16:17 2019

"""


import urllib.parse
import urllib.request

import webbrowser

    
f=open('Map.html','w')

message = """
<!DOCTYPE html>

<html>
  <head>
    <meta charset="utf-8">
    <title>Street View Side-By-Side</title>
    <style>
      html, body {
        height: 100%;
        margin: 0;
        padding: 0;
      }
      #map, #pano {
        float: left;
        height: 100%;
        width: 45%;
      }
    </style>
  </head>
  <body>
    <div id="map"></div>
    <div id="pano"></div>
    <script>
           //just for test 7 trees
           var mydata = 
           [{
            "name_botanical": "Cercis spp.",
            "name_common": "Redbud",
            "family_name_botanical": "Fabaceae",
            "height_group": "1",
            "latitude": "34.0147814950108",
            "longitude": "-118.456095568836",
            "nativity": "exotic",
            "eol_id": "28998"
           },
           {
            "name_botanical": "Cercis spp.",
            "name_common": "Redbud",
            "family_name_botanical": "Fabaceae",
            "height_group": "1",
            "latitude": "34.0148173451519",
            "longitude": "-118.456114009023",
            "nativity": "exotic",
            "eol_id": "28998"
           },
           {
            "name_botanical": "Cercis spp.",
            "name_common": "Redbud",
            "family_name_botanical": "Fabaceae",
            "height_group": "1",
            "latitude": "34.0148629220535",
            "longitude": "-118.456126078963",
            "nativity": "exotic",
            "eol_id": "28998"
           },
           {
            "name_botanical": "Vacant site",
            "name_common": "Vacant Site",
            "family_name_botanical": "Unknown",
            "height_group": "0",
            "latitude": "34.0267926682335",
            "longitude": "-118.468656018376",
            "nativity": "exotic",
            "eol_id": -1
           },
           {
            "name_botanical": "Brachychiton populneus",
            "name_common": "Bottle Tree",
            "family_name_botanical": "Malvaceae",
            "height_group": "2",
            "latitude": "34.040916037816",
            "longitude": "-118.48427893826",
            "nativity": "exotic",
            "eol_id": "487630"
           },
           {
            "name_botanical": "Jacaranda mimosifolia",
            "name_common": "Jacaranda",
            "family_name_botanical": "Bignoniaceae",
            "height_group": "2",
            "latitude": "34.015711094643",
            "longitude": "-118.48130623978",
            "nativity": "exotic",
            "eol_id": "580335"
           },
           {
            "name_botanical": "Cedrus libani",
            "name_common": "Cedar-Of-Lebanon",
            "family_name_botanical": "Pinaceae",
            "height_group": "3",
            "latitude": "34.041045029598",
            "longitude": "-118.48983148415",
            "nativity": "exotic",
            "eol_id": "1061705"
           },
           {
            "name_botanical": "Ulmus parvifolia",
            "name_common": "Chinese Elm",
            "family_name_botanical": "Ulmaceae",
            "height_group": "1",
            "latitude": "34.015546408897",
            "longitude": "-118.48325293368",
            "nativity": "exotic",
            "eol_id": "595062"
           },
           {
            "name_botanical": "Ulmus parvifolia",
            "name_common": "Chinese Elm",
            "family_name_botanical": "Ulmaceae",
            "height_group": "2",
            "latitude": "34.015491210403",
            "longitude": "-118.48317981121",
            "nativity": "exotic",
            "eol_id": "595062"
           }
           ];
        
        
            //Trees Number 3, 4, 7, and 8 wrong
            var i =1;
            var lati = mydata[i].latitude;
            var long = mydata[i].longitude;
            var lati_num = Number(lati);
            var long_num = Number(long);
            
            
           function initialize() {
            var fenway = {lat: lati_num, lng:long_num};
            var map = new google.maps.Map(document.getElementById('map'), {
              center: fenway,
              zoom: 14
               
            });
            var panorama = new google.maps.StreetViewPanorama(
                document.getElementById('pano'), {
                  position: fenway,
                  pov: {
                    heading: 34,
                    pitch: 10
                  }
                });
            var marker = new google.maps.Marker({
                            position:{lat:lati_num,lng:long_num},
                            map:map
                    
                                                      });
        
         map.setStreetView(panorama);
        
      }
    </script>
    <script async defer
        src="https://maps.googleapis.com/maps/api/js?key=AIzaSyAzIfpZ8fmDUko59zGY-iIBoACbygAeBdo&callback=initialize">
    </script>
  </body>
     
  
  
  
  
  
</html>"""

f.write(message)
f.close()

webbrowser.open_new_tab('Map.html')