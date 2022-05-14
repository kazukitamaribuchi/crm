<template>
    <b-container
        id="customer_wrap"
        fluid
    >
        <Header/>
        <b-row class="content_wrap">
            <Sidebar/>
            <div class="content">
                <router-view/>
            </div>
        </b-row>
    </b-container>
</template>

<script>
import Header from '@/components/common/Header'
import Sidebar from '@/components/common/Sidebar'

export default {
    name: 'CustomerItem',
    data: () => ({
    }),
    components: {
        Header,
        Sidebar,
    }
}
</script>

<style lang="scss" scoped>
    #customer_wrap {
        height: $home-height;
        .content_wrap {

            background-color: $theme-color2;

            height: calc( #{$content-height} - #{$header-height} );

            display: flex;
            display: -webkit-flex;

            .content {
                width: $content-width;
                height: $content-height;
            }
        }
    }
</style>
