const customerMutations = {
    setCustomerList (state, payload) {
        state.customer = payload.data
    }
}

export default customerMutations
