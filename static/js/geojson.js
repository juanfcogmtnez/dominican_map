var mymap = L.map('mapid').setView([18.58055, -71.11079], 8);

L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: 'pk.eyJ1IjoianVhbmZjb2dtdG5leiIsImEiOiJja255OW4zc2cxZTZvMnZvYXhoZDEyNW1uIn0.eBgd1q9z4eNb-hvOVSphJg'
}).addTo(mymap);

//Con esto podemos ubicar un marcador
var marker = L.marker([18.58055, -71.11079]).addTo(mymap);

//Con esto podemos ubicar un circulo
var circle = L.circle([19.58055, -70.11079], {
    color: 'red',
    fillColor: '#f03',
    fillOpacity: 0.5,
    radius: 500
}).addTo(mymap);

//con esto un poligono
var polygon = L.polygon([
    [18.58055, -70.08],
    [18.00055, -70.58],
    [19.58055, -71.08]
]).addTo(mymap);

//podemos incluir pop-ups en los elementos
marker.bindPopup("<b>Hello world!</b><br>I am a popup.").openPopup();
circle.bindPopup("I am a circle.");
polygon.bindPopup("I am a polygon.");

//funcion para clickar en el mapa y darnos lat y long
var popup = L.popup();

function onMapClick(e) {
    popup
        .setLatLng(e.latlng)
        .setContent("You clicked the map at " + e.latlng.toString())
        .openOn(mymap);
}

mymap.on('click', onMapClick);

var states = {{name|tojson }};

console.log(states);

L.geoJSON(states, {
    style: function(feature) {
        switch (feature.properties.party) {
            case 'Republican': return {color: "#ff0000"};
            case 'Democrat':   return {color: "#0000ff"};
        }
    }
}).addTo(mymap);


