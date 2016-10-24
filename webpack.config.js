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
        loader: 'style!css!sass?sourceMap!resolve-url'
      },
      {
        test: /\.woff2?$|\.ttf$|\.eot$/,
        loader: 'file?name=/static/fonts/[name].[ext]'
      },
      {
        test: /\.svg$|\.png$/,
        loader: 'file?name=/static/images/[name].[ext]'
      }
    ]
  },
  resolveLoader: {
    fail: true
  },
  resolve: {
    extensions: ['', '.js', '.jsx', '.scss', '.css'],
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
