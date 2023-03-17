<template>
  <div class="hello">
    <p>helloFuck</p>
    <button @click="onClick">sendCommandSignal</button>
    <input v-model="textInput">
  </div>
</template>

<script>

//import axios from 'axios'
export default {
  name: 'HelloWorld',
  data() {
    return {
      textInput: "0"
    }
  },
  props: {
    msg: String
  },
  methods: {
    async onClick() {
      console.log(this.textInput)
      var port = await navigator.serial.requestPort()
      await port.open({ baudRate: 115200 })

      const encoder = new TextEncoder();
      const writer = port.writable.getWriter();
      await writer.write(encoder.encode(this.textInput + ";"));
      console.log("?")

      //const textDecoder=new TextDecoderStream()

      const decoder = new TextDecoder()
      while (port.readable) {
        const reader = port.readable.getReader();
        try {
          for(;;) {
            const { value, done } = await reader.read();
            if (done) {
              // |reader| has been canceled.
              break;
            }
            console.log(decoder.decode(value))
          }
        } catch (error) {
          // Handle |error|…
        } finally {
          reader.releaseLock();
        }
      }
    }


  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
