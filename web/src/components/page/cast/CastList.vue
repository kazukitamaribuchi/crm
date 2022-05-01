<template>
    <div>castList</div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
    name: 'CastListItem',
    data: () => ({
    }),
    created () {
        this.getCastList()
    },
    methods: {
        ...mapActions([
            'getCastList',
        ])
    }
}
</script>
