import Vue from 'vue'

const customerMutations = {
    setCustomerList (state, payload) {
        state.customer = payload.data
    },
    addCustomerList (state, payload) {
        state.customer.push(payload.data)
    },
    updateCustomerList (state, payload) {
        const index = state.customer.findIndex(c => c.id === payload.id)
        Vue.set(state.customer, index, payload)
    },
    deleteCustomerList (state, payload) {
        if (state.customer != undefined) {
            const index = state.customer.findIndex(s => s.id === payload.id)
            if (index !== -1) state.customer = state.customer.filter((_, i) => i !== index)
        }
    },
    setCustomerTopActive (state, payload) {
        state.customerTopActive = payload
    },
}

export default customerMutations
