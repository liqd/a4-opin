const webpack = require('webpack')
const path = require('path')
const CopyWebpackPlugin = require('copy-webpack-plugin')
const MiniCssExtractPlugin = require('mini-css-extract-plugin')

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
    datepicker: [
      './euth_wagtail/assets/js/init-picker.js',
      'datepicker/css/datepicker.min.css'
    ],
    vendor: [
      'jquery',
      'react',
      'react-dom',
      'react-flip-move',
      'classnames',
      '@fortawesome/fontawesome-free/scss/fontawesome.scss',
      '@fortawesome/fontawesome-free/scss/brands.scss',
      '@fortawesome/fontawesome-free/scss/regular.scss',
      '@fortawesome/fontawesome-free/scss/solid.scss',
      'bootstrap-sass',
      'immutability-helper',
      'slick-carousel/slick/slick.min.js',
      'slick-carousel/slick/slick.css',
      './euth_wagtail/assets/js/jquery-fix.js',
      './euth_wagtail/assets/js/modernizr-custom.js'
    ],
    timeline_popover: [
      './euth/projects/static/euth_projects/timeline-popover.js'
    ],
    user_search: [
      'typeahead.js',
      './euth/users/static/users/js/user_search.js'
    ],
    leaflet: [
      'leaflet',
      'leaflet/dist/leaflet.css',
      'leaflet.markercluster',
      'leaflet.markercluster/dist/MarkerCluster.css'
    ]
  },
  output: {
    libraryTarget: 'this',
    library: '[name]',
    path: path.resolve('./euth_wagtail/static'),
    publicPath: '/static/',
    filename: '[name].js'
  },
  externals: {
    django: 'django'
  },
  module: {
    rules: [
      {
        test: /\.jsx?$/,
        exclude: /node_modules\/(?!(adhocracy4|bootstrap)\/).*/, // exclude all dependencies but adhocracy4
        loader: 'babel-loader',
        query: {
          presets: ['@babel/preset-env', '@babel/preset-react'].map(require.resolve),
          plugins: ['@babel/plugin-transform-runtime', '@babel/plugin-transform-modules-commonjs']
        }
      },
      {
        test: /\.s?css$/,
        use: [
          {
            loader: MiniCssExtractPlugin.loader
          },
          {
            loader: 'css-loader'
          },
          {
            loader: 'postcss-loader',
            options: {
              ident: 'postcss',
              plugins: [
                require('autoprefixer')
              ]
            }
          },
          {
            loader: 'sass-loader'
          }
        ]
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
      bootstrap: 'bootstrap-sass/assets/stylesheets/bootstrap'
    }
  },
  plugins: [
    new webpack.optimize.SplitChunksPlugin({
      name: 'vendor',
      filename: 'vendor.js'
    }),
    new MiniCssExtractPlugin({
      filename: '[name].css',
      chunkFilename: '[id].css'
    }),
    new CopyWebpackPlugin([
      {
        from: './euth_wagtail/assets/images/*',
        to: 'images/',
        flatten: true
      },
      {
        from: './euth_wagtail/assets/icons/*',
        to: 'icons/',
        flatten: true
      },
      {
        from: './euth_wagtail/assets/category_icons/**/*',
        to: 'category_icons/',
        flatten: true
      }
    ])
  ]
}
