<template>
    <v-container
        id="home-wrap"
        fluid
    >
        <vs-row vs-w="12">
            <Header/>
        </vs-row>
        <vs-row vs-w="12">
            <vs-col vs-w="2">
                <Sidebar/>
            </vs-col>
            <vs-col vs-w="10">
                <Top/>
            </vs-col>
        </vs-row>
    </v-container>
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

        this.getProductByCategory()
        .then(res => {
            console.log(res)
            this.setProductList(res)
        })
        .catch(e => {
            console.log(e)
        })
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
#home-wrap {
    padding: 0;
}
</style>
