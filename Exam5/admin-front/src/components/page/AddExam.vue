<template>
    <div>
        <div class="crumbs">
            <el-breadcrumb separator="/">
                <el-breadcrumb-item><i class="el-icon-date"></i> 添加</el-breadcrumb-item>
                <el-breadcrumb-item>添加考试</el-breadcrumb-item>
            </el-breadcrumb>
        </div>
        <div class="form-box">
            <el-form ref="form" :model="form" label-width="80px">
                <el-form-item label="试卷编号">
                    <el-input v-model="form.paperId"></el-input>
                </el-form-item>
                <el-form-item label="考试名">
                    <el-input v-model="form.title"></el-input>
                </el-form-item>
                <el-form-item label="开始时间">
                    <el-col :span="11">
                        <el-date-picker type="date" placeholder="选择日期" v-model="form.startDate" style="width: 100%;"></el-date-picker>
                    </el-col>
                    <el-col class="line" :span="2">-</el-col>
                    <el-col :span="11">
                        <el-time-picker type="fixed-time" placeholder="选择时间" v-model="form.startTime" style="width: 100%;"></el-time-picker>
                    </el-col>
                </el-form-item>
                <el-form-item label="结束时间">
                    <el-col :span="11">
                        <el-date-picker type="date" placeholder="选择日期" v-model="form.endDate" style="width: 100%;"></el-date-picker>
                    </el-col>
                    <el-col class="line" :span="2">-</el-col>
                    <el-col :span="11">
                        <el-time-picker type="fixed-time" placeholder="选择时间" v-model="form.endTime" style="width: 100%;"></el-time-picker>
                    </el-col>
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
                    paperId: "",
                    examTitle: "",
                    startDate: "",
                    startTime: "",
                    endDate: "",
                    endTime: ""
                },
                url: '/api/addExam'
            }
        },
        methods: {
            onSubmit() {
                let startTime = this.form.startDate;
                let endTime = this.form.endDate;
                startTime.setHours(this.form.startTime.getHours());
                startTime.setMinutes(this.form.startTime.getMinutes());
                startTime.setSeconds(this.form.startTime.getSeconds());
                endTime.setHours(this.form.endTime.getHours());
                endTime.setMinutes(this.form.endTime.getMinutes());
                endTime.setSeconds(this.form.endTime.getSeconds());
                this.form.startTime = this.dateToString(startTime);
                this.form.endTime = this.dateToString(endTime);
                this.$http.post(this.url, this.form).then((response) => {
                    if(response.data.status == 0){
                        this.$message.success("提交成功");
                        window.location.href = "/admin/exam-table";
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
