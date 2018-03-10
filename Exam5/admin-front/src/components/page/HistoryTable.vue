<template>
    <div class="table">
        <div class="crumbs">
            <el-breadcrumb separator="/">
                <el-breadcrumb-item><i class="el-icon-menu"></i> 表格</el-breadcrumb-item>
                <el-breadcrumb-item>考试记录列表</el-breadcrumb-item>
            </el-breadcrumb>
        </div>
        <div class="handle-box">
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
                                   @click="handleFinish(scope.$index, scope.row)">简答题批阅
                        </el-button>
                        <el-button size="small" type="info"
                                   @click="showScore(scope.$index, scope.row)">查看作答
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
            <el-dialog title="考试详情" :visible.sync="dialogFormVisible2">
                <el-form :model="selectTable2">
                    <el-form-item label="单选题回答" label-width="100px">
                        <el-input :disabled="true"
                                  type="textarea"
                                  autosize v-model="selectTable2.questionAanswer" auto-complete="off"></el-input>
                    </el-form-item>
                    <el-form-item label="单选题答案" label-width="100px">
                        <el-input :disabled="true"
                                  type="textarea"
                                  autosize v-model="selectTable2.questionAright" auto-complete="off"></el-input>
                    </el-form-item>
                    <el-form-item label="单选题得分" label-width="100px">
                        <el-input :disabled="true" v-model="selectTable2.questionAscore" auto-complete="off"></el-input>
                    </el-form-item>
                    <el-form-item label="多选题回答" label-width="100px">
                        <el-input :disabled="true"
                                  type="textarea"
                                  autosize v-model="selectTable2.questionBanswer" auto-complete="off"></el-input>
                    </el-form-item>
                    <el-form-item label="多选题答案" label-width="100px">
                        <el-input :disabled="true"
                                  type="textarea"
                                  autosize v-model="selectTable2.questionBright" auto-complete="off"></el-input>
                    </el-form-item>
                    <el-form-item label="多选题得分" label-width="100px">
                        <el-input :disabled="true" v-model="selectTable2.questionBscore" auto-complete="off"></el-input>
                    </el-form-item>
                    <el-form-item label="填空题回答" label-width="100px">
                        <el-input :disabled="true"
                                  type="textarea"
                                  autosize v-model="selectTable2.questionCanswer" auto-complete="off"></el-input>
                    </el-form-item>
                    <el-form-item label="填空题答案" label-width="100px">
                        <el-input :disabled="true"
                                  type="textarea"
                                  autosize v-model="selectTable2.questionCright" auto-complete="off"></el-input>
                    </el-form-item>
                    <el-form-item label="填空题得分" label-width="100px">
                        <el-input :disabled="true" v-model="selectTable2.questionCscore" auto-complete="off"></el-input>
                    </el-form-item>
                    <el-form-item label="判断题回答" label-width="100px">
                        <el-input :disabled="true"
                                  type="textarea"
                                  autosize v-model="selectTable2.questionDanswer" auto-complete="off"></el-input>
                    </el-form-item>
                    <el-form-item label="判断题答案" label-width="100px">
                        <el-input :disabled="true"
                                  type="textarea"
                                  autosize v-model="selectTable2.questionDright" auto-complete="off"></el-input>
                    </el-form-item>
                    <el-form-item label="判断题得分" label-width="100px">
                        <el-input :disabled="true" v-model="selectTable2.questionDscore" auto-complete="off"></el-input>
                    </el-form-item>
                    <el-form-item label="简答题回答" label-width="100px">
                        <el-input :disabled="true"
                                  type="textarea"
                                  autosize v-model="selectTable2.questionEanswer" auto-complete="off"></el-input>
                    </el-form-item>
                    <el-form-item label="简答题得分" label-width="100px">
                        <el-input :disabled="true" v-model="selectTable2.questionEscore" auto-complete="off"></el-input>
                    </el-form-item>
                </el-form>
                <div slot="footer" class="dialog-footer">
                    <el-button @click="dialogFormVisible2 = false">关 闭</el-button>
                </div>
            </el-dialog>
            <el-dialog title="批卷" :visible.sync="dialogFormVisible">
                <el-form :model="selectTable">
                    <el-form-item label="编号" label-width="100px">
                        <el-input v-model="selectTable.id" auto-complete="off"></el-input>
                    </el-form-item>
                    <el-form-item label="学生名" label-width="100px">
                        <el-input v-model="selectTable.studyName" auto-complete="off"></el-input>
                    </el-form-item>
                    <el-form-item :label="'简答题'+index" v-for="(questionE, index) in selectTable.questionEinfoList"
                                  label-width="100px">
                        <el-input :disabled="true" v-model="questionE.title" auto-complete="off"></el-input>
                        <el-input :disabled="true" v-model="questionE.answer" auto-complete="off"></el-input>
                        <el-input v-model="questionE.score" auto-complete="off"></el-input>
                    </el-form-item>
                </el-form>
                <div slot="footer" class="dialog-footer">
                    <el-button @click="dialogFormVisible = false">取 消</el-button>
                    <el-button type="primary" @click="readOverUrl()">确 定</el-button>
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
                historyListUrl: '/api/historyList',
                readOverUrl: '/api/readOver',
                total: 0,
                currentPage: 1,
                dialogFormVisible: false,
                dialogFormVisible2: false,
                selectTable: {},
                selectTable2: {},
                pageSize: 5,
                select_word: '',
                is_search: false,
                tableData: [],
                allData: [],
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
                let token = this.getCookie('examAdminToken');
                this.$http.get(this.historyListUrl, {params: {token:token}}).then((response) => {
                    if (response.data.status == 0) {
                        self.allData = response.data.data;
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
            },
            showScore(index, row) {
                this.dialogFormVisible2 = true;
                this.selectTable2 = row;
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
