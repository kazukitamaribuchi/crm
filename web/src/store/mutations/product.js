const productMutations = {
    setProductList (state, payload) {
        state.product = payload.data
    },
    addProductList (state, payload) {
        state.product.push(payload.data)
    }
}

export default productMutations
