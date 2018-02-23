import Vue from 'vue'
import Router from 'vue-router'
import exam from '@/components/Exam'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'exam',
      component: exam
    }
  ]
})
