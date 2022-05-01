import Vue from 'vue'

const bottleActions = {
    getBottleList (ctx, kwargs) {
        console.log('getBottleList')
        return new Promise((resolve, reject) => {
            Vue.prototype.$axios({
                method: 'GET',
                url: '/api/bottle/',
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

export default bottleActions
