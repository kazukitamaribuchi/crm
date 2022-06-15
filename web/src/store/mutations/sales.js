import Vue from 'vue'

const salesMutations = {
    setSalesList (state, payload) {
        state.sales = payload.data
    },
    addSalesList (state, payload) {
        state.sales.push(payload.data)
    },
    updateSalesList (state, payload) {
        const index = state.sales.findIndex(s => s.id === payload.id)
        Vue.set(state.sales, index, payload)
    },
    deleteSalesList (state, payload) {
        if (state.sales != undefined) {
            const index = state.sales.findIndex(s => s.id === payload.id)
            if (index !== -1) state.sales = state.sales.filter((_, i) => i !== index)
        }
    },
    setSalesTopActive (state, payload) {
        state.salesTopActive = payload
    }
}

export default salesMutations
