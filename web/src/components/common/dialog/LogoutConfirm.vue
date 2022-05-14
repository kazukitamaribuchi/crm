<template>
    <b-modal
        v-model="dialog"
        hide-header
        @ok="logout"
    >
        ログアウトしますか？
    </b-modal>
</template>

<script>
import { mapMutations } from 'vuex'

export default {
    name: 'LogoutConfirmItem',
    props: {
    },
    data: () => ({
        dialog: false,
    }),
    computed: {
    },
    methods: {
        ...mapMutations([
            'initAuthToken',
        ]),
        open () {
            this.dialog = true
        },
        close () {
            this.dialog = false
        },
        logout () {
            this.initAuthToken()
            this.dialog = false
            this.$router.push('/')
        }
    }
}

</script>

<style lang="scss" scoped>
</style>
