const customerMutations = {
    setCustomerList (state, payload) {
        state.customer = payload.data
    },
    addCustomerList (state, payload) {
        state.customer.push(payload.data)
    },
}

export default customerMutations
