const productMutations = {
    setProductList (state, payload) {
        state.product = payload.data
    },
    addProductList (state, payload) {
        state.product.push(payload.data)
    },
    setPopularProductList (state, payload) {
        state.popularProduct = payload.data
    },
    addPopularProductList (state, payload) {
        state.popularProduct.push(payload.data)
    },
    setProductByCategoryList (state, payload) {
        state.productByCategory = payload.data
    },
    addProductByCategoryList (state, payload) {
        state.productByCategory.push(payload.data)
    },

}

export default productMutations
