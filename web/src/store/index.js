import Vue from 'vue'
import Vuex from 'vuex'
import VuexPersistedstate from 'vuex-persistedstate'

import customerActions from './customer'
import castActions from './cast'
import bottleActions from './bottle'
import bookingActions from './booking'
import salesActions from './sales'
import attendanceActions from './attendance'

Vue.use(Vuex)

const initialState = {
    isAuth: false,
    token: '',
    loginUser: '',
    customer: [],
    sales: [],
    attendance: [],
    cast: [],
    booking: [],
    bottle: [],
}


export default new Vuex.Store({
    strict: true,
    state: {
        ...{},
        ...initialState
    },
    getters: {
        isAuth: state => state.isAuth,
        token: state => state.token,
        loginUser: state => state.loginUser,
        customer: state => state.customer,
        sales: state => state.sales,
        attendance: state => state.attendance,
        cast: state => state.cast,
        booking: state => state.booking,
        bottle: state => state.bottle,
    },
    mutations: {
        setAuthToken (state, payload) {
            state.isAuth = true
            state.token = payload.data.token
            state.loginUser = payload.requestData.username
        },
        initAuthToken (state, payload) {
            state.isAuth = false
            state.token = ''
            state.loginUser = ''
        }
    },
    actions: {
        ...customerActions,
        ...castActions,
        ...bookingActions,
        ...bottleActions,
        ...salesActions,
        ...attendanceActions,

        checkAuthToken (ctx, kwargs) {
            return new Promise((resolve, reject) => {
                Vue.prototype.$axios({
                    method: 'POST',
                    url: '/auth/',
                    data: kwargs
                })
                .then(res => {
                    console.log('認証結果', res)
                    this.commit('setAuthToken', res)
                    resolve(res)
                })
                .catch(e => {
                    console.log(e)
                    reject(e)
                })
            })
        },
    },
    modules: {
    },
    plugins: [
        VuexPersistedstate({
            storage: window.localStorage
        })
    ]
})
