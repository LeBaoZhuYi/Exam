<template>
    <div class="table">
        <div class="crumbs">
            <el-breadcrumb separator="/">
                <el-breadcrumb-item><i class="el-icon-menu"></i> 表格</el-breadcrumb-item>
                <el-breadcrumb-item>试卷列表</el-breadcrumb-item>
            </el-breadcrumb>
        </div>
        <div class="handle-box">
            <el-input v-model="select_word" placeholder="筛选关键词" class="handle-input mr10"></el-input>
            <el-button type="primary" icon="search" @click="search">搜索</el-button>
        </div>
        <div>
            <el-table :data="data" border style="width: 100%">
                <el-table-column type="expand">
                    <template slot-scope="props">
                        <el-form label-position="left" inline class="demo-table-expand">
                            <el-form-item label="编号">
                                <span>{{ props.row.id }}</span>
                            </el-form-item>
                            <el-form-item label="试卷名">
                                <span>{{ props.row.title }}</span>
                            </el-form-item>
                            <el-form-item label="试卷难度">
                                <span>{{ props.row.degree }}</span>
                            </el-form-item>
                            <el-form-item label="单选题号">
                                <span>{{ props.row.questionAlist }}</span>
                            </el-form-item>
                            <el-form-item label="多选题号">
                                <span>{{ props.row.questionBlist }}</span>
                            </el-form-item>
                            <el-form-item label="填空题号">
                                <span>{{ props.row.questionClist }}</span>
                            </el-form-item>
                            <el-form-item label="判断题号">
                                <span>{{ props.row.questionDlist }}</span>
                            </el-form-item>
                            <el-form-item label="简答题号">
                                <span>{{ props.row.questionElist }}</span>
                            </el-form-item>
                            <el-form-item label="创建时间">
                                <span>{{ props.row.ctime }}</span>
                            </el-form-item>
                        </el-form>
                    </template>
                </el-table-column>
                <el-table-column prop="id" label="编号" sortable width="120">
                </el-table-column>
                <el-table-column prop="title" label="试卷名" width="120">
                </el-table-column>
                <el-table-column prop="degree" label="试卷难度" width="120">
                </el-table-column>
                <el-table-column prop="ctime" label="创建时间">
                </el-table-column>
                <el-table-column label="操作" width="180">
                    <template scope="scope">
                        <el-button size="small" type="danger"
                                   @click="handleDelete(scope.$index, scope.row)">删除
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
    </div>
</template>

<script>
    import ElOption from "../../../node_modules/element-ui/packages/select/src/option.vue";

    export default {
        components: {ElOption},
        data() {
            return {
                url: '/api/paperList',
                total: 0,
                currentPage: 1,
                pageSize: 5,
                select_cate: '',
                select_word: '',
                is_search: false,
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
                self.filtedTableData = self.allData.filter(function (od) {
                    let flag = false;
                    let d = self.formatObjectData(od);
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
                        self.$message.error('获取试卷列表失败！' + response.data.msg);
                    } else {
                        self.$message.error('获取试卷列表失败！请稍后再试或联系管理员');
                    }
                })
            },
            search() {
                this.is_search = true;
            },
            handleDelete(index, row) {
                this.$message.error('删除第' + (index + 1) + '行');
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
            }
        }
    }
</script>

<style scoped>
    .handle-box {
        margin-bottom: 20px;
    }

    .handle-select {
        width: 120px;
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
