<template>
  <div>
    <el-header>
      <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal">
        <el-menu-item index="1" @click="open('/examList');">考试列表</el-menu-item>
        <el-menu-item index="2" @click="open('/historyList');">成绩表</el-menu-item>
      </el-menu>
    </el-header>
    <el-main>
    <div class="table">
      <div class="crumbs">
        <el-breadcrumb separator="/">
          <el-breadcrumb-item><i class="el-icon-menu"></i> 表格</el-breadcrumb-item>
          <el-breadcrumb-item>考试安排列表</el-breadcrumb-item>
        </el-breadcrumb>
      </div>
      <div class="handle-box">
        <el-input v-model="select_word" placeholder="筛选关键词" class="handle-input mr10"></el-input>
        <el-button type="primary" icon="search">搜索</el-button>
      </div>
      <el-table :data="data" border style="width: 100%">
        <el-table-column prop="id" label="序号" sortable width="150">
        </el-table-column>
        <el-table-column prop="title" label="考试名" width="120">
        </el-table-column>
        <el-table-column prop="degree" label="难度" width="120">
        </el-table-column>
        <el-table-column prop="ctime" label="发布时间" width="240">
        </el-table-column>
        <el-table-column prop="endTime" label="开始时间">
        </el-table-column>
        <el-table-column prop="startTime" label="结束时间">
        </el-table-column>
        <el-table-column label="操作" width="180">
          <template scope="scope">
            <el-button size="small"
                       @click="start(scope.$index, scope.row)">开始考试
            </el-button>
          </template>
        </el-table-column>
      </el-table>
      <div class="pagination">
        <el-pagination
          @size-change="handleSizeChange"
          @current-change="handleCurrentChange"
          :current-page="currentPage"
          :page-sizes="[5, 10, 20]"
          :page-size="5"
          layout="sizes, prev, pager, next"
          :total="total">
        </el-pagination>
      </div>
    </div>
    </el-main>
  </div>
</template>
<script>
  export default {
    data() {
      return {
        url: '/api/examList',
        activeIndex: '1',
        total: 0,
        currentPage: 1,
        pageSize: 5,
        select_word: '',
        tableData: [],
        allData: [{
          id: '1',
          title: '好滋好味鸡蛋仔',
          degree: '困难',
          ctime: (new Date()).toDateString(),
          startTime: (new Date()).toDateString(),
          endTime: (new Date()).toDateString()
        }, {
          id: '1',
          title: '好滋好味鸡蛋仔',
          degree: '困难',
          ctime: (new Date()).toDateString(),
          startTime: (new Date()).toDateString(),
          endTime: (new Date()).toDateString()
        }, {
          id: '1',
          title: '好滋好味鸡蛋仔',
          degree: '困难',
          ctime: (new Date()).toDateString(),
          startTime: (new Date()).toDateString(),
          endTime: (new Date()).toDateString()
        }, {
          id: '1',
          title: '好滋好味鸡蛋仔',
          degree: '困难',
          ctime: (new Date()).toDateString(),
          startTime: (new Date()).toDateString(),
          endTime: (new Date()).toDateString()
        }, {
          id: '1',
          title: '好滋好味鸡蛋仔',
          degree: '困难',
          ctime: (new Date()).toDateString(),
          startTime: (new Date()).toDateString(),
          endTime: (new Date()).toDateString()
        }, {
          id: '1',
          title: '好滋好味鸡蛋仔',
          degree: '困难',
          ctime: (new Date()).toDateString(),
          startTime: (new Date()).toDateString(),
          endTime: (new Date()).toDateString()
        }, {
          id: '1',
          title: '好滋好味鸡蛋仔',
          degree: '困难',
          ctime: (new Date()).toDateString(),
          startTime: (new Date()).toDateString(),
          endTime: (new Date()).toDateString()
        }]
      }
    },
    created() {
      // this.getData();
      this.tableData = this.allData;
      this.handleCurrentChange(1);
    },
    computed: {
      data() {
        const self = this;
        self.filtedTableData = self.allData.filter(function (d) {
          let flag = false;
          self.formatObjectData(d);
          Object.values(d).forEach(v => {
            if (v.indexOf(self.select_word) > -1) {
              flag = true;
              return;
            }
          });
          if (flag) {
            return d;
          }
        });
        self.total = self.filtedTableData.length;
        return self.computeTableData(self.filtedTableData);
      }
    },
    methods: {
      getData() {
        const self = this;
        this.$http.get(this.url).then((response) => {
          if (response.data.status == 0) {
            self.allData = response.data.data;
          } else if (response.data.status > 0) {
            self.$message.error('获取分组列表失败！' + response.data.msg);
          } else {
            self.$message.error('获取分组列表失败！请稍后再试或联系管理员');
          }
        })
      },
      handleCurrentChange(val) {
        this.currentPage = val;
      },
      handleSizeChange(val) {
        this.pageSize = val;
      },
      computeTableData(allData) {
        let page = this.currentPage;
        let pageSize = this.pageSize;
        return allData.slice(pageSize * (page - 1), pageSize * page);
      },
      open(url){
        window.location.href = url;
      },
      start(index, row) {
        let startTime = row.startTime;
        let endTime = row.endTime;
        let now = new Date();
        if (now < startTime){
          this.$alert("未到考试开始时间", "警告");
        } else if(now > endTime){
          this.$alert("考试已经结束", "警告");
        } else{
          let paperId = row.paperId;
          this.$route.push({path:'/exam',query:{paperId:paperId}});
        }
      }
    }
  }
</script>

<style scoped>
  .handle-box {
    margin-bottom: 20px;
  }

  .handle-input {
    width: 300px;
    display: inline-block;
  }
</style>
