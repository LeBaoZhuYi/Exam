<template>
    <div class="table">
        <div class="crumbs">
            <el-breadcrumb separator="/">
                <el-breadcrumb-item><i class="el-icon-menu"></i> 表格</el-breadcrumb-item>
                <el-breadcrumb-item>考试记录列表</el-breadcrumb-item>
            </el-breadcrumb>
        </div>
        <div class="handle-box">
            <el-select v-model="select_cate" placeholder="筛选考试" class="handle-select mr10">
                <el-option label="全部" value=""></el-option>
                <el-option v-for="exam in examList" :label="exam.examTitle" :value="exam.examTitle"
                           :key="exam.id"></el-option>
            </el-select>
            <el-input v-model="select_word" placeholder="筛选关键词" class="handle-input mr10"></el-input>
            <el-button type="primary" icon="search" @click="search">搜索</el-button>
        </div>
        <div>
            <el-table :data="data" border style="width: 100%">
                <el-table-column prop="id" label="编号" sortable width="120">
                </el-table-column>
                <el-table-column prop="studyName" label="学生" width="120">
                </el-table-column>
                <el-table-column prop="examTitle" label="考试" width="120">
                </el-table-column>
                <el-table-column prop="score" label="成绩" width="120">
                </el-table-column>
                <el-table-column prop="status" label="状态" width="120">
                </el-table-column>
                <el-table-column prop="ctime" label="创建时间">
                </el-table-column>
                <el-table-column label="操作" width="180">
                    <template scope="scope">
                        <el-button size="small" type="danger"
                                   @click="handleFinish(scope.$index, scope.row)">简答题批卷
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

            <el-dialog title="批卷" :visible.sync="dialogFormVisible">
                <el-form :model="selectTable">
                    <el-form-item label="编号" label-width="100px">
                        <el-input v-model="selectTable.id" auto-complete="off"></el-input>
                    </el-form-item>
                    <el-form-item label="学生名" label-width="100px">
                        <el-input v-model="selectTable.studyName" auto-complete="off"></el-input>
                    </el-form-item>
                </el-form>
                <div slot="footer" class="dialog-footer">
                    <el-button @click="dialogFormVisible = false">取 消</el-button>
                    <el-button type="primary" @click="">确 定</el-button>
                </div>
            </el-dialog>
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
                dialogFormVisible: false,
                selectTable: {},
                pageSize: 5,
                select_cate: '',
                select_word: '',
                is_search: false,
                tableData: [],
                allData: [{
                    id: 1,
                    examTitle: 2,
                    studyName: "123",
                    score: "456",
                    status: "456",
                    ctime: new Date()
                }, {
                    id: 1,
                    examTitle: 2,
                    studyName: "123",
                    score: "456",
                    status: "456",
                    ctime: new Date()
                }, {
                    id: 1,
                    examTitle: 2,
                    studyName: "123",
                    score: "456",
                    status: "456",
                    ctime: new Date()
                }, {
                    id: 1,
                    examTitle: 2,
                    studyName: "123",
                    score: "456",
                    status: "456",
                    ctime: new Date()
                }],
                examList: []
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
                    self.formmatObjectData(d);
                    if (d.examTitle.indexOf(self.select_cate) > -1) {
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
            handleFinish(index, row) {
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
