<template>
	<div>
		<p>
			BID :{{dialogSettings.BID}}
		</p>
		<p>Longitude: {{dialogSettings.lng}}</p>
		<p>Latitude: {{dialogSettings.lat}}</p>
		<p>Most Recent Alert: {{dialogSettings.recentAlert}}</p>
	</div>
</template>

<script>
	export default {
		props:{
			dialogSettings:Object
		},
		data() {
			return {
				
			}
		},
		onShow(){
		},
		methods: {
			
		}
	}
</script>

<style>

</style>
