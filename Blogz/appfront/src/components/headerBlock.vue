<template>
    <div class="max-width"><h1 class="site-title">Blogz<span class="title-span">技术改变世界·阅读塑造人生</span></h1></div>
</template>

<script>
export default {
    data() {
      return {
        activeIndex: '1',
        activeIndex2: '1'
      };
    },
    methods: {
      handleSelect(key, keyPath) {
        console.log(key, keyPath);
      }
    }
    
}
</script>

<style>
  .max-width{
      height: 100px;
      width: 80%;
      margin: 0 auto;
      padding: 20px;
  }

.site-title {
    height: 70px;
    display: block;
    float: left;
    margin: 10px auto;
    font-family: San Francisco UI;
    font-size: 50px;
    line-height: 70px;
    color:#fff;
}

.title-span {
    font-size: 25px;
    margin-left: 10px; 
    font-family:'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
}
</style>