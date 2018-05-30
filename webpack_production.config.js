var config = require('./webpack.config.js');

delete config.output.publicPath;
config.output.path = require('path').resolve('./assets/dist');

module.exports = config;