import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'

//安装插件
Vue.use(Router)

import headerBlock from '../components/headerBlock.vue';
import navBlock from '../components/navBlock.vue';
import mainBlock from '../components/mainBlock.vue';
import postBlock from '../components/postBlock.vue';
import footerBlock from '../components/footerBlock.vue';

//导出Router对象
export default new Router({
  //配置路由和组件之间的映射关系
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: 'post',
      component: postBlock
    }
  ]
})
