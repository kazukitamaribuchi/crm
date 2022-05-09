<template>
    <div>
        <vs-table
            :data="bottle"
        >
            <template slot="header">
                <h3>
                    ボトル一覧
                </h3>
            </template>
            <template slot="thead">
                <vs-th>
                    顧客名
                </vs-th>
                <vs-th>
                    ボトル名
                </vs-th>
                <vs-th>
                    開封日
                </vs-th>
                <vs-th>
                    期限
                </vs-th>
            </template>
            <template slot-scope="{data}">
                <vs-tr :data="tr" :key="indextr" v-for="(tr, indextr) in data">
                    <vs-td>
                        {{ tr.customer.name }}
                    </vs-td>
                    <vs-td>
                        {{ tr.product.name }}
                    </vs-td>
                    <vs-td>
                        {{ tr.open_date }}
                    </vs-td>
                    <vs-td>
                        {{ tr.deadline }}
                    </vs-td>
                </vs-tr>
            </template>
            <template slot="expand">

            </template>
        </vs-table>
    </div>
</template>

<script>
import { mapGetters, mapMutations, mapActions } from 'vuex'

export default {
    name: 'BottleListItem',
    data: () => ({
    }),
    computed: {
        ...mapGetters([
            'bottle'
        ]),
    },
    created () {
        this.getBottleList()
        .then(res => {
            this.setBottleList(res)
        })
    },
    mounted () {
        console.log('this.bottle', this.bottle)
    },
    methods: {
        ...mapMutations([
            'setBottleList',
        ]),
        ...mapActions([
            'getBottleList',
        ])
    }
}
</script>
