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
          <el-breadcrumb-item>成绩表</el-breadcrumb-item>
        </el-breadcrumb>
      </div>
      <div class="handle-box">
        <el-input v-model="select_word" placeholder="筛选关键词" class="handle-input mr10"></el-input>
        <el-button type="primary" icon="search">搜索</el-button>
      </div>
      <el-table :data="data" border style="width: 100%">
        <el-table-column prop="id" label="序号" sortable width="150">
        </el-table-column>
        <el-table-column prop="examTitle" label="考试名" width="120">
        </el-table-column>
        <el-table-column prop="degree" label="难度" width="120">
        </el-table-column>
        <el-table-column prop="status" label="状态" width="240">
        </el-table-column>
        <el-table-column prop="score" label="得分" width="240">
        </el-table-column>
        <el-table-column prop="ctime" label="结卷时间">
        </el-table-column>
        <el-table-column label="操作" width="180">
          <template scope="scope">
            <el-button size="small"
                       @click="detail(scope.$index, scope.row)">查看详情
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
      <el-dialog title="考试详情" :visible.sync="dialogFormVisible">
        <el-form :model="selectTable">
          <el-form-item label="单选题回答" label-width="100px">
            <el-input :disabled="true"
                      type="textarea"
                      autosize v-model="selectTable.questionAanswer" auto-complete="off"></el-input>
          </el-form-item>
          <el-form-item label="单选题得分" label-width="100px">
            <el-input :disabled="true" v-model="selectTable.questionAscore" auto-complete="off"></el-input>
          </el-form-item>
          <el-form-item label="多选题回答" label-width="100px">
            <el-input :disabled="true"
                      type="textarea"
                      autosize v-model="selectTable.questionBanswer" auto-complete="off"></el-input>
          </el-form-item>
          <el-form-item label="多选题得分" label-width="100px">
            <el-input :disabled="true" v-model="selectTable.questionBscore" auto-complete="off"></el-input>
          </el-form-item>
          <el-form-item label="填空题回答" label-width="100px">
            <el-input :disabled="true"
                      type="textarea"
                      autosize v-model="selectTable.questionCanswer" auto-complete="off"></el-input>
          </el-form-item>
          <el-form-item label="填空题得分" label-width="100px">
            <el-input :disabled="true" v-model="selectTable.questionCscore" auto-complete="off"></el-input>
          </el-form-item>
          <el-form-item label="判断题回答" label-width="100px">
            <el-input :disabled="true"
                      type="textarea"
                      autosize v-model="selectTable.questionDanswer" auto-complete="off"></el-input>
          </el-form-item>
          <el-form-item label="判断题得分" label-width="100px">
            <el-input :disabled="true" v-model="selectTable.questionDscore" auto-complete="off"></el-input>
          </el-form-item>
          <el-form-item label="简答题回答" label-width="100px">
            <el-input :disabled="true"
                      type="textarea"
                      autosize v-model="selectTable.questionEanswer" auto-complete="off"></el-input>
          </el-form-item>
          <el-form-item label="简答题得分" label-width="100px">
            <el-input :disabled="true" v-model="selectTable.questionEscore" auto-complete="off"></el-input>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="dialogFormVisible = false">关 闭</el-button>
        </div>
      </el-dialog>
    </div>
    </el-main>
  </div>
</template>
<script>
  export default {
    data() {
      return {
        url: '/api/historyList',
        total: 0,
        activeIndex: '2',
        currentPage: 1,
        pageSize: 5,
        select_word: '',
        dialogFormVisible: false,
        selectTable: {},
        tableData: [],
        allData: []
      }
    },
    created() {
      this.getData();
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
          const self = this;
          let token = this.getCookie('examToken');
          this.$http.get(this.url, {params: {token:token}}).then((response) => {
            if (response.data.status == 0) {
              self.allData = response.data.data;
            } else if (response.data.status > 0) {
              self.$message.error('获取分组列表失败！' + response.data.msg);
            } else {
              self.$message.error('获取分组列表失败！请稍后再试或联系管理员');
            }
          })
        })
      },
      detail(index, row) {
        this.dialogFormVisible = true;
        this.selectTable = row;
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
  .demo-table-expand {
    font-size: 0;
  }

  .demo-table-expand label {
    width: 90px;
    color: #99a9bf;
  }

  .demo-table-expand .el-form-item {
    margin-right: 0;
    margin-bottom: 0;
    width: 50%;
  }
</style>
