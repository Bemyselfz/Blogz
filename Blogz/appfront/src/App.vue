<template>
  <div id="app">
    <el-main class="header">
      <headerBlock></headerBlock>
    </el-main>
    <el-main class="nav">
      <navBlock @postListChange="postListChange"
                @postListShow="postListShow"></navBlock>
    </el-main>
    <el-main class="main">
      <mainBlock ref="mainBlock"
                 :postList="postList"></mainBlock>
    </el-main>
    <el-footer class="footer">
      <footerBlock></footerBlock>
    </el-footer>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue';
import headerBlock from './components/headerBlock.vue';
import navBlock from './components/navBlock.vue';
import mainBlock from './components/mainBlock.vue';
import postBlock from './components/postBlock.vue';
import footerBlock from './components/footerBlock.vue';

import { request } from './network/request'

export default {
  name: 'App',
  data () {
    return {
      postList: '',
    }
  },

  created: function () {
    request({ url: "/post" })
      .then(res => {
        this.postList = res.data.results
      }).catch(err => {
        console.log(err)
      })

  },
  methods: {
    postListChange (value) {
      this.postList = value;
      this.$refs.mainBlock._data.postListShow = true;
      this.$refs.mainBlock._data.postDetailShow = false;
    },
    postListShow () {

    }
  },

  components: {
    HelloWorld,
    headerBlock,
    navBlock,
    mainBlock,
    footerBlock,
  }

}
</script>

<style scoped>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background-color: #ebeef5;
  margin-top: 0px;
  height: 100%;
}

.el-header {
  color: #333;
  text-align: center;
  line-height: 70px;
}

.el-footer {
  color: #333;
  text-align: center;
  line-height: 70px;
}

.el-aside {
  color: #333;
  text-align: center;
  line-height: 200px;
}

.el-main {
  color: #333;
  text-align: center;
  line-height: 160px;
  padding: 0px;
}

body > .el-container {
  margin-bottom: 40px;
}

.el-container:nth-child(5) .el-aside,
.el-container:nth-child(6) .el-aside {
  line-height: 260px;
}

.el-container:nth-child(7) .el-aside {
  line-height: 320px;
}

.header {
  height: 150px;
  margin: 0 auto;
  margin-top: 0;
  padding: 0 20px;
  background: #333;
}

.nav {
  height: 120px;
  width: 100%;
  margin: 0 auto;
  background: #333;
}

.main {
  margin-top: -50px;
  width: 100%;
  min-height: 800px;
}

.footer {
  width: 80%;
  margin: 0 auto;
}
</style>
