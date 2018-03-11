<template>
    <div class="sidebar">
        <el-menu :default-active="onRoutes" class="el-menu-vertical-demo" theme="dark" unique-opened router>
            <template v-for="item in items">
                <template v-if="item.subs">
                    <el-submenu :index="item.index">
                        <template slot="title"><i :class="item.icon"></i>{{ item.title }}</template>
                        <el-menu-item v-for="(subItem,i) in item.subs" :key="i" :index="subItem.index">{{ subItem.title
                            }}
                        </el-menu-item>
                    </el-submenu>
                </template>
                <template v-else>
                    <el-menu-item :index="item.index">
                        <i :class="item.icon"></i>{{ item.title }}
                    </el-menu-item>
                </template>
            </template>
        </el-menu>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                items: [
                    {
                        icon: 'el-icon-menu',
                        index: '1',
                        title: '学生管理',
                        subs: [
                            {
                                index: 'student-table',
                                title: '学生列表'
                            },
                            {
                                index: 'history-table',
                                title: '考试历史列表'
                            }
                        ]
                    },
                    {
                        icon: 'el-icon-bell',
                        index: '2',
                        title: '试题管理',
                        subs: [
                            {
                                index: 'question-table',
                                title: '题目列表'
                            },
                            {
                                index: 'paper-table',
                                title: '试卷列表'
                            },
                            {
                                index: 'exam-table',
                                title: '考试列表'
                            }
                        ]
                    },
                    {
                        icon: 'el-icon-date',
                        index: '3',
                        title: '管理操作',
                        subs: [
                            {
                                index: 'add-student',
                                title: '添加学生'
                            },
                            {
                                index: 'add-paper',
                                title: '添加试卷'
                            },
                            {
                                index: 'add-exam',
                                title: '添加考试'
                            },
                            {
                                index: 'add-a-question',
                                title: '添加单选题'
                            },
                            {
                                index: 'add-b-question',
                                title: '添加多选题'
                            },
                            {
                                index: 'add-c-question',
                                title: '添加填空题'
                            },
                            {
                                index: 'add-d-question',
                                title: '添加判断题'
                            },
                            {
                                index: 'add-e-question',
                                title: '添加简答题'
                            }
                        ]
                    }
                ]
            }
        },
        computed: {
            onRoutes() {
                // return this.$route.path.replace('/','');
            }
        }
    }
</script>

<style scoped>
    .sidebar {
        display: block;
        position: absolute;
        width: 250px;
        left: 0;
        top: 70px;
        bottom: 0;
        background: #2E363F;
    }

    .sidebar > ul {
        height: 100%;
    }
</style>
