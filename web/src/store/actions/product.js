import Vue from 'vue'

const productActions = {
    getProductList (ctx, kwargs) {
        return new Promise((resolve, reject) => {
            Vue.prototype.$axios({
                method: 'GET',
                url: '/api/product/',
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
    },
    getProductByCategory (ctx, kwargs) {
        return new Promise((resolve, reject) => {
            Vue.prototype.$axios({
                method: 'GET',
                url: '/api/product/get_product_by_category/',
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

export default productActions
