import Vue from 'vue'
import VueRouter from 'vue-router'
import pages from './pages'
import HomeView from '../views/HomeView.vue'

Vue.use(VueRouter)

const routes = [...pages]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
    next()
})

router.beforeResolve((to, from, next) => {
    next()
})

router.afterEach((to, from) => {
})

export default router
