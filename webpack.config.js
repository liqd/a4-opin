var BundleTracker = require('webpack-bundle-tracker')
var ExtractTextPlugin = require('extract-text-webpack-plugin')
var CopyWebpackPlugin = require('copy-webpack-plugin')
var path = require('path')
var webpack = require("webpack");
var autoprefixer = require('autoprefixer');


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
    adhocracy4: [
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
      'moment/locale/de',
      'moment/locale/fr',
      'moment/locale/it',
      'moment/locale/sv',
      'moment/locale/sl',
      'moment/locale/da',
      'moment/locale/el',
      'moment/locale/uk',
      'moment/locale/ru',
      'font-awesome/scss/font-awesome.scss',
      './euth_wagtail/assets/js/jquery-fix.js',
      'bootstrap-sass',
      './euth_wagtail/assets/js/modernizr-custom.js',
      'slick-carousel/slick/slick.min.js',
      'slick-carousel/slick/slick.css'
    ],
    user_search: [
      './euth/users/static/users/js/user_search.js'
    ]
  },
  devtool: 'eval',
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
        exclude: /node_modules\/(?!adhocracy4)/,  // exclude all dependencies but adhocracy4
        loader: 'babel-loader',
        query: {
          presets: ['babel-preset-es2015', 'babel-preset-react'].map(require.resolve)
        }
      },
      {
        test: /\.s?css$/,
        loader: ExtractTextPlugin.extract('style?sourceMap','!css?sourceMap!postcss?sourceMap!sass?sourceMap')
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
  postcss: [
    autoprefixer({browsers: ['last 3 versions', 'ie >= 10']})
  ],
  resolve: {
    fallback: path.join(__dirname, 'node_modules'),
    extensions: ['', '.js', '.jsx', '.scss', '.css']
  },
  resolveLoader: { fallback: path.join(__dirname, "node_modules") },
  sassLoader: {
    includePaths: [
      path.resolve('./node_modules/bootstrap-sass/assets/stylesheets')
    ]
  },
  plugins: [
    new webpack.IgnorePlugin(/^\.\/locale$/, /moment$/),
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
      },
      {
        from: './euth_wagtail/assets/scss/wagtail_admin',
        to: '',
        flatten: true
      }

    ])
  ]
}
