# vibr.online
<!DOCTYPE html> 
<html>
    <head>
        <link rel="stylesheet" href="https://unpkg.com/leaflet@1.6.0/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.6.0/dist/leaflet.js"></script>
<style>
    #map{position: absolute; top 0; bottom 0; left 0; right 0;}
</style>
    </head>
    <body>
        <div id = "map"></div>
        <script>
            var map = L.map('map').setView([0, 0], 1);
            L.tilelayer('https://api.maptiler.com/maps/streets/{z}/{x}/{y}.png?key=UxP36Xd9KVDL0dsaHpIF', {
                attribution: '<a href="https://www.maptiler.com/copyright/" target="_blank">&copy; MapTiler</a> <a href="https://www.openstreetmap.org/copyright" target="_blank">&copy; OpenStreetMap contributors</a>',
            }).addTo(map);
        </script>

    </body>
</html>
