import Vue from 'vue'

const castActions = {
    getCastList (ctx, kwargs) {
        return new Promise((resolve, reject) => {
            Vue.prototype.$axios({
                method: 'GET',
                url: '/api/cast/',
            })
            .then(res => {
                console.log('getCastList', res)
                resolve(res)
            })
            .catch(e => {
                console.log(e)
                reject(e)
            })
        })
    }
}

export default castActions
