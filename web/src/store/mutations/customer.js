const customerMutations = {
    setCustomerList (state, payload) {
        state.customer = payload.data
    },
    addCustomerList (state, payload) {
        state.customer.push(payload.data)
    },
    setCustomerTopActive (state, payload) {
        state.customerTopActive = payload
    }
}

export default customerMutations
