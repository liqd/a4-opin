var BundleTracker = require('webpack-bundle-tracker')

module.exports = {
  entry: './euth/contrib/static/js/app.js',
  output: {
    libraryTarget: 'var',
    library: 'Opin',
    path: './euth_wagtail/static/bundles/',
    filename: '[name].js'
  },
  externals: {
    'jquery': 'jQuery',
    'django': 'django'
  },
  plugins: [
    new BundleTracker({filename: './webpack-stats.json'})
  ]
}
