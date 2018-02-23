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
                    path: '/admin/group-table',
                    component: resolve => require(['../components/page/GroupTable.vue'], resolve)
                },
                {
                    path: '/admin/history-table',
                    component: resolve => require(['../components/page/HistoryTable.vue'], resolve)
                },
                {
                    path: '/admin/video-table',
                    component: resolve => require(['../components/page/VideoTable.vue'], resolve)
                },
                {
                    path: '/admin/class-table',
                    component: resolve => require(['../components/page/ClassTable.vue'], resolve)
                },
                {
                    path: '/admin/add-video',
                    component: resolve => require(['../components/page/AddVideo.vue'], resolve)
                },
                {
                    path: '/admin/add-student',
                    component: resolve => require(['../components/page/AddStudent.vue'], resolve)
                },
                {
                    path: '/admin/add-class',
                    component: resolve => require(['../components/page/AddClass.vue'], resolve)
                },
                {
                    path: '/admin/add-group',
                    component: resolve => require(['../components/page/AddGroup.vue'], resolve)       // Vue-Core-Image-Upload组件
                }
            ]
        },
    ]
})
