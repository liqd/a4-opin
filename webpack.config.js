var BundleTracker = require('webpack-bundle-tracker')

module.exports = {
  entry: './euth/contrib/static/js/app.js',
  output: {
    libraryTarget: 'var',
    library: 'Opin',
    path: './euth_wagtail/static/bundles/',
    filename: '[name].js'
  },
  module: {
    loaders: [
      { test: /\.js([x]?)$/, exclude: /node_modules/, loader: "babel-loader" },
    ]
  },
  eslint: {
    configFile: './.eslintrc'
  },
  plugins: [
    new BundleTracker({filename: './webpack-stats.json'})
  ]
}
