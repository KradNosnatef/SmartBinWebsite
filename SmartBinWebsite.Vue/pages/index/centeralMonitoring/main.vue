<template>
	<view>
		<MyMap :points="points" @selectBin="selectBin"></MyMap>
		<BinItemCard></BinItemCard>
	</view>
</template>

<script>
	import BinItemCard from "./BinItemCard.vue"
	import MyMap from "./Map.vue"
	export default {
		data() {
			return {
				points:[
					{
						lng:103.7948,
						lat:1.3329
					},
					{
						lng:103.7938,
						lat:1.3758
					}
				]
			}
		},
		components:{
			BinItemCard,
			MyMap
		},
		methods: {
			selectBin(event){
				console.log("hi everyone"+event.index)
			}
		}
	}
</script>

<style>

</style>
