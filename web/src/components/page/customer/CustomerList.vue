<template>
    <div>
        <!-- <ListView
            :viewData=customer
            :type='customer'
        /> -->


        <v-row>
            <v-col cols="6">
                <v-card-title>
                    顧客一覧
                </v-card-title>
            </v-col>
            <v-spacer/>
            <v-col cols="1">
                <v-card-subtitle>
                    <vs-button
                        radius
                        color="primary"
                        type="flat"
                        icon="person_add"
                        @click="createCustomerDialog=!createCustomerDialog"
                    ></vs-button>
                </v-card-subtitle>
            </v-col>
        </v-row>
        <vs-table
            :data="customer"
            v-model="selected"
            @selected="showCustomerDetail"
            @dblSelection="moveCustomerDetail"
            search
        >
            <!-- <template slot="header">
                <v-card-subtitle>
                    顧客一覧
                </v-card-subtitle>
            </template> -->
            <template slot="thead">
                <vs-th sort-key="name">
                    名前
                </vs-th>
                <vs-th sort-key="age">
                    年齢
                </vs-th>
                <vs-th sort-key="birthday">
                    誕生日
                </vs-th>
                <vs-th sort-key="rank">
                    ランク
                </vs-th>
                <vs-th sort-key="total_visit">
                    総来店回数
                </vs-th>
                <vs-th sort-key="total_sales">
                    総売上
                </vs-th>
                <vs-th sort-key="first_visit">
                    初来店日
                </vs-th>
            </template>
            <template slot-scope="{data}">
                <vs-tr
                    :data="tr"
                    :key="indextr"
                    v-for="(tr, indextr) in data"
                >
                    <vs-td>
                        {{ tr.name }}
                    </vs-td>
                    <vs-td>
                        {{ tr.age }}
                    </vs-td>
                    <vs-td>
                        {{ tr.birthday }}
                    </vs-td>
                    <vs-td>
                        {{ tr.rank }}
                    </vs-td>
                    <vs-td>
                        {{ tr.total_visit }}
                    </vs-td>
                    <vs-td>
                        {{ tr.total_sales }}
                    </vs-td>
                    <vs-td>
                        {{ tr.first_visit }}
                    </vs-td>
                </vs-tr>
            </template>
            <template slot="expand">

            </template>
        </vs-table>

        <CreateCustomerDialog
            @update="createCustomerDialog = $event"
            :createCustomerDialog="createCustomerDialog"
        />
    </div>
</template>

<script>
import CreateCustomerDialog from '@/components/common/dialog/CreateCustomerDialog'
import { mapGetters, mapMutations, mapActions } from 'vuex'
// import ListView from '@/components/parts/ListView'/

export default {
    name: 'CustomerListItem',
    data: () => ({
        selected: [],
        createCustomerDialog: false,
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
        this.getCustomerList()
        .then(res => {
            this.setCustomerList(res)
        })
    },
    mounted () {
    },
    methods: {
        ...mapMutations([
            'setCustomerList',
        ]),
        ...mapActions([
            'getCustomerList',
        ]),
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
    }
}
</script>

<style lang="scss" scoped>
.vs-con-table {
    background: white;
}

// .vs-table--tbody {
//     z-index: 200 !important;
// }

.header-table {
  padding-right: 100px !important;
  margin-bottom: 20px !important;
}

</style>
