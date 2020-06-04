<template>
  <div class="content">
    <div v-if="postListShow">
      <div v-for="post in postList"
           v-bind:key="post.id"
           class="post"
           @click="postDetail(post.id)">
        <article>
          <div class="post-container">
            <div class="post-header">
              <h2>{{ post.title }}</h2>
            </div>
            <div class="post-content">
              {{ post.desc }}
            </div>
            <div class="post-tags">
              分类：{{ post.category }}
            </div>
          </div>
        </article>
      </div>
    </div>
    <div v-if="postDetailShow"
         class="post">
      <article>
        <div class="post-container">
          <div class="post-header">
            <h2>{{ post.title }}</h2>
          </div>
          <div class="post-content"
               v-html="post.content">
          </div>
          <div class="post-tags">
            分类：{{ post.category }}
          </div>
        </div>
      </article>
    </div>
  </div>

</template>
<script>
import { request } from "../network/request";
export default {
  props: ['postList',],
  data () {
    return {
      postListShow: true,
      postDetailShow: false,
      post: {}
    }
  },
  methods: {
    handleSelect (key, keyPath) {
      // console.log(key, keyPath);
    },
    postDetail (postId) {
      console.log(postId)
      request({ url: "/post/" + postId })
        .then(res => {
          this.post = res.data
        }).catch(err => {
          console.log(err)
        });
      this.postListShow = false;
      this.postDetailShow = true;
    }
  }

}
</script>

<style>
.content {
  position: relative;
  left: 10%;
  width: 680px;
  background: #e4e7ed;
  box-sizing: border-box;
}

.post {
  width: 100%;
  margin-bottom: 20px;
  float: left;
  background: #fff;
  box-shadow: 5px 5px 5px #888888;
}

.content article {
  width: 100%;
  margin-bottom: 20px;
}

.post-container {
  width: 92%;
  margin: 30px auto;
}

.post-header {
  width: 100%;
  height: 50px;
}

.post-header h2 {
  width: 100%;
  display: block;
  font-size: 26px;
  line-height: 26px;
  text-align: left;
  float: left;
  margin: 0 auto;
}

.post-content {
  line-height: 24px;
  text-align: left;
  margin-bottom: 20px;
}

.post-tags {
  line-height: 24px;
  text-align: left;
}
</style>