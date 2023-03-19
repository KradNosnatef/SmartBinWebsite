<template>
	<view>
		<text v-for="row in RawText">
			<br>
			{{row[4]}} :
			<br>
			weight: {{row[0]}}; distance:{{row[1]}}; pitch:{{row[2]}}; roll:{{row[3]}};
			<br>

		</text>
	</view>
</template>

<script>
	export default {
		onLoad(option) {
			this.BID=option.BID
			this.refershRawText()
			setInterval(this.refershRawText,5000)
		},
		data() {
			return {
				BID:null,
				RawText: []
			}
		},
		methods: {
			refershRawText() {
				console.log(this.BID)
				uni.request({
					url: "/Wapi/getRawInfoByBID",
					method: 'POST',
					data: {
						BID:this.BID
					},
					success: (response) => {
						this.RawText = response.data
					}
				})
			}
		}
	}
</script>

<style>

</style>
