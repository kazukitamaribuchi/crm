<template>
    <div>
        <v-card
            flat
        >
            <v-card-title>
                顧客詳細
                <v-btn
                    icon
                    @click="showEditCustomerDialog"
                ><i class='bx bxs-edit'></i></v-btn>
            </v-card-title>
            <vs-tabs :color="colorx" alignment="fixed">
                <vs-tab label="基本情報" @click="colorx = 'rgb(16, 16, 179)'">
                    <v-card-title>
                        {{ customerData.name }} ({{ customerData.age }})
                    </v-card-title>
                    <v-row>
                        <v-col cols="4">
                            <!-- <v-card-subtitle>
                                年齢
                            </v-card-subtitle>
                            <v-card-text>
                                {{ customerData.age }}
                            </v-card-text> -->
                            <v-card-subtitle>
                                誕生日
                            </v-card-subtitle>
                            <v-card-text>
                                {{ customerData.birthday }}
                            </v-card-text>
                            <v-card-subtitle>
                                職業
                            </v-card-subtitle>
                            <v-card-text>
                                {{ customerData.job }}
                            </v-card-text>
                            <v-card-subtitle>
                                会社
                            </v-card-subtitle>
                            <v-card-text>
                                {{ customerData.company }}
                            </v-card-text>
                            <!-- <v-card-subtitle>
                                住所
                            </v-card-subtitle>
                            <v-card-text>
                                {{ customerData.address }}
                            </v-card-text> -->
                        </v-col>
                        <v-col cols="4">
                            <v-card-subtitle>
                                初回来店日
                            </v-card-subtitle>
                            <v-card-text>
                                {{ customerData.first_visit }}
                            </v-card-text>
                            <v-card-subtitle>
                                総来店回数
                            </v-card-subtitle>
                            <v-card-text>
                                {{ customerData.total_visit }}
                            </v-card-text>
                            <v-card-subtitle>
                                総売上
                            </v-card-subtitle>
                            <v-card-text>
                                {{ customerData.total_sales }}
                            </v-card-text>
                        </v-col>
                        <v-col cols="4">
                            <v-card-subtitle>
                                ランク
                            </v-card-subtitle>
                            <v-card-text>
                                {{ customerData.rank_id }}
                            </v-card-text>
                            <v-card-subtitle>
                                会員No
                            </v-card-subtitle>
                            <v-card-text>
                                {{ customerData.customer_no }}
                            </v-card-text>
                            <v-card-subtitle>
                                担当
                            </v-card-subtitle>
                            <v-card-text>
                                エミ
                            </v-card-text>
                        </v-col>
                    </v-row>
                </vs-tab>
                <vs-tab label="売上情報" @click="colorx = 'rgb(244, 10, 10)'">
                    <div class="con-tab-ejemplo">
                        売上情報
                    </div>
                </vs-tab>
                <vs-tab label="その他" @click="colorx = 'rgb(16, 243, 249)'">
                    <div class="con-tab-ejemplo">
                        login
                    </div>
                </vs-tab>
            </vs-tabs>
        </v-card>

        <EditCustomerDialog
            ref="editCustomer"
            @update="customerData = $event"
        />
    </div>
</template>

<script>
import EditCustomerDialog from '@/components/common/dialog/EditCustomerDialog'
import { mapGetters } from 'vuex'

export default {
    name: 'CustomerDetailItem',
    data: () => ({
        customerData: {},
        colorx: 'rgb(16, 16, 179)',
        editCustomerDialog: false,
    }),
    props: {
    },
    components: {
        EditCustomerDialog,
    },
    computed: {
        ...mapGetters([
            'customer',
        ]),
    },
    created () {
        this.$axios({
            method: 'GET',
            url: `/api/customer/${this.$route.params['id']}`,
        })
        .then(res => {
            console.log(res)
            this.customerData = res.data
        })
        .catch(e => {
            console.log(e)
        })
        // 検索から詳細きてうまくいかせるやり方わかったら、↓の様にstoreから取得する方法に切り替え
        // this.customerData = this.customer.find(c => c.id === this.$route.params['id'])
    },
    mounted () {
    },
    methods: {
        showEditCustomerDialog () {
            this.$refs.editCustomer.open(this.customerData)
        }
    }
}
</script>

<style lang="scss">
// .con-slot-tabs {
//     margin-bottom: 4px;
//     background: white !important;
// }
</style>
