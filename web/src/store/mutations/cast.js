const castMutations = {
    setCastList (state, payload) {
        state.cast = payload.data
    },
    setCastTopActive (state, payload) {
        state.castTopActive = payload
    }
}

export default castMutations
