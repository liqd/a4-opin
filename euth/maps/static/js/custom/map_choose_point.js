function createMap (L, baseurl, name) {
  var basemap = baseurl + '{z}/{x}/{y}.png'
  var osmAttrib = '&copy; <a href="http://openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  var baselayer = L.tileLayer(basemap, { maxZoom: 18, attribution: osmAttrib })
  var map = new L.Map('map_' + name)
  baselayer.addTo(map)
  return map
}

function isMarkerInsidePolygon (marker, poly) {
  var polyPoints = poly.getLatLngs()
  var x = marker.getLatLng().lat
  var y = marker.getLatLng().lng

  var inside = false
  for (var i = 0, j = polyPoints.length - 1; i < polyPoints.length; j = i++) {
    var xi = polyPoints[i].lat
    var yi = polyPoints[i].lng
    var xj = polyPoints[j].lat
    var yj = polyPoints[j].lng

    var intersect = ((yi > y) !== (yj > y)) &&
        (x < (xj - xi) * (y - yi) / (yj - yi) + xi)
    if (intersect) inside = !inside
  }
  return inside
}

window.jQuery(document).ready(function () {
  var $ = window.jQuery
  var L = window.L
  var name = window.name
  var polygon = window.polygon
  var point = window.point
  var baseurl = window.baseurl
  var map = createMap(L, baseurl, name)
  var mapVisible = $('#map_' + name).width() !== 0

  var drawnItems = L.featureGroup().addTo(map)

  var polygonStyle = {
    'color': '#0076ae',
    'weight': 2,
    'opacity': 1,
    'fillOpacity': 0.2
  }

  var basePolygon = L.geoJson(polygon, {style: polygonStyle}).addTo(map)
  map.fitBounds(basePolygon)

  if (point) {
    L.geoJson(point, {
      onEachFeature: function (feature, layer) {
        if (layer.getLayers) {
          layer.getLayers().forEach(function (l) {
            drawnItems.addLayer(l)
          })
        } else {
          drawnItems.addLayer(layer)
        }
      }
    })
  }

  map.addControl(new L.Control.Draw({
    edit: {
      featureGroup: drawnItems
    },
    draw: {
      polygon: false,
      rectangle: false,
      marker: true,
      polyline: false,
      circle: false
    }
  }))

  map.on(L.Draw.Event.CREATED, function (event) {
    var layer = event.layer
    basePolygon.getLayers().forEach(function (each) {
      if (isMarkerInsidePolygon(layer, each)) {
        drawnItems.addLayer(layer)
        var shape = drawnItems.toGeoJSON()
        $('#id_' + name).val(JSON.stringify(shape))
        return
      }
    })
  })

  map.on(L.Draw.Event.EDITED, function (event) {
    var shape = drawnItems.toGeoJSON()
    $('#id_' + name).val(JSON.stringify(shape))
  })

  map.on(L.Draw.Event.DELETED, function (event) {
    var shape = drawnItems.toGeoJSON()
    $('#id_' + name).val(JSON.stringify(shape))
  })

  $('a[data-toggle="tab"]').on('shown.bs.tab', function (e) {
    if (!mapVisible) {
      map.invalidateSize().fitBounds(basePolygon)
      mapVisible = true
    }
  })
})
