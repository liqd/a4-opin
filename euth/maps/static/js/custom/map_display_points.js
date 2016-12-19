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

  var customOptions =
    {
      'className': 'maps-popups',
      closeButton: false
    }

  var basePolygon = L.geoJson(polygon, {style: polygonStyle}).addTo(map)
  map.fitBounds(basePolygon)

  function getImage (feature) {
    if (feature.properties.image) {
      return '<div class="maps-popups-popup-image" style="background-image:url(' + feature.properties.image + ');"></div>'
    }
    return ''
  }

  L.geoJson(point, {
    pointToLayer: function (feature, latlng) {
      var marker = L.marker(latlng, {draggable: false}).addTo(map)
      var popupContent = getImage(feature) +
                        '<div class="maps-popups-popup-meta">' +
                            '<span class="idea-upvotes idea-meta-item">' +
                            feature.properties.positive_rating_count + ' <i class="fa fa-chevron-up" aria-hidden="true"></i>' +
                            '</span>' +
                            '<span class="idea-downvotes idea-meta-item">' +
                            feature.properties.negative_rating_count + ' <i class="fa fa-chevron-down" aria-hidden="true"></i>' +
                            '</span>' +
                            '<span class="idea-comments-count idea-meta-item">' +
                            feature.properties.comments_count + ' <i class="fa fa-comment-o" aria-hidden="true"></i>' +
                            '</span>' +
                            '</div>' +
                        '<div class="maps-popups-popup-name"><a href="' + feature.properties.url + '">' + feature.properties.name + '</a></div>'

      marker.bindPopup(popupContent, customOptions)
      return marker
    }
  })
})
