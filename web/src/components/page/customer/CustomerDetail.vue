<template>
    <div id="customer_detail_wrap">
        <b-card
            class="customer_detail"
            text-variant="white"
        >
            <b-card-title
                :title="customerData.name"
            >
            </b-card-title>
            <b-card-sub-title
                :sub-title=customerData.name_kana
            >
            </b-card-sub-title>

            <b-row>
                <b-col cols="4">
                    <b-card
                        header="顧客ランク"
                        class="mb-2"
                        header-text-variant="white"
                        :header-bg-variant=backColorHeaderRank
                        border-variant="secondary"
                        :text-variant=textColorRank
                        :bg-variant=backColorRank
                    >
                        <b-card-body class="customer_detail_card_body">
                            <div>
                                <label for="rating-inline">
                                    <b-icon
                                        :icon=cardType
                                        :style=cardColor
                                    ></b-icon>
                                    {{ customerData.rank_name }}
                                </label>
                                <b-form-rating
                                    id="rating-inline"
                                    inline no-border
                                    :value=customerData.rank_id
                                    readonly
                                ></b-form-rating>
                            </div>
                            <small class="customer_detail_rank_detail">
                                【初回来店日】  2022年6月15日
                                <!-- 初回来店日 {{ customerData.first_visit }} -->
                            </small>
                            <small class="customer_detail_rank_detail">
                                【総来店数】  110 回
                                <!-- 総来店数 {{ customerData.total_visit }} -->
                            </small>
                            <small class="customer_detail_rank_detail">
                                【総売上】  ￥100,000,000
                                <!-- 総来店数 {{ customerData.total_sales }} -->
                            </small>
                        </b-card-body>
                    </b-card>
                    <b-card
                        header="基本情報"
                        :text-variant=textColorBasis
                        :bg-variant=backColorBasis
                        header-text-variant="white"
                        border-variant="secondary"
                        :header-bg-variant=backColorHeaderBasis
                    >
                        <b-card-body class="customer_detail_card_body">
                            <b-card-text>
                                <b-form-group
                                    label="年齢"
                                    class="customer_detail_age"
                                >
                                    <b-input-group>
                                        <b-form-input
                                            disabled
                                            v-model="customerData.age"
                                            type="text"
                                        ></b-form-input>
                                    </b-input-group>
                                </b-form-group>

                                <b-form-group
                                    label="誕生日"
                                    class="customer_detail_birthday"
                                >
                                    <b-input-group>
                                        <b-form-input
                                            disabled
                                            v-model="customerData.birthday"
                                            type="text"
                                        ></b-form-input>
                                    </b-input-group>
                                </b-form-group>

                                <b-form-group
                                    label="職業"
                                    class="customer_detail_job"
                                >
                                    <b-input-group>
                                        <b-form-input
                                            disabled
                                            v-model="customerData.job"
                                            type="text"
                                        ></b-form-input>
                                    </b-input-group>
                                </b-form-group>

                                <b-form-group
                                    label="会社"
                                    class="customer_detail_company"
                                >
                                    <b-input-group>
                                        <b-form-input
                                            disabled
                                            v-model="customerData.company"
                                            type="text"
                                        ></b-form-input>
                                    </b-input-group>
                                </b-form-group>

                            </b-card-text>
                        </b-card-body>
                    </b-card>
                </b-col>
                <b-col cols="3">
                    <b-card
                        title="予約状況、ボトルとか"
                        text-variant="black"
                    >

                    </b-card>
                </b-col>
                <b-col>
                    <b-card
                        title="グラフとかテーブルで指名、売上の傾向とか"
                        text-variant="black"
                    >

                    </b-card>
                </b-col>
            </b-row>
        </b-card>


        <!-- <EditCustomerDialog
            ref="editCustomer"
            @update="customerData = $event"
        /> -->

    </div>
</template>

<script>
import EditCustomerDialog from '@/components/common/dialog/EditCustomerDialog'
import { mapGetters } from 'vuex'
import _ from 'lodash'

export default {
    name: 'CustomerDetailItem',
    data: () => ({
        customerData: {},
        editCustomerData: {},
        colorx: 'rgb(16, 16, 179)',
        editCustomerDialog: false,
        isDanger: false,
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
        cardColor () {
            let cardColor = 'rgb(116, 116, 116)'
            switch (this.customerData.rank_id) {
                case 1:
                    cardColor = 'rgb(116, 116, 116)'
                    break;
                case 2:
                    cardColor = 'rgb(192, 192, 192)'
                    break;
                case 3:
                    cardColor = 'rgb(185, 199, 19)'
                    break;
                case 4:
                    cardColor = 'rgb(98, 98, 98)'
                    break;
                case 5:
                    cardColor ='rgb(0, 0, 0)'
                    break;
            }
            return `color: ${cardColor};`
        },
        cardType () {
            if (this.customerData.rank_id == 1) return 'credit-card2-front'
            return 'credit-card2-front-fill'
        },
        backColorBasis () {
            if (this.isDanger) return 'danger'
            return 'light'
        },
        textColorBasis () {
            if (this.isDanger) return 'white'
            return 'black'
        },
        backColorHeaderBasis () {
            if (this.isDanger) return 'danger'
            return 'dark'
        },
        backColorHeaderRank () {
            if (this.isDanger) return 'danger'
            return 'dark'
        },
        backColorRank () {
            if (this.isDanger) return 'danger'
            return 'light'
        },
        textColorRank () {
            if (this.isDanger) return 'white'
            return 'black'
        },
    },
    created () {
        this.$axios({
            method: 'GET',
            url: `/api/customer/${this.$route.params['id']}`,
        })
        .then(res => {
            console.log(res)
            this.customerData = _.cloneDeep(res.data)
            this.isDanger = this.customerData.caution_flg
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

<style lang="scss" scoped>
    #customer_detail_wrap {
        background-color: $theme-color;
        // background-color: white;
        margin-top: $main-top-margin;
        margin-left: $main-top-side-margin;
        margin-right: $main-top-side-margin;
        height: $main-height;
        padding: 20px;

        .customer_detail {
            background-color: $theme-color;
            height: 100%;

            .customer_detail_card_body {
                padding: 0 1.5rem;


                .input-group-text {
                    height: 100%;
                    border-radius: 5px 0 0 5px !important;
                }

                .customer_detail_age {
                    width: 6rem;
                }

                .customer_detail_birthday {
                    width: 8rem;
                }

                .customer_detail_job {
                    width: 12rem;
                }

                .customer_detail_rank_detail {
                    display: block;
                }

            }

        }

    }

// .con-slot-tabs {
//     margin-bottom: 4px;
//     background: white !important;
// }
</style>
