<template>
    <div>salesList</div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
    name: 'SalesListItem',
    data: () => ({
    }),
    created () {
        this.getSalesList()
    },
    methods: {
        ...mapActions([
            'getSalesList',
        ])
    }
}
</script>
