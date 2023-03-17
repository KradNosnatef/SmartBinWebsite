<template>
	<div>
		<button class="binItemCard" @click="onButtonClick">
			<text style="float:left">BID:{{bin.BID}}</text>
			<text>recent alert:{{bin.recentAlert}}</text>
		</button>
	</div>
</template>

<script>
	export default{
		props:{
			bin:Object
		},
		methods:{
			onButtonClick(){
				var event={
					BID:this.bin.BID
				}
				this.$emit("selectBinByButton",event)
			}
		}
	}
</script>

<style>
	.binItemCard{
		margin-top: 5px;
		margin-left: 5px;
		margin-right: 5px;
		border-radius: 10px;
	}
</style>