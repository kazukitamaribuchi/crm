<template>
    <div>bottleList</div>
</template>

<script>
import { mapGetters, mapMutations, mapActions } from 'vuex'

export default {
    name: 'BottleListItem',
    data: () => ({
    }),
    computed: {
        ...mapGetters([
            'bottle'
        ]),
    },
    created () {
        this.getBottleList()
        .then(res => {
            this.setBottleList(res)
        })
    },
    mounted () {
        console.log('this.bottle', this.bottle)
    },
    methods: {
        ...mapMutations([
            'setBottleList',
        ]),
        ...mapActions([
            'getBottleList',
        ])
    }
}
</script>
