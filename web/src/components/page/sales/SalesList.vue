<template>
    <div id="sales_list_wrap">
        <b-row>
            <b-col cols="4">
                <b-card class="sales_list_1">
                </b-card>
            </b-col>
            <b-col>
                <b-card class="sales_list_2">
                </b-card>
            </b-col>
            <b-col>
                <b-card class="sales_list_2">
                </b-card>
            </b-col>
        </b-row>
        <b-row>
            <b-col cols="3">
                <b-card class="sales_list_3">
                </b-card>
            </b-col>
            <b-col cols="6">
                <b-card class="sales_list_4">
                </b-card>
            </b-col>
            <b-col>
                <b-card class="sales_list_5">
                </b-card>
            </b-col>
        </b-row>
        <!-- <b-card
            class="customer_list"
            no-body
        >

        </b-card> -->
        <!-- <v-row>
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
        </vs-table> -->

        <!-- <InputSalesDialog
            @update="inputSalesDialog = $event"
            :inputSalesDialog="inputSalesDialog"
        /> -->
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
    },
    mounted () {
    },
    methods: {
    }
}
</script>

<style lang="scss" scoped>
    #sales_list_wrap {
        // background-color: $theme-color;
        // background-color: white;
        margin-top: $main-top-margin;
        margin-left: $main-top-side-margin;
        margin-right: $main-top-side-margin;
        height: $main-height;
        padding: 20px;

        .sales_list_1 {
            background-color: $theme-color;
            height: 25rem;
        }
        .sales_list_2 {
            background-color: $theme-color;
            height: 25rem;
        }
        .sales_list_3 {
            background-color: $theme-color;
            height: 25rem;
        }
        .sales_list_4 {
            background-color: $theme-color;
            height: 25rem;
        }
        .sales_list_5 {
            background-color: $theme-color;
            height: 25rem;
        }
    }
</style>
