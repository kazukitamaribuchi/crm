import Vue from 'vue'

const customerActions = {
    getCustomerList (ctx, kwargs) {
        console.log('getCustomerList')
        return new Promise((resolve, reject) => {
            Vue.prototype.$axios({
                method: 'GET',
                url: '/api/customer/',
            })
            .then(res => {
                console.log(res)
                resolve(res)
            })
            .catch(e => {
                console.log(e)
                reject(e)
            })
        })
    }
}

export default customerActions
