function createMap (L, baseurl, name) {
  const basemap = baseurl + '{z}/{x}/{y}.png'
  const osmAttrib = '&copy; <a href="http://openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  const baselayer = L.tileLayer(basemap, { maxZoom: 18, attribution: osmAttrib })
  const map = new L.Map('map_' + name, { scrollWheelZoom: false, zoomControl: true, minZoom: 2 })
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
  const $ = window.jQuery
  const L = window.L
  const name = window.name
  const polygon = window.polygon
  const bbox = window.bbox
  const baseurl = window.baseurl
  const map = createMap(L, baseurl, name)
  let mapVisible = $('#map_' + name).width() !== 0

  const polygonStyle = {
    color: '#0076ae',
    weight: 2,
    opacity: 1,
    fillOpacity: 0.2
  }

  let drawnItems
  if (polygon) {
    drawnItems = L.geoJson(polygon, {
      style: polygonStyle
    })
    if (drawnItems.getLayers().length > 0) {
      map.fitBounds(drawnItems)
    } else {
      map.fitBounds(getBasePolygon(L, polygon, bbox))
    }
  } else {
    drawnItems = L.featureGroup()
    map.fitBounds(getBasePolygon(L, polygon, bbox))
  }
  drawnItems.addTo(map)

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
    const layer = event.layer
    drawnItems.addLayer(layer)
    const shape = drawnItems.toGeoJSON()
    $('#id_' + name).val(JSON.stringify(shape))
  })

  map.on(L.Draw.Event.EDITED, function (event) {
    const shape = drawnItems.toGeoJSON()
    $('#id_' + name).val(JSON.stringify(shape))
  })

  map.on(L.Draw.Event.DELETED, function (event) {
    const shape = drawnItems.toGeoJSON()
    $('#id_' + name).val(JSON.stringify(shape))
  })

  $('a[data-toggle="tab"]').on('shown.bs.tab', function (e) {
    if (!mapVisible) {
      map.invalidateSize().fitBounds(getBasePolygon(L, polygon, bbox))
      mapVisible = true
    }
  })
})
