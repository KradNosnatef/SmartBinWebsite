<template>
	<view>
		<MyMap v-bind:points="points" @selectBinByMap="selectBinByMapHandler"></MyMap>
		<p v-for="bin in bins">
			<BinItemCard v-bind:bin="bin" @selectBinByButton="selectBinByButtonHandler"></BinItemCard>
		</p>
		
		<dialog id="binInfoDialog" style="margin: auto;">
			<BinInfoDialog v-bind:dialogSettings="dialogSettings"></BinInfoDialog>
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
				bins:[],
				points: [],
				dialogSettings:{
					BID:0,
					lat:0,
					lng:0,
					recentAlert:""
				}
			}
		},
		onShow() {
			uni.request({
				url: "/Wapi/getBinBriefing",
				method: 'GET',
				success: (res) => {
					this.bins=[]
					this.points = []
					//console.log(res.data)
					for (var i = 0; i < res.data.length; i++) {
						
						this.points[i] = {}
						//console.log(res.data[i].longitude)
						this.points[i].lng = res.data[i].longitude
						this.points[i].lat = res.data[i].latitude
						//console.log(i)
						
						this.bins[i]={
							BID:res.data[i].BID,
							lat:res.data[i].latitude,
							lng:res.data[i].longitude,
							recentAlert:res.data[i].text
						}
					}
					console.log(this.bins)
				}
			})


			//console.log("refresh bin briefing")

		},
		components: {
			BinItemCard,
			MyMap,
			BinInfoDialog
		},
		methods: {
			selectBinByMapHandler(event) {
				console.log("the index:" + event.index +" is selected")
				this.selectBinHandler(event.index)
			},
			selectBinByButtonHandler(event) {
				var index=0
				for(var i=0;i<this.bins.length;i++){
					if (event.BID==this.bins[i].BID){
						index=i
						break
					}
				}
				console.log("the index:" + index +" is selected")
				this.selectBinHandler(index)
			},
			
			selectBinHandler(index){
				this.dialogSettings.BID=this.bins[index].BID
				this.dialogSettings.lat=this.bins[index].lat
				this.dialogSettings.lng=this.bins[index].lng
				this.dialogSettings.recentAlert=this.bins[index].recentAlert
				
				binInfoDialog.showModal()
			}
		}
	}
</script>

<style>

</style>
