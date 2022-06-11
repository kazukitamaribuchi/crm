const salesMutations = {
    setSalesList (state, payload) {
        state.sales = payload.data
    },
    setSalesTopActive (state, payload) {
        state.salesTopActive = payload
    }
}

export default salesMutations
