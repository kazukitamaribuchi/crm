import Vue from 'vue'
import Vuex from 'vuex'
import VuexPersistedstate from 'vuex-persistedstate'

import customerMutations from './mutations/customer'
import castMutations from './mutations/cast'
import questionMutations from './mutations/question'
import bottleMutations from './mutations/bottle'
import bookingMutations from './mutations/booking'
import salesMutations from './mutations/sales'
import attendanceMutations from './mutations/attendance'
import productMutations from './mutations/product'

import customerActions from './actions/customer'
import castActions from './actions/cast'
import questionActions from './actions/question'
import bottleActions from './actions/bottle'
import bookingActions from './actions/booking'
import salesActions from './actions/sales'
import attendanceActions from './actions/attendance'
import productActions from './actions/product'

Vue.use(Vuex)

const initialState = {
    isAuth: false,
    token: '',
    loginUser: '',
    currentTime: '',
    customer: [],
    customerTopActive: 0,
    sales: [],
    salesTopActive: 0,
    attendance: [],
    cast: [],
    castTopActive: 0,
    question: [],
    booking: [],
    bottle: [],
    product: [],
    popularProduct: [],
    productByCategory: [],
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
        currentTime: state => state.currentTime,
        customer: state => state.customer,
        customerTopActive: state => state.customerTopActive,
        sales: state => state.sales,
        salesTopActive: state => state.salesTopActive,
        attendance: state => state.attendance,
        cast: state => state.cast,
        castTopActive: state => state.castTopActive,
        question: state => state.question,
        booking: state => state.booking,
        bottle: state => state.bottle,
        product: state => state.product,
        popularProduct: state => state.popularProduct,
        productByCategory: state => state.productByCategory,
    },
    mutations: {
        ...customerMutations,
        ...castMutations,
        ...questionMutations,
        ...bottleMutations,
        ...bookingMutations,
        ...salesMutations,
        ...attendanceMutations,
        ...productMutations,

        setAuthToken (state, payload) {
            state.isAuth = true
            state.token = payload.data.token
            state.loginUser = payload.requestData.username
        },
        initAuthToken (state, payload) {
            state.isAuth = false
            state.token = ''
            state.loginUser = ''
        },
        setCurrentTime (state, payload) {
            state.currentTime = payload
        }
    },
    actions: {
        ...customerActions,
        ...castActions,
        ...questionActions,
        ...bookingActions,
        ...bottleActions,
        ...salesActions,
        ...attendanceActions,
        ...productActions,

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
                    this.commit('initAuthToken')
                    reject(e)
                })
            })
        },
        getCurrentTime (ctx, kwargs) {
            return new Promise((resolve, reject) => {
                Vue.prototype.$axios({
                    method: 'GET',
                    url: '/api/time/get_current_time/',
                    data: kwargs
                })
                .then(res => {
                    this.commit('setCurrentTime', res.data.data)
                    resolve(res)
                })
                .catch(e => {
                    console.log(e)
                    reject(e)
                })
            })
        }
    },
    modules: {
    },
    plugins: [
        VuexPersistedstate({
            storage: window.localStorage
        })
    ]
})
