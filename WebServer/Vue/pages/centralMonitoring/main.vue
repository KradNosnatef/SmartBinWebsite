<template>
	<view>
		<MyMap v-bind:points="points" v-bind:bins="bins" @selectBinByMap="selectBinByMapHandler"></MyMap>
		<p v-for="bin in bins">
			<BinItemCard v-bind:bin="bin" @selectBinByButton="selectBinByButtonHandler"></BinItemCard>
		</p>

		<dialog id="binInfoDialog" style="margin: auto;">
			<BinInfoDialog v-bind:dialogSettings="dialogSettings" @cancel="closeInfoDialog"></BinInfoDialog>
		</dialog>
	</view>
</template>

<script>
	import BinItemCard from "./BinItemCard.vue"
	import MyMap from "./Map.vue"
	import BinInfoDialog from "./BinInfoDialog.vue"
	export default {
		data() {
			return {
				bins: [],
				points: [],
				dialogSettings: {
					BID: 0,
					lat: 0,
					lng: 0,
					recentAlert: "",
					recentAlertTimeText: "",
					recentDistance: null,
					recentReportTime: null,
				}
			}
		},
		onShow() {
			this.refershBinData()
			//console.log("refresh bin briefing")
			setInterval(this.refershBinData,5000)
		},
		components: {
			BinItemCard,
			MyMap,
			BinInfoDialog
		},
		methods: {
			refershBinData() {
				uni.request({
					url: "/Wapi/getBinBriefing",
					method: 'GET',
					success: (res) => {
						this.bins = []
						this.points = []
						//console.log(res.data)
						var i=res.data.length
						for (var j = 0; j < res.data.length; j++) {
							i--
							this.points[i] = {}
							//console.log(res.data[i].longitude)
							this.points[i].lng = res.data[j].longitude
							this.points[i].lat = res.data[j].latitude
							//console.log(i)

							this.bins[i] = {
								BID: res.data[j].BID,
								lat: res.data[j].latitude,
								lng: res.data[j].longitude,
								recentAlert: res.data[j].text,
								recentDistance: res.data[j].nearestDistance,
								recentReportTime:res.data[j].nearestReportTime
							}
							if (this.bins[i].recentReportTime>300){
								this.bins[i].onlineStatusText="offline"
								this.bins[i].onlineStatusTextColor="red"
							}
							else {
								this.bins[i].onlineStatusText="online"
								this.bins[i].onlineStatusTextColor="green"
							}

							if (this.bins[i].recentDistance != null) this.bins[i].recentPercentage = Math
								.round((-0.434) * this.bins[i].recentDistance + 170)
							else this.bins[i].recentPercentage = 0

							if (this.bins[i].recentPercentage > 100) this.bins[i].recentPercentage = 100
							if (this.bins[i].recentPercentage < 0) this.bins[i].recentPercentage = 0

						}
						console.log(this.bins)
					}
				})



			},

			selectBinByMapHandler(event) {
				console.log("the index:" + event.index + " is selected")
				this.selectBinHandler(event.index)
			},
			selectBinByButtonHandler(event) {
				var index = 0
				for (var i = 0; i < this.bins.length; i++) {
					if (event.BID == this.bins[i].BID) {
						index = i
						break
					}
				}
				console.log("the index:" + index + " is selected")
				this.selectBinHandler(index)
			},

			selectBinHandler(index) {
				this.dialogSettings.BID = this.bins[index].BID
				this.dialogSettings.lat = this.bins[index].lat
				this.dialogSettings.lng = this.bins[index].lng


				uni.request({
					url: "/Wapi/getAlertsByBID",
					method: 'POST',
					data: {
						BID: this.bins[index].BID
					},
					success: (response) => {
						//console.log(response.data[0][1])
						this.dialogSettings.recentAlert = this.bins[index].recentAlert
						this.dialogSettings.recentAlertTimeText = response.data[0][1]
					}
				})
				binInfoDialog.showModal()
			},

			closeInfoDialog() {
				binInfoDialog.close()
			}
		}
	}
</script>

<style>

</style>
