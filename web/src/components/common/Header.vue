<template>
    <v-container fluid id="header_wrap">
        <!-- <vs-row>
            <vs-col vs-w="3">
                <h1 class="header_title">顧客管理システム（仮）</h1>
            </vs-col>
            <v-spacer/>
            <vs-col vs-w="3">
                menu
            </vs-col>
        </vs-row> -->

        <v-row class="pl-7 pt-5">
            <v-col cols="3">
                <router-link to='/'>顧客管理システム</router-link>
            </v-col>
            <v-spacer/>
            <v-col cols="2">
                <!-- これらはコンポーネント化する -->
                <v-btn
                    text
                >
                    設定
                </v-btn>
                <LogoutBtn/>
            </v-col>
        </v-row>

    </v-container>
</template>

<script>
import LogoutBtn from '@/components/common/LogoutBtn'

export default {
    name: 'HeaderItem',
    data: () => ({
        activeItem: {}
    }),
    components: {
        LogoutBtn,
    }
}
</script>

<style lang="scss" scoped>
#header_wrap {
    padding: 0;
    margin-bottom: 20px;

    .vs-navbar {
        padding: 14px 30px 10px 20px;
        box-shadow: none !important;
        -webkit-box-shadow: none !important;
    }

    .header_title {
        font-size: 24px;
        font-weight: 100;
        margin: 4px 0 5px 20px;
    }
}

</style>
