<template>
    <span>
        <v-btn
            text
            @click="showLogoutConfirm"
        >
            ログアウト
        </v-btn>

        <LogoutConfirm
            ref="logoutConfirm"
        />
    </span>
</template>

<script>
import LogoutConfirm from '@/components/common/dialog/LogoutConfirm'

export default {
    name: 'LogoutBtnItem',
    data: () => ({
    }),
    components: {
        LogoutConfirm,
    },
    methods: {
        showLogoutConfirm () {
            this.$refs.logoutConfirm.open()
        }
    }
}
</script>

<style lang="scss" scoped>

</style>
