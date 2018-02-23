import Vue from 'vue';
import Router from 'vue-router';

Vue.use(Router);

export default new Router({
    mode: 'history',
    routes: [
        {
            path: '/',
            redirect: '/admin/login'
        },
        {
            path: '/admin/login',
            component: resolve => require(['../components/page/Login.vue'], resolve)
        },
        {
            path: '/admin',
            redirect: '/admin/index'
        },
        {
            path: '/admin',
            component: resolve => require(['../components/common/Home.vue'], resolve),
            children: [
                {
                    path: '/admin/index',
                    component: resolve => require(['../components/page/Readme.vue'], resolve)
                },
                {
                    path: '/admin/student-table',
                    component: resolve => require(['../components/page/StudentTable.vue'], resolve)
                },
                {
                    path: '/admin/history-table',
                    component: resolve => require(['../components/page/HistoryTable.vue'], resolve)
                },
                {
                    path: '/admin/question-table',
                    component: resolve => require(['../components/page/QuestionTable.vue'], resolve)
                },
                {
                    path: '/admin/paper-table',
                    component: resolve => require(['../components/page/PaperTable.vue'], resolve)
                },
                {
                    path: '/admin/exam-table',
                    component: resolve => require(['../components/page/ExamTable.vue'], resolve)
                },
                {
                    path: '/admin/add-student',
                    component: resolve => require(['../components/page/AddStudent.vue'], resolve)
                },
                {
                    path: '/admin/add-a-question',
                    component: resolve => require(['../components/page/AddQuestionA.vue'], resolve)
                },
                {
                    path: '/admin/add-b-question',
                    component: resolve => require(['../components/page/AddQuestionB.vue'], resolve)
                },
                {
                    path: '/admin/add-c-question',
                    component: resolve => require(['../components/page/AddQuestionC.vue'], resolve)
                },
                {
                    path: '/admin/add-d-question',
                    component: resolve => require(['../components/page/AddQuestionD.vue'], resolve)
                },
                {
                    path: '/admin/add-e-question',
                    component: resolve => require(['../components/page/AddQuestionE.vue'], resolve)
                },
                {
                    path: '/admin/add-paper',
                    component: resolve => require(['../components/page/AddPaper.vue'], resolve)
                },
                {
                    path: '/admin/add-exam',
                    component: resolve => require(['../components/page/AddExam.vue'], resolve)
                }
            ]
        },
    ]
})
