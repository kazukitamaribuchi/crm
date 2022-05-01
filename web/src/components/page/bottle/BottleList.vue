<template>
    <div>bottleList</div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
    name: 'BottleListItem',
    data: () => ({
    }),
    created () {
        this.getBottleList()
    },
    methods: {
        ...mapActions([
            'getBottleList',
        ])
    }
}
</script>
