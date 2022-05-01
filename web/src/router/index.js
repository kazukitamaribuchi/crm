import Vue from 'vue'
import VueRouter from 'vue-router'
import pages from './pages'
import customer from './customer'
import cast from './cast'
import sales from './sales'
import attendance from './attendance'
import booking from './booking'
import bottle from './bottle'

Vue.use(VueRouter)

const routes = [
    ...pages,
    {...customer},
    {...cast},
    {...sales},
    {...attendance},
    {...bottle},
    {...booking},
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
	next()
})

export default router
