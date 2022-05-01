<template>
    <div>salesList</div>
</template>

<script>
import { mapGetters, mapMutations, mapActions } from 'vuex'

export default {
    name: 'SalesListItem',
    data: () => ({
    }),
    computed: {
        ...mapGetters([
            'sales'
        ]),
    },
    created () {
        this.getSalesList()
        .then(res => {
            this.setSalesList(res)
        })
    },
    mounted () {
        console.log('this.sales', this.sales)
    },
    methods: {
        ...mapMutations([
            'setSalesList',
        ]),
        ...mapActions([
            'getSalesList',
        ])
    }
}
</script>
