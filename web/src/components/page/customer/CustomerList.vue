<template>
    <div id="customer_list_wrap">
        <b-row>
            <b-col cols="8">
                <b-card class="customer_list_area1">
                </b-card>
            </b-col>
            <b-col>
                <b-card class="customer_list_area2">
                </b-card>
            </b-col>
        </b-row>
        <b-card
            class="customer_list_area3"
            no-body
        >
            <!-- <b-card-header header-tag="nav">
                <b-nav card-header tabs>
                    <b-nav-item
                        v-for="item in navHeader"
                        :key="item.id"
                        @click="navClick(item)"
                        :active="item.id == activeHeader"
                    >
                        {{ item.title }}
                    </b-nav-item>
                </b-nav>
            </b-card-header> -->


            <!-- <b-card-body v-if="activeHeader == 1"> -->
                <b-table
                    striped
                    hover
                    :items="customer"
                    :fields="fields"
                    :dark="true"
                    caption-top
                    selectable
                    :tbody-tr-class="rowClass"
                    @row-selected="onRowSelected"
                >

                    <template #cell(rank_id)="data">
                        <b v-if="data.value == 1">
                            <b-icon
                                icon="credit-card2-front-fill"
                            ></b-icon>
                            <b>
                                normal
                            </b>
                        </b>
                        <b v-else-if="data.value == 2">
                            <b-icon
                                icon="credit-card2-front-fill"
                                style="color: #c0c0c0;"
                            ></b-icon>

                            <b>
                                silver
                            </b>
                        </b>
                        <b v-else-if="data.value == 3">
                            <b-icon
                                icon="credit-card2-front-fill"
                                style="color: #e1f30c;"
                            ></b-icon>
                            <b>
                                gold
                            </b>
                        </b>
                        <b v-else-if="data.value == 4">
                            <b-icon
                                icon="credit-card2-front-fill"
                                style="color: rgb(98,98,98);"
                            ></b-icon>
                            <b>
                                platinum
                            </b>
                        </b>
                        <b v-else-if="data.value == 5">
                            <b-icon
                                icon="credit-card2-front"
                            ></b-icon>
                            <b>
                                black
                            </b>
                        </b>
                    </template>

                    <template #cell(age)="data">
                        <b v-if="data.value != ''">
                            {{ data.value }} 歳
                        </b>
                        <b v-else>
                            -
                        </b>
                    </template>

                    <template #cell(birthday)="data">
                        <b v-if="data.value != ''">
                            {{ data.value }}
                        </b>
                        <b v-else>
                            -
                        </b>
                    </template>

                    <template #cell(total_visit)="data">
                        <b>{{ data.value }}</b> <b>回</b>
                    </template>

                    <template #cell(total_sales)="data">
                        <b>￥{{ data.value }}</b>
                    </template>

                    <template #cell(first_visit)="data">
                        <b v-if="data.value != ''">
                            <b>{{ data.value }}</b>
                        </b>
                        <b v-else>
                            -
                        </b>
                    </template>

                    <template #cell(caution_flg)="data">
                        <b v-if="data.value == true">
                            <b class="text-danger">要注意人物</b>
                        </b>
                        <b v-else>
                            -
                        </b>
                    </template>

                </b-table>
            <!-- </b-card-body>

            <b-card-body v-else-if="activeHeader == 2">
                <b style="color: white;">Customer Sales</b>
            </b-card-body>

            <b-card-body v-else-if="activeHeader == 3">
                <b style="color: white;">Customer Ranking</b>
            </b-card-body> -->

        </b-card>

        <!-- <CreateCustomerDialog
            @update="createCustomerDialog = $event"
            :createCustomerDialog="createCustomerDialog"
        /> -->
    </div>
</template>

<script>
import CreateCustomerDialog from '@/components/common/dialog/CreateCustomerDialog'
import { mapGetters, mapMutations, mapActions } from 'vuex'
// import ListView from '@/components/parts/ListView'/

export default {
    name: 'CustomerListItem',
    data: () => ({
        selected: {},
        createCustomerDialog: false,
        fields: [
            {
                key: 'name',
                sortable: true,
                headerTitle: '名前',
            },
            {
                key: 'rank_id',
                sortable: true,
            },
            {
                key: 'age',
                sortable: true,
                // thStyle: {
                //     'background-color': 'yellow',
                // }
            },
            {
                key: 'birthday',
                sortable: true
            },
            {
                key: 'total_visit',
                sortable: true
            },
            {
                key: 'total_sales',
                sortable: true
            },
            {
                key: 'first_visit',
                sortable: true
            },
            {
                key: 'customer_no',
                sortable: true,
            },
            {
                key: 'caution_flg',
                sortable: true,
            }
        ],
        navHeader: [
            {
                id: 1,
                title: 'Customer List',
                active: false,
            },
            {
                id: 2,
                title: 'Customer Sales',
                active: false,
            },
            {
                id: 3,
                title: 'Customer Ranking',
                active: false,
            },
        ],
        activeHeader: 1,
    }),
    components: {
        // ListView,
        CreateCustomerDialog,
    },
    computed: {
        ...mapGetters([
            'customer'
        ]),
    },
    created () {
    },
    mounted () {
    },
    methods: {
        showCustomerDetail (data) {
            // 1回クリック時
        },
        moveCustomerDetail (data) {
            // ダブルクリック時
            this.$router.push({
                name: 'CustomerDetail',
                params: {
                    id: data.id
                }
            })
        },
        onRowSelected (item) {
            this.$router.push({
                name: 'CustomerDetail',
                params: {
                    id: item[0].customer_no
                }
            })
        },
        rowClass (item, type) {
            if (!item || type !== 'row') return
            if (item.caution_flg == true) return 'table-danger'
        },
        navClick (item) {
            this.activeHeader = item.id
        }
    }
}
</script>

<style lang="scss" scoped>
    #customer_list_wrap {
        // background-color: $theme-color;
        // background-color: white;
        margin-top: $main-top-margin;
        margin-left: $main-top-side-margin;
        margin-right: $main-top-side-margin;
        height: $main-height;
        padding: 20px;

        .customer_list_area1 {
            background-color: $theme-color;
            height: 25rem;
        }
        .customer_list_area2 {
            background-color: $theme-color;
            height: 25rem;
        }

        .customer_list_area3 {
            padding: 1.7rem;
            background-color: $theme-color;
            height: 100%;
            margin-top: 1rem;
        }
    }

// .vs-con-table {
//     background: white;
// }

// .vs-table--tbody {
//     z-index: 200 !important;
// }

// .header-table {
//   padding-right: 100px !important;
//   margin-bottom: 20px !important;
// }

</style>
