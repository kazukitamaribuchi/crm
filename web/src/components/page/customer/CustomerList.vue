<template>
    <div>customerList</div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
    name: 'CustomerListItem',
    data: () => ({
    }),
    created () {
        this.getCustomerList()
    },
    methods: {
        ...mapActions([
            'getCustomerList',
        ])
    }
}
</script>
