window.jQuery(document).ready(function () {
  const L = window.L
  const polygon = window.polygon
  const point = window.point
  const baseurl = window.baseurl

  const basemap = baseurl + '{z}/{x}/{y}.png'
  const osmAttrib = '&copy; <a href="http://openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  const baselayer = L.tileLayer(basemap, { attribution: osmAttrib })
  const map = new L.Map('map', { scrollWheelZoom: false, zoomControl: false })
  baselayer.addTo(map)

  const polygonStyle = {
    color: '#0076ae',
    weight: 2,
    opacity: 1,
    fillOpacity: 0.2
  }

  const icon = L.icon({
    iconUrl: '/static/images/map_pin_01_2x.png',
    shadowUrl: '/static/images/map_shadow_01_2x.png',
    iconSize: [30, 45],
    iconAnchor: [15, 45],
    shadowSize: [40, 54],
    shadowAnchor: [20, 54],
    popupAnchor: [0, -45]
  })

  const basePolygon = L.geoJson(polygon, { style: polygonStyle }).addTo(map)
  map.fitBounds(basePolygon)
  map.options.minZoom = map.getZoom()
  L.control.zoom({
    position: 'topleft'
  }).addTo(map)

  L.geoJson(point, {
    pointToLayer: function (feature, latlng) {
      const marker = L.marker(latlng, { icon: icon }).addTo(map)
      return marker
    }
  })
})
