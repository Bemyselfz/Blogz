<template>
  <div>
    <el-menu :default-active="activeIndex"
             class="el-menu-demo"
             mode="horizontal"
             @select="handleSelect">
      <el-menu-item index="1">首页</el-menu-item>
      <el-menu-item index="2">Django</el-menu-item>
      <el-menu-item index="3">Python</el-menu-item>
      <el-menu-item index="4">HTML/CSS</el-menu-item>
      <el-menu-item index="5">Vue</el-menu-item>

    </el-menu>
  </div>
</template>

<script>
import { request } from '../network/request'
export default {
  data () {
    return {
      activeIndex: '1',
      activeIndex2: '1',
    };
  },
  methods: {
    handleSelect (key, keyPath) {
      this.$emit("postListShow")
      switch (key) {
        case '1': request({ url: "/post" })
          .then(res => {
            this.postList = res.data.results
            this.$emit('postListChange', this.postList)
          }).catch(err => {
            console.log(err)
          });
          break;
        case '2': request({ url: "/post?category=1" })
          .then(res => {
            this.postList = res.data.results
            this.$emit('postListChange', this.postList)
          }).catch(err => {
            console.log(err)
          });
          break;
        case '3': request({ url: "/post?category=4" })
          .then(res => {
            this.postList = res.data.results
            this.$emit('postListChange', this.postList)
          }).catch(err => {
            console.log(err)
          });
          break;
        case '4': request({ url: "/post?category=3" })
          .then(res => {
            this.postList = res.data.results
            this.$emit('postListChange', this.postList)
          }).catch(err => {
            console.log(err)
          });
          break;
        case '5': request({ url: "/post?category=2" })
          .then(res => {
            this.postList = res.data.results
            this.$emit('postListChange', this.postList)
          }).catch(err => {
            console.log(err)
          });
          break;
      }
    }
  },
  watch: {

  }
}
</script>

<style scoped>
.el-menu.el-menu--horizontal {
  width: 80%;
  margin: 0 auto;
  background: #333;
  border-bottom: solid 0px #e6e6e6;
}
.el-menu--horizontal > .el-menu-item {
  height: 50px;
  line-height: 50px;
  font-size: 18px;
  color: #fff;
  font-family: Arial, Helvetica, sans-serif;
  margin-left: 10px;
}
.el-menu--horizontal > .el-menu-item.is-active {
  border-bottom: 0px;
  color: #fff;
}
</style>