import Vue from 'vue'

const salesActions = {
    getSalesList (ctx, kwargs) {
        console.log('getSalesList')
        return new Promise((resolve, reject) => {
            Vue.prototype.$axios({
                method: 'GET',
                url: '/api/sales/',
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

export default salesActions
