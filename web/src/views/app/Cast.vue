<template>
    <b-container
        id="cast_wrap"
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
    name: 'CastItem',
    data: () => ({
    }),
    components: {
        Header,
        Sidebar,
    }
}
</script>

<style lang="scss" scoped>
    #cast_wrap {
        height: $home-height;
        .content_wrap {

            background-color: $theme-color2;

            min-height: calc( #{$content-height} - #{$header-height} );

            display: flex;
            display: -webkit-flex;

            .content {
                width: $content-width;
                height: $content-height;
            }
        }
    }
</style>
