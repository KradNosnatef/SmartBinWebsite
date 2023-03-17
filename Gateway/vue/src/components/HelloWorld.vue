<template>
  <div class="hello">
    <button @click="onClickStartUp" style="font-size: 64px;margin-top: 10px;">click me to startup</button>
    <br>
    <input style="font-size: 24px;margin-top: 30px;" v-model="reportPeriod" type="number"
      placeholder="report period(second)">
    <br>
    <button @click="onClickSetReportSpeed" style="font-size: 24px;margin-top: 10px;">click me to set report speed</button>
  </div>
</template>

<script>
const axios = require('axios').default
export default {
  data() {
    return ({
      reportPeriod: null,
      isPositionSettled: false
    })
  },
  created: function () {
    this.setPosition()
  },
  activated: function () {
    this.setPosition()
  },
  methods: {
    trueSetPosition(position) {
      this.isPositionSettled=true
      var location_lon = position.coords.longitude
      var location_lat = position.coords.latitude
      console.log(location_lon, location_lat, "获取定位")
      axios.post('/cmd/setPosition', {
        latitude: location_lat,
        longitude: location_lon
      }).then(response => {
        console.log(response)
      })
    },
    setPosition() {
      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(this.trueSetPosition);
      } else {
        alert("您的设备不支持定位功能");
      }
    },
    onClickStartUp() {
      if (this.isPositionSettled != true) alert("Please Wait For Positioning Finished")
      else {
        axios.get('/cmd/startup').then(response => {
          console.log(response)
        })
      }
    },
    onClickSetReportSpeed() {
      axios.post('/cmd/setReportSpeed', {
        period: this.reportPeriod
      }).then(response => {
        console.log(response)
      })
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
