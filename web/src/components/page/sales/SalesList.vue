<template>
    <div>

        <v-row>
            <v-col cols="6">
                <v-card-title>
                    売上一覧
                </v-card-title>
            </v-col>
            <v-spacer/>
            <v-col cols="1">
                <v-card-subtitle>
                    <vs-button
                    radius
                    color="primary"
                    type="flat"
                    icon="add_card"
                    @click="inputSalesDialog=!inputSalesDialog"
                    ></vs-button>
                </v-card-subtitle>
            </v-col>
        </v-row>

        <vs-table
            :data="sales"
        >
            <template slot="thead">
                <vs-th>
                    顧客名
                </vs-th>
                <vs-th>
                    担当
                </vs-th>
                <vs-th>
                    総計
                </vs-th>
                <vs-th>
                    会計日
                </vs-th>
            </template>
            <template slot-scope="{data}">
                <vs-tr :data="tr" :key="indextr" v-for="(tr, indextr) in data">
                    <vs-td>
                        {{ tr.customer.name }}
                    </vs-td>
                    <vs-td>
                        {{ tr.cast[0].name }}
                    </vs-td>
                    <vs-td>
                        {{ tr.total_tax_sales }}
                    </vs-td>
                    <vs-td>
                        {{ tr.sales_date }}
                    </vs-td>
                </vs-tr>
            </template>
            <template slot="expand">

            </template>
        </vs-table>

        <InputSalesDialog
            @update="inputSalesDialog = $event"
            :inputSalesDialog="inputSalesDialog"
        />
    </div>
</template>

<script>
import InputSalesDialog from '@/components/common/dialog/InputSalesDialog'
import { mapGetters, mapMutations, mapActions } from 'vuex'

export default {
    name: 'SalesListItem',
    data: () => ({
        inputSalesDialog: false,
    }),
    components: {
        InputSalesDialog,
    },
    computed: {
        ...mapGetters([
            'sales'
        ]),
    },
    created () {
        this.getSalesList()
        .then(res => {
            this.setSalesList(res)
        })
    },
    mounted () {
        console.log('this.sales', this.sales)
    },
    methods: {
        ...mapMutations([
            'setSalesList',
        ]),
        ...mapActions([
            'getSalesList',
        ])
    }
}
</script>

<style lang="scss" scoped>
.vs-con-table {
    background: white;
}

.header-table {
  padding-right: 100px !important;
  margin-bottom: 20px !important;
}

</style>
