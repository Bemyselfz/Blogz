<template>
  <div id="HelloWorld">
    <el-container>
      <el-container>
        <el-header>
            <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect">
                <el-menu-item index="1">首页</el-menu-item>
                <el-menu-item index="2">处理中心</el-menu-item>
                <el-menu-item index="3">处理中心</el-menu-item>
                <el-menu-item index="4">处理中心</el-menu-item>
              </el-menu>
        </el-header>
        <el-main>
            
            <el-table
            :data="postList"
            style="width: 100%"
            :default-sort = "{prop: 'date', order: 'descending'}"
            >
            <el-table-column
              prop="title"
              label="标题"
              sortable
              width="180">
            </el-table-column>
            <el-table-column
              prop="owner"
              label="作者"
              sortable
              width="180">
            </el-table-column>
            <el-table-column
              prop="category"
              label="分类"
              sortable
              width="180">
            </el-table-column>
            <el-table-column
              prop="tags"
              label="标签"
              sortable
              width="180">
            </el-table-column>
            <el-table-column
              prop="address"
              label="地址"
              >
            </el-table-column>
          </el-table>
        </el-main>
        <el-aside width="200px">Aside</el-aside>
        <el-footer>Footer</el-footer>
      </el-container>
    </el-container>
  </div>
</template>
 
<script>
  export default {
      mounted () {

  },
  props:['postList'],
    data() {
      return {
        activeIndex: '1',
        activeIndex2: '1'
      }
    },
     methods: {
        handleSelect(key, keyPath) {
        console.log(key, keyPath);
      }
    }

  }
</script>
 
<style>
.el-row {
    margin-bottom: 30px;
    &:last-child {
      margin-bottom: 0;
    }
  }
  .el-col {
    border-radius: 10px;
  }
  .bg-purple-dark {
    background: #99a9bf;
  }
  .bg-purple {
    background: #d3dce6;
  }
  .bg-purple-light {
    background: #e5e9f2;
  }
  .grid-content {
    border-radius: 4px;
    min-height: 36px;
  }
  .row-bg {
    padding: 10px 0;
    background-color: #f9fafc;
  }
</style>
