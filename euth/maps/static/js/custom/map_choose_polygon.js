function createMap (L, baseurl, name) {
  var basemap = baseurl + '{z}/{x}/{y}.png'
  var osmAttrib = '&copy; <a href="http://openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  var baselayer = L.tileLayer(basemap, { maxZoom: 18, attribution: osmAttrib })
  var map = new L.Map('map_' + name)
  baselayer.addTo(map)
  return map
}

function getBasePolygon (L, polygon, bbox) {
  if (polygon) {
    if (polygon.type === 'FeatureCollection' && polygon.features.length === 0) {
      return bbox
    }
    return L.geoJson(polygon)
  } else {
    return bbox
  }
}

window.jQuery(document).ready(function () {
  var $ = window.jQuery
  var L = window.L
  var name = window.name
  var polygon = window.polygon
  var bbox = window.bbox
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

  if (polygon) {
    L.geoJson(polygon, {
      style: polygonStyle,
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
    if (drawnItems.getLayers().length > 0) {
      map.fitBounds(drawnItems)
    } else {
      map.fitBounds(getBasePolygon(L, polygon, bbox))
    }
  } else {
    map.fitBounds(getBasePolygon(L, polygon, bbox))
  }

  map.addControl(new L.Control.Draw({
    edit: {
      featureGroup: drawnItems,
      edit: {
        selectedPathOptions: {
          maintainColor: true
        }
      }
    },
    draw: {
      polygon: {
        shapeOptions: polygonStyle
      },
      rectangle: {
        shapeOptions: polygonStyle
      },
      marker: false,
      polyline: false,
      circle: false
    }
  }))

  map.on(L.Draw.Event.CREATED, function (event) {
    var layer = event.layer
    drawnItems.addLayer(layer)
    var shape = drawnItems.toGeoJSON()
    $('#id_' + name).val(JSON.stringify(shape))
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
      map.invalidateSize().fitBounds(getBasePolygon(L, polygon, bbox))
      mapVisible = true
    }
  })
})
