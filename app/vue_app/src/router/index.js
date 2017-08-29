import Vue from 'vue'
import Router from 'vue-router'
import Board from '@/components/Board'
import Login from '@/components/Login'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Login',
      component: Login
    }
  ]
})
