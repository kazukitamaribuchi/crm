<template>
    <b-row id="header_wrap" class="pt-2">
        <b-col cols="6">
            <router-link
                to='/'
                class="header_title"
            >Customer Management System</router-link>
        </b-col>
        <b-col cols="6">
            <b-nav align="right">
                <Settings/>
                <Logout/>
            </b-nav>
        </b-col>
    </b-row>
</template>

<script>
import Logout from '@/components/common/Logout'
import Settings from '@/components/common/Settings'

export default {
    name: 'HeaderItem',
    data: () => ({
        activeItem: {}
    }),
    components: {
        Logout,
        Settings,
    }
}
</script>

<style lang="scss" scoped>
#header_wrap {
    height: $header-height;
    background-color: $theme-color;
    color: white;

    .header_title {
        padding-left: 1rem;
        color: $menu-text-color;
        text-decoration: none;
        // font-family: 'Anton', sans-serif;
        // font-family: 'Roboto Condensed', sans-serif;
        position: relative;
        top: 2px;
        font-weight: bold;
        font-size: 22px;
    }
}

</style>
