var ExtractTextPlugin = require('extract-text-webpack-plugin')
var path = require('path')
var webpack = require('webpack');
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
      './euth_wagtail/static/scss/all.scss',
      './euth/contrib/static/js/app.js'
    ],
    datepicker: [
      './euth_wagtail/static/js/init-picker.js',
      'datepicker/css/datepicker.min.css'
    ],
    vendor: [
      'jquery',
      'react',
      'react-dom',
      'react-flip-move',
      'classnames',
      'font-awesome/scss/font-awesome.scss',
      './euth_wagtail/static/js/jquery-fix.js',
      'bootstrap-sass',
      'immutability-helper',
      './euth_wagtail/static/js/modernizr-custom.js',
      'slick-carousel/slick/slick.min.js',
      'slick-carousel/slick/slick.css'
    ],
    user_search: [
      './euth/users/static/users/js/user_search.js'
    ],
    leaflet: [
      'leaflet',
      'leaflet/dist/leaflet.css',
      'leaflet.markercluster',
      'leaflet.markercluster/dist/MarkerCluster.css'
    ],
  },
  output: {
    libraryTarget: 'var',
    library: '[name]',
    path: path.resolve('./euth_wagtail/static/bundles'),
    publicPath: '/static/bundles/',
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
          presets: ['babel-preset-env', 'babel-preset-react'].map(require.resolve)
        }
      },
      {
        test: /\.s?css$/,
        use: ExtractTextPlugin.extract({
          fallback: 'style-loader',
          use: [
            'css-loader',
            {
              loader: 'postcss-loader',
              options: {
                ident: 'postcss',
                plugins: (loader) => [
                  autoprefixer({browsers: ['last 3 versions', 'ie >= 10']})
                ]
              }
            },
            {
              loader: 'sass-loader'
            }
          ]
        })
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
    extensions: ['*', '.js', '.jsx', '.scss', '.css'],
    // when using `npm link`, dependencies are resolved against the linked
    // folder by default. This may result in dependencies being included twice.
    // Setting `resolve.root` forces webpack to resolve all dependencies
    // against the local directory.
    modules: [path.resolve('./node_modules')],
    alias: {
      'bootstrap': 'bootstrap-sass/assets/stylesheets/bootstrap'
    }
  },
  plugins: [
    new webpack.optimize.CommonsChunkPlugin({ name: 'vendor', filename: 'vendor.js'}),
    new ExtractTextPlugin('[name].css'),
  ]
}
