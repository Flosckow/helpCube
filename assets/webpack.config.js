const path = require('path');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const OptimizeCSSAssetsPlugin = require('optimize-css-assets-webpack-plugin');
const isDev = true ? process.env.NODE_ENV === 'development' : false;


module.exports = {
  mode: process.env.NODE_ENV,
  entry: {
    // styles
    "css/style": "./sass/style.scss",

    // scripts
    "js/main.js": './js/main.js',
  },
  output: {
    path: path.resolve(__dirname, '..','static'),
    filename: "[name]",
    publicPath: "./"
  },
  watch: !!isDev,
  watchOptions: {
    aggregateTimeout: 100
  },
  module: {
    rules: [
      {
        // js
        test: /\.js$/i,
        loader: 'babel-loader',
        include: [path.resolve(__dirname, './js/'),],
        exclude: /node_modules/,
        options: {
          presets: ["@babel/preset-env"]
        },
      },
      {
        // scss
        test: /\.(sa|sc|c)ss$/,
        include: [path.resolve(__dirname, './sass/'),],
        use: [
          MiniCssExtractPlugin.loader,
          'css-loader',
          'sass-loader',
        ]
      },
      {
        // images
        test: /\.(png|jpeg|jpg|gif|svg)$/i,
        loader: 'file-loader?name=' + './images/[name].[ext]'
      },
    ]
  },
  resolve: {
    modules: [path.resolve(__dirname), 'node_modules'],
    extensions: ['.js', '.json'],
    alias: {
      '@': path.join(__dirname, 'js/'),
      $: 'jquery',
      '$': 'jquery',
    }
  },
  optimization: {
    minimize: true ? !isDev : false,
    minimizer: [new OptimizeCSSAssetsPlugin(),]
  },
  plugins: [
    new MiniCssExtractPlugin({}),
  ]
}