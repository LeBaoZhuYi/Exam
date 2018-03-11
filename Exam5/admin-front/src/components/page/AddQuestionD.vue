<template>
    <div>
        <div class="crumbs">
            <el-breadcrumb separator="/">
                <el-breadcrumb-item><i class="el-icon-date"></i> 添加</el-breadcrumb-item>
                <el-breadcrumb-item>添加判断</el-breadcrumb-item>
            </el-breadcrumb>
        </div>
        <div class="form-box">
            <el-form ref="form" :model="form" label-width="80px">
                <el-form-item label="题目">
                    <el-input v-model="form.title"></el-input>
                </el-form-item>
                <el-form-item label="答案">
                    <el-radio-group v-model="form.answer">
                        <el-radio label="是" value="1"></el-radio>
                        <el-radio label="否" value="0"></el-radio>
                    </el-radio-group>
                </el-form-item>
                <el-form-item label="难度">
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
                    optionA: "",
                    optionB: "",
                    optionC: "",
                    optionD: "",
                    answer: "",
                    degree: ""
                },
                url: '/api/addQuestionD'
            }
        },
        methods: {
            onSubmit() {
                this.$http.post(this.url, this.form).then((response) => {
                    if(response.data.status == 0){
                        this.$message.success("提交成功");
                        window.location.href = "/admin/question-table";
                    } else if(response.data.status > 0){
                        this.$message.warning("提交失败！" + response.data.msg);
                    } else{
                        this.$message.error("提交失败！请稍后重试或咨询管理员");
                    }
                });
            }
        }
    }
</script>
