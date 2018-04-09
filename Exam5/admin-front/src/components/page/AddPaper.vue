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
                    <el-input v-model="form.title"></el-input>
                </el-form-item>
                <el-form-item label="单选题编号">
                    <el-input v-model="form.questionAlist"></el-input>
                </el-form-item>
                <el-form-item label="单选题每题分数">
                    <el-input v-model="form.questionAscore"></el-input>
                </el-form-item>
                <el-form-item label="多选题编号">
                    <el-input v-model="form.questionBlist"></el-input>
                </el-form-item>
                <el-form-item label="多选题每题分数">
                    <el-input v-model="form.questionBscore"></el-input>
                </el-form-item>
                <el-form-item label="填空题编号">
                    <el-input v-model="form.questionClist"></el-input>
                </el-form-item>
                <el-form-item label="填空题每题分数">
                    <el-input v-model="form.questionCscore"></el-input>
                </el-form-item>
                <el-form-item label="判断题编号">
                    <el-input v-model="form.questionDlist"></el-input>
                </el-form-item>
                <el-form-item label="判断题每题分数">
                    <el-input v-model="form.questionDscore"></el-input>
                </el-form-item>
                <el-form-item label="简单题编号">
                    <el-input v-model="form.questionElist"></el-input>
                </el-form-item>
                <el-form-item label="简答题每题分数">
                    <el-input v-model="form.questionEscore"></el-input>
                </el-form-item>
                <el-form-item label="当前总分">
                    <h1>{{allScore}}</h1>
                </el-form-item><el-form-item label="难度">
                <el-radio-group v-model="form.degree">
                    <el-radio label="简单" value="1"></el-radio>
                    <el-radio label="普通" value="2"></el-radio>
                    <el-radio label="较难" value="3"></el-radio>
                </el-radio-group>
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
                    title: "",
                    questionAlist: "",
                    questionAscore: 0,
                    questionBlist: "",
                    questionBscore: 0,
                    questionClist: "",
                    questionCscore: 0,
                    questionDlist: "",
                    questionDscore: 0,
                    questionElist: "",
                    questionEscore: 0,
                    degree: ""
                },
                url: '/api/addPaper'
            }
        },
        computed: {
            allScore: function() {
                return this.form.questionAlist.split(",").length * this.form.questionAscore +
                    this.form.questionBlist.split(",").length * this.form.questionBscore +
                    this.form.questionClist.split(",").length * this.form.questionCscore +
                    this.form.questionDlist.split(",").length * this.form.questionDscore +
                    this.form.questionElist.split(",").length * this.form.questionEscore ;
            }
        },
        methods: {
            onSubmit() {
                this.$http.post(this.url, this.form).then((response) => {
                    if (response.data.status == 0) {
                        this.$message.success("提交成功");
                        window.location.href = "/admin/paper-table";
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
