window.jQuery(document).ready(function () {
  var L = window.L
  var polygon = window.polygon
  var point = window.point
  var baseurl = window.baseurl

  var basemap = baseurl + '{z}/{x}/{y}.png'
  var osmAttrib = '&copy; <a href="http://openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  var baselayer = L.tileLayer(basemap, { maxZoom: 18, attribution: osmAttrib })
  var map = new L.Map('map')
  baselayer.addTo(map)

  var polygonStyle = {
    'color': '#0076ae',
    'weight': 2,
    'opacity': 1,
    'fillOpacity': 0.2
  }

  var basePolygon = L.geoJson(polygon, {style: polygonStyle}).addTo(map)
  map.fitBounds(basePolygon)

  L.geoJson(point, {
    pointToLayer: function (feature, latlng) {
      var marker = L.marker(latlng, {draggable: false}).addTo(map)
      return marker
    }
  })
})
