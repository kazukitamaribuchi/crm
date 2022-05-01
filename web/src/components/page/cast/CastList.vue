<template>
    <div>castList</div>
</template>

<script>
import { mapGetters, mapMutations, mapActions } from 'vuex'

export default {
    name: 'CastListItem',
    data: () => ({
    }),
    computed: {
        ...mapGetters([
            'cast'
        ]),
    },
    created () {
        this.getCastList()
        .then(res => {
            this.setCastList(res)
        })
    },
    mounted () {
        console.log('this.cast', this.cast)
    },
    methods: {
        ...mapMutations([
            'setCastList',
        ]),
        ...mapActions([
            'getCastList',
        ])
    }
}
</script>
