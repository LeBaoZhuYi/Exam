<template>
    <div>
        <div class="crumbs">
            <el-breadcrumb separator="/">
                <el-breadcrumb-item><i class="el-icon-date"></i> 添加</el-breadcrumb-item>
                <el-breadcrumb-item>添加试卷</el-breadcrumb-item>
            </el-breadcrumb>
        </div>
        <el-alert
            title="编号以英文逗号隔开"
            type="warning"
            close-text="知道了">
        </el-alert>
        <div class="form-box">
            <el-form ref="form" :model="form" label-width="180px">
                <el-form-item label="试卷名">
                    <el-input v-model="form.paperTitle"></el-input>
                </el-form-item>
                <el-form-item label="单选题编号">
                    <el-input v-model="form.questionAList"></el-input>
                </el-form-item>
                <el-form-item label="单选题每题分数">
                    <el-input v-model="form.questionAScore"></el-input>
                </el-form-item>
                <el-form-item label="多选题编号">
                    <el-input v-model="form.questionBList"></el-input>
                </el-form-item>
                <el-form-item label="多选题每题分数">
                    <el-input v-model="form.questionBScore"></el-input>
                </el-form-item>
                <el-form-item label="填空题编号">
                    <el-input v-model="form.questionCList"></el-input>
                </el-form-item>
                <el-form-item label="填空题每题分数">
                    <el-input v-model="form.questionCScore"></el-input>
                </el-form-item>
                <el-form-item label="判断题编号">
                    <el-input v-model="form.questionDList"></el-input>
                </el-form-item>
                <el-form-item label="判断题每题分数">
                    <el-input v-model="form.questionDScore"></el-input>
                </el-form-item>
                <el-form-item label="简单题编号">
                    <el-input v-model="form.questionEList"></el-input>
                </el-form-item>
                <el-form-item label="简答题每题分数">
                    <el-input v-model="form.questionEScore"></el-input>
                </el-form-item>
                <el-form-item label="当前总分">
                    <h1>{{allScore}}</h1>
                </el-form-item>
                <el-form-item>
                    <el-button type="primary" @click="onSubmit">提交</el-button>
                </el-form-item>
            </el-form>
        </div>

    </div>
</template>

<script>
    export default {
        data: function () {
            return {
                form: {
                    paperTitle: "",
                    questionAList: "1,2,3",
                    questionAScore: 0,
                    questionBList: "2",
                    questionBScore: 0,
                    questionCList: "",
                    questionCScore: 0,
                    questionDList: "",
                    questionDScore: 0,
                    questionEList: "",
                    questionEScore: 0
                }
            }
        },
        computed: {
            allScore: function() {
                let a= 1;
                let b = 2;
                return this.form.questionAList.split(",").length * this.form.questionAScore +
                    this.form.questionBList.split(",").length * this.form.questionBScore +
                    this.form.questionCList.split(",").length * this.form.questionCScore +
                    this.form.questionDList.split(",").length * this.form.questionDScore +
                    this.form.questionEList.split(",").length * this.form.questionEScore ;
            }
        },
        methods: {
            onSubmit() {
                this.$http.post(this.url, this.form).then((response) => {
                    if (response.data.status == 0) {
                        this.$message.success("提交成功");
                        window.location.href = "/admin/user-table";
                    } else if (response.data.status > 0) {
                        this.$message.warning("提交失败！" + response.data.msg);
                    } else {
                        this.$message.error("提交失败！请稍后重试或咨询管理员");
                    }
                });
            }
        }
    }
</script>
