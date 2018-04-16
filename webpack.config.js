const path = require('path');
const BundleTracker = require('webpack-bundle-tracker');
const CleanWebpackPlugin = require('clean-webpack-plugin');
const webpack = require('webpack');

module.exports = {
    mode: 'development',
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
                test: /\.css$/,
                use: ['style-loader', 'css-loader']
            }
        ]
    },
    plugins: [
        new CleanWebpackPlugin(['assets/bundles']),
        new BundleTracker({filename: './webpack-stats.json'}),
        new webpack.HotModuleReplacementPlugin(),
        new webpack.DefinePlugin({
            'process.env.NODE_ENV': JSON.stringify('production')
        })
    ]
};