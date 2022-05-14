<template>
    <b-container
        id="home_wrap"
        fluid
    >
        <Header/>
        <b-row class="content_wrap">
            <Sidebar/>
            <div class="content">
                <Top/>
            </div>
        </b-row>
    </b-container>
</template>

<script>
import Header from '@/components/common/Header'
import Sidebar from '@/components/common/Sidebar'
import Top from '@/components/page/Top'
import { mapGetters, mapMutations, mapActions } from 'vuex'

export default {
    name: 'HomeItem',
    components: {
        Header,
        Sidebar,
        Top
    },
    created () {
        // this.getProductList()
        // .then(res => {
        //     console.log(res)
        //     this.setProductList(res)
        // })
        // .catch(e => {
        //     console.log(e)
        // })

        // this.getProductByCategory()
        // .then(res => {
        //     console.log(res)
        //     this.setProductList(res)
        // })
        // .catch(e => {
        //     console.log(e)
        // })
    },
    computed: {
        ...mapGetters([
            'product',
        ]),
    },
    methods: {
        ...mapMutations([
            'setProductList',
        ]),
        ...mapActions([
            'getProductList',
            'getProductByCategory',
        ])
    }
}
</script>

<style lang="scss" scoped>
    #home_wrap {
        height: $home-height;
        .content_wrap {

            background-color: $theme-color2;

            height: calc( #{$content-height} - #{$header-height} );

            display: flex;
            display: -webkit-flex;

            .content {
                width: $content-width;
            }
        }
    }
</style>
