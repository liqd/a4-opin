var BundleTracker = require('webpack-bundle-tracker')
var path = require('path')

module.exports = {
  entry: './euth/contrib/static/js/app.js',
  devtool: 'source-map',
  entry: [
    './euth/contrib/static/js/app.js',
    './euth_wagtail/static/scss/all.scss'
  ],
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
  module: {
    loaders: [
      {
        test: /\.jsx?$/,
        exclude: /node_modules/,
        loader: 'babel-loader',
        query: {
          presets: ['es2015', 'react']
        }
      },
      {
        test: /\.scss$/,
        loader: 'style!css!resolve-url!sass?sourceMap'
      },
      {
        test: /\.woff2?$|\.ttf$|\.eot$|\.svg$|\.png$/,
        loader: 'file'
      },
    ]
  },
  resolveLoader: {
    fail: true
  },
  sassLoader: {
    includePaths: [path.resolve(__dirname, "./euth_wagtail/static")]
  },
  plugins: [
    new BundleTracker({filename: './webpack-stats.json'})
  ],
  resolve: {
    extensions: ['', '.webpack.js', '.web.js', '.js', '.jsx']
  }
}
