import Vue from 'vue'
import Vuex from 'vuex'
import VuexPersistedstate from 'vuex-persistedstate'

Vue.use(Vuex)

const initialState = {
    isAuth: false,
    token: '',
    loginUser: '',
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
