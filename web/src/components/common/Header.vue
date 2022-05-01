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


        <vs-navbar v-model="activeItem" class="nabarx">
            <div slot="title">
                <vs-navbar-title>
                    <router-link to='/'>顧客管理システム</router-link></vs-navbar-title>
            </div>
            <vs-navbar-item index="1">
                <a href="#">設定</a>
            </vs-navbar-item>
            <vs-navbar-item index="2">
                <a href="#">ログアウト</a>
            </vs-navbar-item>
        </vs-navbar>
    </v-container>
</template>

<script>
export default {
    name: 'HeaderItem',
    data: () => ({
        activeItem: {}
    })
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
