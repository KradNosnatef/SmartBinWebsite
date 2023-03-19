<template>
	<view class="content">
		<div style="margin-top: 5%;margin-left: 10px;margin-right: 10px;">
			<view class="text-area">
				<text class="title">Input admin password and press button to login into ADMIN mode</text>
			</view>
			<view class="text-area">
				<text class="title">or</text>
			</view>
			<view class="text-area">
				<text class="title">Press login button without password to visit in GUEST mode</text>
			</view>
		</div>
		<div style="margin-top: 30px;">
			<form>
				<input type="text" name="password" style="outline:auto ;" v-model="value" placeholder="ADMIN Password"/>
			</form>
			<button style="margin-top: 10px; margin-bottom: 30px;" @click="onClickLogin">login</button>
		</div>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				value:""
			}
		},
		onLoad() {
			
		},
		methods: {
			onClickLogin(){
				if(this.value!=""){
					alert("Wrong Password")
				}
				else{
					uni.navigateTo({
						url:"/pages/mainMenu/main"
					})
				}
			}
		}
	}
</script>

<style>
	.content {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		outline-style: auto;
	}

	.logo {
		height: 200rpx;
		width: 200rpx;
		margin-top: 200rpx;
		margin-left: auto;
		margin-right: auto;
		margin-bottom: 50rpx;
	}

	.text-area {
		display: flex;
		justify-content: center;
	}

	.title {
		font-size: 36rpx;
		color: black;
	}
</style>
