<template>
	<div>
		<button class="binItemCard" @click="onButtonClick">
			<text :style="{color:bin.onlineStatusTextColor,float:'left'}">BID:{{bin.BID}} status:{{bin.onlineStatusText}}</text>
			<br>
			<text>{{bin.recentPercentage}}%</text>
			<meter :value="bin.recentPercentage/100" :style="{width:'90%',float: 'right'}" optimum=0 low=0.3 high=0.7></meter>
			<br>
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
			},
			getOnlineStatusColor(){
				return true
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