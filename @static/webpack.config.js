const path = require('path');
const UglifyJSPlugin = require('uglifyjs-webpack-plugin');

module.exports = {
    context: path.resolve(__dirname),
    entry: './index.ts',

    output: {
        path: path.resolve(__dirname, "../react_habitat/static/react_habitat"),
        filename: 'react-habitat-bundle.min.js'
    },

    plugins: [
        new UglifyJSPlugin()
    ],
    module: {
        rules: [
            {
                test: /\.tsx?/,
                exclude: /node_modules/,
                loader: 'awesome-typescript-loader',
                // use: "awesome-typescript-loader",
                query: {
                    // Use this to point to your tsconfig.json.
                    configFileName: './tsconfig.json'
                }
            },
            {
                test: require.resolve('react-habitat'),
                use: [
                    {
                        loader: 'expose-loader',
                        options: 'ReactHabitat'
                    }
                ]
            },
            {
                test: require.resolve('react'),
                use: [
                    {
                        loader: 'expose-loader',
                        options: 'React'
                    }
                ]
            },
            {
                test: require.resolve('react-dom'),
                use: [
                    {
                        loader: 'expose-loader',
                        options: 'ReactDOM'
                    }
                ]
            }
        ]
    },
    resolve: {
        extensions: [".webpack.js", "web.js", ".ts", ".tsx", ".js"],
        modules: ["node_modules"]
    },
};