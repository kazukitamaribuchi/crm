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
        this.getCustomerList()
        .then(res => {
            this.setCustomerList(res)
        })

        this.getProductList()
        .then(res => {
            console.log(res)
            this.setProductList(res)
            this.setPopularProductList(res)
        })

        this.getProductByCategoryList()
        .then(res => {
            // this.setProductList(res)
            this.setProductByCategoryList(res)
        })

        this.getCastList()
        .then(res => {
            this.setCastList(res)
        })

        this.getSalesList()
        .then(res => {
            this.setSalesList(res)
        })
    },
    computed: {
    },
    methods: {
        ...mapMutations([
            'setProductList',
            'setCustomerList',
            'setCastList',
            'setSalesList',
            'setProductByCategoryList',
            'setPopularProductList',
        ]),
        ...mapActions([
            'getProductList',
            'getProductByCategoryList',
            'getCustomerList',
            'getCastList',
            'getSalesList',
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
