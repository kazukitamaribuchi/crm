<template>
    <v-dialog
        v-model="dialog"
        max-width="300px"
    >
        <v-card>
            <v-card-subtitle>
                ログアウトしますか？
            </v-card-subtitle>
            <v-card-actions>
                <vs-button
                    color="primary"
                    type="filled"
                    icon="done"
                    @click="logout"
                >はい</vs-button>
                <vs-button
                    color="primary"
                    type="border"
                    icon="done"
                    @click="close"
                >いいえ</vs-button>
            </v-card-actions>
        </v-card>
    </v-dialog>
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
