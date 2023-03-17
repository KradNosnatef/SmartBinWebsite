const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    port:8080,
    https: false,
    proxy: {
      "/Tapi": {
        target: "http://fuqianshan.asuscomm.com:22000",
        changeOrigin: true
      }
    }
  }
})
