const path = require('path');
const webpack = require('webpack');
const HtmlWebpackPlugin = require('html-webpack-plugin')
const MiniCssExtractPlugin = require('mini-css-extract-plugin')


module.exports = {
  entry: './index.js',
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: 'bundle.js'
  },
  mode: 'production',
  devtool: 'source-map',
  plugins: [
    new webpack.ProvidePlugin({
      Reveal: 'reveal.js/js/reveal.js'
    }),
    new HtmlWebpackPlugin({
      template: './index.pug',
    }),
    new MiniCssExtractPlugin({
      filename: 'bundle.css'
    })
  ],
  module: {
    rules: [
      {
        test: /\.css$/,
        use: ['style-loader', MiniCssExtractPlugin.loader, 'css-loader']
      },
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: 'babel-loader'
      },
      {
        test: /\.pug$/,
        use: 'pug-loader'
      },
      {
        test:  /\.(woff|woff2|eot|ttf|otf|png|jpg)$/,
        use: "file-loader"
      }
    ]
  }
};
