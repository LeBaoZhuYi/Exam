import Vue from 'vue'
import Router from 'vue-router'
import Exam from '@/components/Exam'
import ExamList from '@/components/ExamList'
import HistoryList from '@/components/HistoryList'
import Login from '@/components/Login'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'login',
      component: Login
    },
    {
      path: '/exam',
      name: 'exam',
      component: Exam
    },
    {
      path: '/examList',
      name: 'examList',
      component: ExamList
    },
    {
      path: '/historyList',
      name: 'historyList',
      component: HistoryList
    }
  ]
})
