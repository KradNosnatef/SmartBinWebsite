<template>
	<div>
		<p>
			BID :{{dialogSettings.BID}}
		</p>
		<p>Longitude: {{dialogSettings.lng}}</p>
		<p>Latitude: {{dialogSettings.lat}}</p>
		</br>
		<p>Most Recent Alert: {{dialogSettings.recentAlert}} </br>at {{dialogSettings.recentAlertTimeText}}</p>
		<button @click="onClick" style="margin-top: 5px;">goto Log Info</button>
		<button @click="onClickCancel" style="margin-top: 5px;">cancel</button>
	</div>
</template>

<script>
	export default {
		props: {
			dialogSettings: Object
		},
		data() {
			return {

			}
		},
		onShow() {
		},
		methods: {
			onClick() {
				uni.navigateTo({
					url:"/pages/logInfo/main?BID="+this.dialogSettings.BID
				})
			},
			onClickCancel(){
				this.$emit("cancel")
			}
		}
	}
</script>

<style>

</style>
