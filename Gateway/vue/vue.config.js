const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  devServer:{
    proxy:{
      '/cmd':{
        target:'http://localhost:25565',
        changeOrigin:true
      }
    }
  }

})
