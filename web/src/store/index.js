import Vue from 'vue'
import Vuex from 'vuex'
import VuexPersistedstate from 'vuex-persistedstate'

import customerMutations from './mutations/customer'
import castMutations from './mutations/cast'
import bottleMutations from './mutations/bottle'
import bookingMutations from './mutations/booking'
import salesMutations from './mutations/sales'
import attendanceMutations from './mutations/attendance'
import productMutations from './mutations/product'

import customerActions from './actions/customer'
import castActions from './actions/cast'
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
    customer: [],
    sales: [],
    attendance: [],
    cast: [],
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
        customer: state => state.customer,
        sales: state => state.sales,
        attendance: state => state.attendance,
        cast: state => state.cast,
        booking: state => state.booking,
        bottle: state => state.bottle,
        product: state => state.product,
        popularProduct: state => state.popularProduct,
        productByCategory: state => state.productByCategory,
    },
    mutations: {
        ...customerMutations,
        ...castMutations,
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
        }
    },
    actions: {
        ...customerActions,
        ...castActions,
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
    },
    modules: {
    },
    plugins: [
        VuexPersistedstate({
            storage: window.localStorage
        })
    ]
})
