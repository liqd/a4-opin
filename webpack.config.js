var BundleTracker = require('webpack-bundle-tracker')
var ExtractTextPlugin = require('extract-text-webpack-plugin')
var CopyWebpackPlugin = require('copy-webpack-plugin')
var path = require('path')
var webpack = require("webpack");


module.exports = {
  entry: {
    app: [
      './euth/contrib/static/js/app.js',
      './euth_wagtail/assets/scss/all.scss'
    ],
    vendor: [
      'jquery',
      'react',
      'react-dom',
      'react-flip-move',
      'react-addons-update',
      'classnames',
      'moment',
      'font-awesome/scss/font-awesome.scss',
      'marked',
      './euth_wagtail/assets/js/jquery-fix.js',
      'bootstrap-sass',
      './euth_wagtail/assets/js/modernizr-custom.js',
      'owl.carousel',
      'owl.carousel/dist/assets/owl.carousel.min.css'
    ]
  },
  devtool: 'source-map',
  output: {
    libraryTarget: 'var',
    library: 'Opin',
    path: './euth_wagtail/static/',
    publicPath: "/static/",
    filename: '[name].js'
  },
  externals: {
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
        test: /\.s?css$/,
        loader: ExtractTextPlugin.extract('style-loader?sourceMap','!css-loader?sourceMap!sass-loader?sourceMap')
      },
      {
        test: /fonts\/.*\.(svg|woff2?|ttf|eot)(\?.*)?$/,
        loader: 'file-loader?name=fonts/[name].[ext]'
      },
      {
        test: /\.svg$|\.png$/,
        loader: 'file-loader?name=images/[name].[ext]'
      }
    ]
  },
  resolve: {
    extensions: ['', '.js', '.jsx', '.scss', '.css']
  },
  sassLoader: {
    includePaths: [
      path.resolve('./node_modules/bootstrap-sass/assets/stylesheets')
    ]
  },
  plugins: [
    new BundleTracker({filename: './webpack-stats.json'}),
    new webpack.optimize.CommonsChunkPlugin(/* chunkName= */"vendor", /* filename= */"vendor.js"),
    new ExtractTextPlugin('[name].css'),
    new CopyWebpackPlugin([
      {
        from: './euth_wagtail/assets/images/**/*',
        to: 'images/',
        flatten: true
      },
      {
        from: './euth_wagtail/assets/icons/favicon.ico',
        to: 'images/',
        flatten: true
      }

    ])
  ]
}
