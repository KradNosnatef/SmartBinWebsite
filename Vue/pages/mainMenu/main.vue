<template>
	<view>
		<div style="margin-top: 20px;margin-left: 20px; margin-right: 20px;">
			<button style="margin: 10px;" @click="gotoCenteralMonitoring">Centeral Monitoring</button>
			<button style="margin: 10px;">Register New Bin</button>
			<button style="margin: 10px;" @click="callBIDInputDialog('realTimeTelemetry/main')">Real-time telemetry</button>
			<button style="margin: 10px;" @click="callBIDInputDialog('logInfo/main')">Get Log Data</button>
		</div>
		<dialog id="dialog" style="margin: auto;">
			<h1>Enter the Bin ID</h1>
			<input v-model="BIDInput" style="outline-style: auto;" placeholder="enter the BID" type="number"></input>
			<div style="margin-left: 0px;margin-right: 0px;margin-top: 10px;">
				<button style="float: left;" @click="gotoNextPage">Continue</button>
				<button style="float: right;" @click="closeDialog">Escape</button>
			</div>
		</dialog>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				dialogRouterTarget:"",
				BIDInput:null
			}
		},
		onShow() {
		},
		methods: {
			gotoCenteralMonitoring(){
				uni.navigateTo({
					url:"/pages/centralMonitoring/main"
				})
			},
			callBIDInputDialog(targetPagePath){
				this.dialogRouterTarget=targetPagePath
				dialog.showModal()
			},
			gotoNextPage(){
				console.log(this.BIDInput)
				dialog.close()
				uni.navigateTo({
					url:"/pages/"+this.dialogRouterTarget+"?BID="+this.BIDInput
				})
			},
			closeDialog(){
				dialog.close()
			}
		}
	}
</script>

<style>

</style>
