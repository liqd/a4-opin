function createMap (L, baseurl, name) {
  const basemap = baseurl + '{z}/{x}/{y}.png'
  const osmAttrib = '&copy; <a href="http://openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  const baselayer = L.tileLayer(basemap, { maxZoom: 18, attribution: osmAttrib })
  const map = new L.Map('map_' + name, { scrollWheelZoom: false, zoomControl: false })
  baselayer.addTo(map)
  return map
}

function createMarker ($, L, newlatln, oldlatln, basePolygon, map, name) {
  const icon = L.icon({
    iconUrl: '/static/images/map_pin_01_2x.png',
    shadowUrl: '/static/images/map_shadow_01_2x.png',
    iconSize: [30, 45],
    iconAnchor: [15, 45],
    shadowSize: [40, 54],
    shadowAnchor: [20, 54],
    popupAnchor: [0, -45]
  })

  const marker = L.marker(newlatln, { draggable: true, icon: icon }).addTo(map)
  marker.on('dragend', function () {
    let markerInsidePolygon = false
    basePolygon.getLayers().forEach(function (each) {
      if (isMarkerInsidePolygon(marker, each)) {
        markerInsidePolygon = true
        oldlatln = marker.getLatLng()
        const shape = marker.toGeoJSON()
        $('#id_' + name).val(JSON.stringify(shape))
      }
    })
    if (!markerInsidePolygon) {
      marker.setLatLng(oldlatln)
    }
  })
  return marker
}

function isMarkerInsidePolygon (marker, poly) {
  const polyPoints = poly.getLatLngs()
  const x = marker.getLatLng().lat
  const y = marker.getLatLng().lng

  let inside = false
  for (let i = 0, j = polyPoints.length - 1; i < polyPoints.length; j = i++) {
    const xi = polyPoints[i].lat
    const yi = polyPoints[i].lng
    const xj = polyPoints[j].lat
    const yj = polyPoints[j].lng

    const intersect = ((yi > y) !== (yj > y)) &&
        (x < (xj - xi) * (y - yi) / (yj - yi) + xi)
    if (intersect) inside = !inside
  }
  return inside
}

window.jQuery(document).ready(function () {
  const $ = window.jQuery
  const L = window.L
  const name = window.name
  const polygon = window.polygon
  const point = window.point
  const baseurl = window.baseurl
  const map = createMap(L, baseurl, name)

  const polygonStyle = {
    color: '#0076ae',
    weight: 2,
    opacity: 1,
    fillOpacity: 0.2
  }

  const basePolygon = L.geoJson(polygon, { style: polygonStyle }).addTo(map)
  map.fitBounds(basePolygon)
  map.options.minZoom = map.getZoom()
  L.control.zoom({
    position: 'topleft'
  }).addTo(map)

  let marker

  if (point) {
    L.geoJson(point, {
      pointToLayer: function (feature, newlatlng) {
        const oldlatlng = newlatlng
        marker = createMarker($, L, newlatlng, oldlatlng, basePolygon, map, name)
        return marker
      }
    })
  }

  basePolygon.on('click', function (event) {
    if (typeof marker === 'undefined') {
      const oldlatlng = event.latlng
      marker = createMarker($, L, event.latlng, oldlatlng, basePolygon, map, name)
      const shape = marker.toGeoJSON()
      $('#id_' + name).val(JSON.stringify(shape))
    }
  })
})
