var BundleTracker = require('webpack-bundle-tracker')
var ExtractTextPlugin = require("extract-text-webpack-plugin")
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
        loader: ExtractTextPlugin.extract('style-loader','!css-loader!sass-loader?sourceMap')
      },
      {
        test: /\.woff2?$|\.ttf$|\.eot$/,
        loader: 'file-loader?name=/static/fonts/[name].[ext]'
      },
      {
        test: /\.svg$|\.png$/,
        loader: 'file-loader?name=/static/images/[name].[ext]'
      }
    ]
  },
  resolve: {
    extensions: ['', '.js', '.jsx', '.scss', '.css']
  },
  sassLoader: {
    includePaths: [
      path.resolve('./euth_wagtail/static'),
      path.resolve('./node_modules/bootstrap-sass/assets/stylesheets')
    ]
  },
  plugins: [
    new BundleTracker({filename: './webpack-stats.json'}),
    new ExtractTextPlugin("[name].css")
  ],
  resolve: {
    extensions: ['', '.webpack.js', '.web.js', '.js', '.jsx']
  }
}
