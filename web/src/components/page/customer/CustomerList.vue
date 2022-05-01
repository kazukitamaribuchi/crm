<template>
    <div>customerList</div>
</template>

<script>
import { mapGetters, mapMutations, mapActions } from 'vuex'

export default {
    name: 'CustomerListItem',
    data: () => ({
    }),
    computed: {
        ...mapGetters([
            'customer'
        ]),
    },
    created () {
        this.getCustomerList()
        .then(res => {
            this.setCustomerList(res)
        })
    },
    mounted () {
        console.log('this.customer', this.customer)
    },
    methods: {
        ...mapMutations([
            'setCustomerList',
        ]),
        ...mapActions([
            'getCustomerList',
        ])
    }
}
</script>
