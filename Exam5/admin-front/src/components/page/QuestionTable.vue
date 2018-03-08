<template>
    <div class="table">
        <div class="crumbs">
            <el-breadcrumb separator="/">
                <el-breadcrumb-item><i class="el-icon-menu"></i> 表格</el-breadcrumb-item>
                <el-breadcrumb-item>题目列表</el-breadcrumb-item>
            </el-breadcrumb>
        </div>
        <div class="handle-box">
            <el-select v-model="select_cate" placeholder="筛选题型" class="handle-select mr10">
                <el-option label="全部" value=""></el-option>
                <el-option label="单选题" value="单选题"></el-option>
                <el-option label="多选题" value="多选题"></el-option>
                <el-option label="填空题" value="填空题"></el-option>
                <el-option label="判断题" value="判断题"></el-option>
                <el-option label="简答题" value="简答题"></el-option>
            </el-select>
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
                            <el-form-item label="题目">
                                <span>{{ props.row.questionTitle }}</span>
                            </el-form-item>
                            <el-form-item label="题目类型">
                                <span>{{ props.row.questionType }}</span>
                            </el-form-item>
                            <el-form-item label="难易程度">
                                <span>{{ props.row.questionDegree }}</span>
                            </el-form-item>
                            <el-form-item label="答案">
                                <span>{{ props.row.answer }}</span>
                            </el-form-item>
                            <el-form-item label="创建时间">
                                <span>{{ props.row.ctime }}</span>
                            </el-form-item>
                        </el-form>
                    </template>
                </el-table-column>
                <el-table-column prop="id" label="编号" sortable width="120">
                </el-table-column>
                <el-table-column prop="questionTitle" label="题目" sortable width="120">
                </el-table-column>
                <el-table-column prop="questionType" label="题目类型" width="120">
                </el-table-column>
                <el-table-column prop="questionDegree" label="难易程度" width="120">
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
//        url: '/api/admin/student/getList',
                total: 0,
                currentPage: 1,
                pageSize: 5,
                select_cate: '',
                select_word: '',
                is_search: false,
                tableData: [],
                allData: [{
                    id: 1,
                    questionTitle: 2,
                    questionType: "123",
                    questionDegree: "456",
                    answer: "456",
                    ctime: new Date()
                }, {
                    id: 1,
                    questionTitle: 2,
                    questionType: "123",
                    questionDegree: "456",
                    answer: "456",
                    ctime: new Date()
                }, {
                    id: 1,
                    questionTitle: 2,
                    questionType: "123",
                    questionDegree: "456",
                    answer: "456",
                    ctime: new Date()
                }, {
                    id: 1,
                    questionTitle: 2,
                    questionType: "123",
                    questionDegree: "456",
                    answer: "456",
                    ctime: new Date()
                }]
            }
        },
        created() {
//      this.getData();
            this.tableData = this.allData;
            this.handleCurrentChange(1);
        },
        computed: {
            data() {
                const self = this;
                self.filtedTableData = self.allData.filter(function (d) {
                    let flag = false;
                    self.formatObjectData(d);
                    if (d.questionType.indexOf(self.select_cate) > -1) {
                        Object.values(d).forEach(v => {
                            if (v.indexOf(self.select_word) > -1) {
                                flag = true;
                                return;
                            }
                        });
                    }
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
                        let groupMap = new Map();
                        self.allData.forEach(function (value, key, arr) {
                            if (!groupMap.has(value.groupId)) {
                                groupMap.set(value.groupId,
                                    {
                                        groupId: value.groupId,
                                        groupName: value.groupName
                                    })
                            }
                        });
                    } else if (response.data.status > 0) {
                        self.$message.error('获取分组列表失败！' + response.data.msg);
                    } else {
                        self.$message.error('获取分组列表失败！请稍后再试或联系管理员');
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
