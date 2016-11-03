var BundleTracker = require('webpack-bundle-tracker')
var ExtractTextPlugin = require('extract-text-webpack-plugin')
var CopyWebpackPlugin = require('copy-webpack-plugin')
var path = require('path')
var webpack = require("webpack");


/** How do we use webpack to handle static files?
 *
 * - dependencies (js, scss, and css) are installed via npm
 * - dependencies (js, scss, and css ) are moved to `vendor.(js|css)`
 *   by specifing them in the vendor entry point
 * - everything else (our js, scss) is compiled into app.(js|css)
 * - our images, fonts, icons, js, css and scss is either in each apps
 *   static folder (/euth/<appname>/static) or in the projects asset folder
 *   (/euth_wagtail/assets)
 * - after running webpack all static ressources will be in the
 *   project static folder (/euth_wagtail/static) and can then be served
 *   by django
 * - webpack compiles jsx+es2015 to js and scss to css for us
 */

module.exports = {
  entry: {
    opin: [
      './euth_wagtail/assets/scss/all.scss',
      './euth/contrib/static/js/app.js'
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
    library: '[name]',
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
