<template>
	<div>
		<p>
			BID :{{dialogSettings.BID}}
		</p>
		<p>Longitude: {{dialogSettings.lng}}</p>
		<p>Latitude: {{dialogSettings.lat}}</p>
		<p>Most Recent Alert: {{dialogSettings.recentAlert}}</p>
		<button @click="onClick">test</button>
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
		onShow() {},
		methods: {
			onClick() {
				uni.request({
					url: "/Wapi/getAlertsByBID",
					method: 'POST',
					data: {
						BID: 15
					},
					success: (response) => {
						console.log(response)
					}
				})
			}
		}
	}
</script>

<style>

</style>
