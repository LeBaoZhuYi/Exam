<template>
  <div>
    <div class="crumbs">
      <el-breadcrumb separator="/">
        <el-breadcrumb-item><i class="el-icon-date"></i> 添加</el-breadcrumb-item>
        <el-breadcrumb-item>添加学生</el-breadcrumb-item>
      </el-breadcrumb>
    </div>
    <div class="form-box">
      <el-form ref="form" :model="form" label-width="80px">
        <el-form-item label="登录名">
          <el-input v-model="form.loginName"></el-input>
        </el-form-item>
        <el-form-item label="密码">
          <el-input v-model="form.password"></el-input>
        </el-form-item>
        <el-form-item label="学生姓名">
          <el-input v-model="form.studyName"></el-input>
        </el-form-item>
        <el-form-item label="学生学号">
          <el-input v-model="form.studyId"></el-input>
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
          loginName: "",
          password: "",
            studyName: "",
            studyId: ""
        }
      }
    },
    methods: {
      onSubmit() {
        this.$http.post(this.url, this.form).then((response) => {
          if(response.data.status == 0){
            this.$message.success("提交成功");
            window.location.href = "/admin/user-table";
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
