<template>
	<div>
		<baidu-map class="bm-view" ak="uK1MNayhkgUDF5QPuvU6fsQGuoxKEN8u" center="新加坡" :zoom="12" :double-click-zoom="false">
			<bm-point-collection v-bind:points="points" shape="BMAP_POINT_SHAPE_STAR" color="red" @click="onPointClick" @mouseover="onPointMouseOver"></bm-point-collection>
			<bm-marker :position="position" v-if="enable"></bm-marker>
			<p :key="bins.length">
				<bm-label v-for="index in bins.length" :content="bins[index-1].BID.toString()" :position="{lng:bins[index-1].lng,lat:bins[index-1].lat}"></bm-label>
			</p>
		</baidu-map>
	</div>
</template>


<script>
	import BaiduMap from 'vue-baidu-map/components/map/Map.vue'
	import BmPointCollection from 'vue-baidu-map/components/overlays/PointCollection.vue'
	import BmMarker from 'vue-baidu-map/components/overlays/Marker.vue'
	import BmLabel from 'vue-baidu-map/components/overlays/Label.vue'
	export default {
		props:{
			points:Array,
			bins:Array
		},
		mounted() {
		},
		data() {
			return {
				enable:false,
				position:{
					lng:0,
					lat:0
				}
			}
		},
		components: {
			BaiduMap,
			BmPointCollection,
			BmMarker,
			BmLabel
		},
		methods: {
			
			onPointClick(event){
				this.enable=true
				this.position.lng=event.point.lng
				this.position.lat=event.point.lat
				
				//very stupid move, but have to do this
				var index=0
				for (var i=0;i<this.points.length;i++){
					//console.log(this.points[i].lng)
					if (event.point.lng==this.points[i].lng && event.point.lat==this.points[i].lat){
						index=i;
						break;
					}
				}
				//console.log("you click point:"+index)
				
				var reEventer={
					index:index
				}
				this.$emit("selectBinByMap",reEventer)
			},
			onPointMouseOver(event){
				this.enable=true
				this.position.lng=event.point.lng
				this.position.lat=event.point.lat
			}
		}
	}
</script>

<style>
	.bm-view {
		width: 100%;
		height: 300px;
	}
</style>
