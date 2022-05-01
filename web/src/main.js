import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import http from '@/plugins/http'
import vuetify from '@/plugins/vuetify'
import Vuesax from 'vuesax'
import VueSession from 'vue-session'
import './registerServiceWorker'

import 'vuesax/dist/vuesax.css'
import 'boxicons/css/boxicons.min.css'

Vue.config.productionTip = false

Vue.use(http)
Vue.use(Vuesax, {
})

Vue.use(VueSession)

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
