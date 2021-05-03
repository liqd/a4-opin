const webpack = require('webpack')
const path = require('path')
const CopyWebpackPlugin = require('copy-webpack-plugin')
const MiniCssExtractPlugin = require('mini-css-extract-plugin')

/** How do we use webpack to handle static files?
 *
 * - dependencies (js, scss, and css) are installed via npm
 * - dependencies (js, scss, and css ) are moved to `adhocracy.(js|css)`
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
      '@fortawesome/fontawesome-free/scss/fontawesome.scss',
      '@fortawesome/fontawesome-free/scss/brands.scss',
      '@fortawesome/fontawesome-free/scss/regular.scss',
      '@fortawesome/fontawesome-free/scss/solid.scss',
      'immutability-helper',
      'slick-carousel/slick/slick.min.js',
      'slick-carousel/slick/slick.css',
      './euth_wagtail/assets/js/modernizr-custom.js',
      './euth_wagtail/assets/scss/all.scss',
      './euth_wagtail/assets/js/app.js'
    ],
    datepicker: {
      import: [
        './euth_wagtail/assets/js/init-picker.js',
        'datepicker/css/datepicker.min.css'
      ],
      dependOn: 'adhocracy4'
    },
    user_search: {
      import: [
        'typeahead.js/dist/typeahead.jquery.min.js',
        './euth/users/static/users/js/user_search.js'
      ],
      dependOn: 'adhocracy4'
    },
    flatpickr: {
      import: [
        './euth_wagtail/assets/js/init-picker.js',
        'datepicker/css/datepicker.min.css'
      ],
      dependOn: 'adhocracy4'
    },
    leaflet: {
      import: [
        'leaflet',
        'leaflet/dist/leaflet.css',
        'leaflet.markercluster',
        'leaflet.markercluster/dist/MarkerCluster.css'
      ],
      dependOn: 'adhocracy4'
    },
    // A4 dependencies - we want all of them to go through webpack
    a4maps_display_point: {
      import: [
        'leaflet/dist/leaflet.css',
        'mapbox-gl/dist/mapbox-gl.css',
        'adhocracy4/adhocracy4/maps/static/a4maps/a4maps_display_point.js'
      ],
      dependOn: 'adhocracy4'
    },
    a4maps_display_points: {
      import: [
        'leaflet/dist/leaflet.css',
        'mapbox-gl/dist/mapbox-gl.css',
        'leaflet.markercluster/dist/MarkerCluster.css',
        'adhocracy4/adhocracy4/maps/static/a4maps/a4maps_display_points.js'
      ],
      dependOn: 'adhocracy4'
    },
    a4maps_choose_point: {
      import: [
        'leaflet/dist/leaflet.css',
        'mapbox-gl/dist/mapbox-gl.css',
        'adhocracy4/adhocracy4/maps/static/a4maps/a4maps_choose_point.js'
      ],
      dependOn: 'adhocracy4'
    },
    a4maps_choose_polygon: {
      import: [
        'leaflet/dist/leaflet.css',
        'mapbox-gl/dist/mapbox-gl.css',
        'leaflet-draw/dist/leaflet.draw.css',
        'adhocracy4/adhocracy4/maps/static/a4maps/a4maps_choose_polygon.js'
      ],
      dependOn: 'adhocracy4'
    },
    category_formset: {
      import: [
        'adhocracy4/adhocracy4/categories/assets/category_formset.js'
      ],
      dependOn: 'adhocracy4'
    },
    image_uploader: {
      import: [
        'adhocracy4/adhocracy4/images/assets/image_uploader.js'
      ],
      dependOn: 'adhocracy4'
    },
    select_dropdown_init: {
      import: [
        'adhocracy4/adhocracy4/categories/assets/select_dropdown_init.js'
      ],
      dependOn: 'adhocracy4'
    },
    fileupload_formset: {
      import: [
        './euth/communitydebate/static/js/fileupload_formset.js'
      ],
      dependOn: 'adhocracy4'
    },
    blueprintsuggest: {
      import: [
        './euth/blueprints/static/euth_blueprintsuggest/js/blueprintsuggest.js'
      ],
      dependOn: 'adhocracy4'
    }
  },
  output: {
    libraryTarget: 'this',
    library: '[name]',
    path: path.resolve('./euth_wagtail/static'),
    publicPath: '/static/'
  },
  externals: {
    django: 'django'
  },
  module: {
    rules: [
      {
        test: /\.jsx?$/,
        exclude: /node_modules\/(?!(adhocracy4)\/).*/, // exclude all dependencies but adhocracy4
        loader: 'babel-loader',
        options: {
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
            loader: 'css-loader',
            options: {
              url: url => !url.startsWith('/')
            }
          },
          {
            loader: 'postcss-loader',
            options: {
              postcssOptions: {
                plugins: [
                  require('autoprefixer')
                ]
              }
            }
          },
          {
            loader: 'sass-loader'
          }
        ]
      },
      {
        test: /(fonts|files)\/.*\.(svg|woff2?|ttf|eot|otf)(\?.*)?$/,
        loader: 'file-loader',
        options: {
          name: 'fonts/[name].[ext]'
        }
      },
      {
        test: /\.svg$|\.png$/,
        loader: 'file-loader',
        options: {
          name: 'images/[name].[ext]'
        }
      }
    ]
  },
  resolve: {
    fallback: { path: require.resolve('path-browserify') },
    extensions: ['*', '.js', '.jsx', '.scss', '.css'],
    // when using `npm link`, dependencies are resolved against the linked
    // folder by default. This may result in dependencies being included twice.
    // Setting `resolve.root` forces webpack to resolve all dependencies
    // against the local directory.
    modules: [path.resolve('./node_modules')],
    alias: {
      bootstrap$: 'bootstrap/dist/js/bootstrap.bundle.min.js',
      jquery$: 'jquery/dist/jquery.min.js',
      a4maps_common$: 'adhocracy4/adhocracy4/maps/static/a4maps/a4maps_common.js'
    }
  },
  plugins: [
    new webpack.ProvidePlugin({
      $: 'jquery',
      jQuery: 'jquery',
      'window.$': 'jquery',
      'window.jQuery': 'jquery'
    }),
    new MiniCssExtractPlugin({
      filename: '[name].css',
      chunkFilename: '[id].css'
    }),
    new CopyWebpackPlugin({
      patterns: [{
        from: './euth_wagtail/assets/images/*',
        to: 'images/[name][ext]'
      },
      {
        from: './euth_wagtail/assets/icons/*',
        to: 'icons/[name][ext]'
      },
      {
        from: './euth_wagtail/assets/category_icons/**/*',
        to: 'category_icons/icons/[name][ext]'
      }]
    })
  ]
}
