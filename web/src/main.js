import Vue from 'vue'
import App from '@/App.vue'
import router from '@/router'
import vuetify from '@/plugins/vuetify'
import store from '@/store'
import http from '@/plugins/http'
import VueSession from 'vue-session'
import { BootstrapVue, BootstrapVueIcons } from 'bootstrap-vue'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import 'bootstrap-vue/dist/bootstrap-vue-icons.min.css'
require('@/assets/scss/main.scss')

Vue.prototype.$store = store
Vue.config.productionTip = false

Vue.use(http)
Vue.use(BootstrapVue)
Vue.use(BootstrapVueIcons)

Vue.use(VueSession)

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#main')
