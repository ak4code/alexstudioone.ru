const path = require('path');
const BundleTracker = require('webpack-bundle-tracker');
const CleanWebpackPlugin = require('clean-webpack-plugin');
const ExtractTextPlugin = require('extract-text-webpack-plugin');
const webpack = require('webpack');
const extractSCSS = new ExtractTextPlugin('[name].min.css');

module.exports = {
    entry: {
        app: './assets/js/index.js',
    },
    output: {
        path: path.resolve('./assets/bundles/'),
        chunkFilename: '[name].bundle.js',
        filename: '[name].bundle.js',
        publicPath: 'http://localhost:8080/assets/bundles/',
    },
    devtool: 'inline-source-map',
    devServer: {
        hot: true
    },
    module: {
        rules: [
            {
                test: /\.(png|svg|jpg|gif)$/,
                use: [
                    'file-loader'
                ]
            },
            {
                test: /\.scss/i,
                exclude: /node_modules/,
                use: extractSCSS.extract(['css-loader', 'sass-loader'])
            },
            {
                test: /\.js$/,
                exclude: /node_modules/,
                use: {
                    loader: 'babel-loader'
                }
            }
        ]
    },
    plugins: [
        new CleanWebpackPlugin(['assets/bundles']),
        new BundleTracker({filename: './webpack-stats.json'}),
        extractSCSS,
        new webpack.HotModuleReplacementPlugin(),
        new webpack.DefinePlugin({
            'process.env.NODE_ENV': JSON.stringify('production')
        }),
        new webpack.ProvidePlugin({
            $: 'jquery',
            jQuery: 'jquery'
        })
    ]
};