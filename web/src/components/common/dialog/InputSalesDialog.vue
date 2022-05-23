<template>
    <div>
        <b-modal
            v-model="dialog"
            size="xl"
            screenable
            title="売上入力"
            header-bg-variant="dark"
            header-text-variant="light"
        >
            <b-form class="input_sales_form">
                <b-card bg-variant="light" class="mt-3">
                    <b-form-group
                        label-cols-lg="3"
                        label="基本料金"
                        label-size="lg"
                        label-class="font-weight-bold pt-0"
                        class="mb-0"
                    >
                        <b-row>
                            <b-col cols="4">
                                <b-form-group
                                    class="input_sales_customer_no"
                                    label="会員No"
                                >
                                    <b-input-group>
                                        <b-form-input
                                            v-model="inputSalesData.customer_no"
                                            type="number"
                                            placeholder="会員Noを入力してください"
                                            required
                                        ></b-form-input>
                                    </b-input-group>
                                </b-form-group>
                            </b-col>
                            <b-col cols="4"></b-col>
                            <b-col cols="2">
                                <b-form-group
                                    label="料金プラン"
                                    class="mb-0 pb-0"
                                    label-class="mb-0 pb-0"
                                >
                                    <b-form-radio-group
                                        class="pt-0"
                                        :options="planOptions"
                                        v-model="basicPlan"
                                    ></b-form-radio-group>
                                </b-form-group>
                            </b-col>
                            <b-col>
                                <b-form-group
                                    class="input_sales_stay_hour_wrap"
                                    label="滞在時間"
                                >
                                    <b-form-select
                                        v-model="selectedStayHour"
                                        :options="stayHourOptions"
                                        stayHourOptions
                                        value-field="value"
                                        text-field="text"
                                        class="input_sales_stay_hour"
                                    ></b-form-select>

                                    <!-- <b-input-group>
                                        <b-form-input
                                            v-model="inputSalesData.stay_hour"
                                            type="number"
                                            placeholder="滞在時間を入力してください"
                                            required
                                        ></b-form-input>
                                    </b-input-group> -->
                                </b-form-group>
                            </b-col>
                        </b-row>
                        <b-row>
                            <b-col cols="8">
                                <label>担当キャスト</label>
                                <div
                                    class="mt-2"
                                >
                                    <table
                                        v-if="appointedCastDataList.length > 0"
                                        class="appointed_cast_area"
                                    >
                                        <tr>
                                            <th
                                                v-for="(castHeader, id) in appointedCastHeader"
                                                :key=id
                                            >{{ castHeader.text }}</th>
                                        </tr>
                                        <tr
                                            v-for="(castData, idx) in appointedCastDataList"
                                            :key=idx
                                        >
                                            <td>
                                                <b-avatar
                                                    :src="apiPath + castData.cast.icon"
                                                    class="cast_icon"
                                                    v-if="castData.cast.icon != null"
                                                ></b-avatar>
                                                <b-avatar
                                                    :src="defaultCastIcon"
                                                    class="cast_icon"
                                                    v-else
                                                ></b-avatar>
                                            </td>
                                            <td>{{ castData.cast.name }}</td>
                                            <td>{{ getAppointStr(castData.appointType) }}</td>
                                            <td>{{ getDouhanStr(castData.isDouhan) }}</td>
                                            <td>{{ getStayHourStr(castData.stayHour) }}</td>
                                            <td>
                                                <b-icon
                                                    icon="trash-fill"
                                                    aria-hidden="true"
                                                    @click="deleteCast(castData, idx)"
                                                    variant="danger"
                                                    class="trash_icon"
                                                ></b-icon>
                                            </td>
                                        </tr>
                                    </table>
                                    <b-button
                                        size="sm"
                                        @click="showAddCastDialog"
                                        class="mt-3"
                                        variant="primary"
                                    >
                                        <b-icon
                                            icon="person-plus"
                                            aria-hidden="true"
                                        ></b-icon> キャストを追加...
                                    </b-button>
                                </div>
                            </b-col>
                            <b-col cols="4">
                                <b-form-group
                                    class="input_sales_date"
                                    label="会計日"
                                >
                                    <b-form-datepicker
                                        v-model="inputSalesData.sales_date"
                                        placeholder="会計日を入力してください"
                                    ></b-form-datepicker>
                                </b-form-group>
                            </b-col>
                        </b-row>

                    </b-form-group>
                </b-card>

                <b-card bg-variant="light" class="mt-3">
                    <b-form-group
                        label-cols-lg="3"
                        label="明細"
                        label-size="lg"
                        label-class="font-weight-bold pt-0"
                        class="mb-0"
                    >
                        <b-row>
                            <b-col cols="4">
                                <b-button
                                    size="sm"
                                    @click="showAddDetailDialog"
                                    class="mt-3"
                                    variant="primary"
                                >
                                    <b-icon
                                        icon="plus-circle"
                                        aria-hidden="true"
                                    ></b-icon> 明細を追加...
                                </b-button>
                            </b-col>
                        </b-row>
                    </b-form-group>
                    <b-table
                        v-if="inputSalesDetailData.length > 0"
                        :fields="inputSalesDetailFields"
                        :items="inputSalesDetailData"
                        hover
                        table-variant="light"
                    >
                        <template #cell(actions)="data">
                            <b-row>
                                <b-col>
                                    <b-button
                                        size="sm"
                                        variant="light"
                                        @click="editSalesDetail(data)"
                                    >
                                        <b-icon
                                            icon="pencil-square"
                                            aria-hidden="true"
                                            variant="primary"
                                            class="trash_icon"
                                        ></b-icon>
                                    </b-button>
                                </b-col>
                                <b-col>
                                    <b-button
                                        size="sm"
                                        variant="light"
                                        @click="deleteSalesDetail(data)"
                                    >
                                        <b-icon
                                            icon="trash-fill"
                                            aria-hidden="true"
                                            variant="danger"
                                            class="trash_icon"
                                        ></b-icon>
                                    </b-button>
                                </b-col>
                            </b-row>
                        </template>
                    </b-table>
                </b-card>

            </b-form>
            <template #modal-footer>
                <b-container fluid>
                    <b-row>
                        <b-col cols="2">
                            <b-card-sub-title>
                                総計(税抜)
                            </b-card-sub-title>
                            <b-card-title class="mb-0">
                                ￥ {{ totalPrice }}
                            </b-card-title>
                        </b-col>
                        <b-col cols="2">
                            <b-card-sub-title>
                                総計(税込)
                            </b-card-sub-title>
                            <b-card-title class="mb-0">
                                ￥ {{ totalTaxPrice }}
                            </b-card-title>
                        </b-col>
                        <b-col align="right" class="add_sales_detail_footer_col">
                            <b-button
                                variant="secondary"
                                @click="close"
                                class="btn_close"
                            >
                                閉じる
                            </b-button>
                            <b-button
                                variant="primary"
                                @click="register"
                                :disabled=isDisabled
                            >
                                登録
                            </b-button>
                        </b-col>
                    </b-row>
                </b-container>
            </template>
        </b-modal>

        <InputSalesAddDetailDialog
            ref="inputSalesAddDetailDialog"
        />

        <InputSalesAddCastDialog
            ref="inputSalesAddcastDialog"
            :appointed="appointedCastDataList"
        />
    </div>
</template>

<script>
import InputSalesDetailDialog from '@/components/common/dialog/InputSalesDetailDialog'
import InputSalesAddDetailDialog from '@/components/common/dialog/InputSalesAddDetailDialog'
import InputSalesAddCastDialog from '@/components/common/dialog/InputSalesAddCastDialog'
import { mapMutations } from 'vuex'
import { Const } from '@/assets/js/const'
const Con = new Const()

export default {
    name: 'InputSalesDialogItem',
    props: {
    },
    components: {
        InputSalesDetailDialog,
        InputSalesAddCastDialog,
        InputSalesAddDetailDialog,
    },
    data: () => ({
        basicPlan: 0,
        planOptions: [
            {
                text: 'Normal',
                value: 0,
            },
            {
                text: 'VIP',
                value: 1,
            }
        ],
        selectedStayHour: null,
        dialog: false,
        inputSalesData: {
            sales_date: '2022-05-14'
        },
        inputSalesDetailTestData: [
            {
                product: {
                    name: 'レモンサワー',
                    price: '500',
                    tax: {
                        tax_rate: 30,
                    },
                },
                quantity: 2.0,
                actually_price: 400,
            },
        ],
        inputSalesDetailTestData2: [
            {
                name: 'レモンサワー',
                price: '1000',
                actually_price: 500,
                tax_rate: 30,
                quantity: 2.0,
                total_price: 500,
            },
            {
                name: 'レモンサワー',
                price: '500',
                actually_price: 400,
                tax_rate: 30,
                quantity: 2.0,
                total_price: 800,
            },
            {
                name: 'レモンサワー',
                price: '500',
                actually_price: 400,
                tax_rate: 30,
                quantity: 2.0,
                total_price: 800,
            },
            {
                name: 'レモンサワー',
                price: '500',
                actually_price: 400,
                tax_rate: 30,
                quantity: 2.0,
                total_price: 800,
            },
        ],
        inputSalesDetailFields: [
            {
                key: 'name',
                sortable: true,
                headerTitle: '商品名'
            },
            {
                key: 'price',
                sortable: true,
                headerTitle: '定価'
            },
            {
                key: 'actually_price',
                sortable: true,
                headerTitle: '実価格'
            },
            {
                key: 'tax_rate',
                sortable: true,
                headerTitle: '税率'
            },
            {
                key: 'quantity',
                sortable: true,
                headerTitle: '個数'
            },
            {
                key: 'total_price',
                sortable: true,
                headerTitle: '総計(税抜)'
            },
            {
                key: 'total_tax_price',
                sortable: true,
                headerTitle: '総計(税込)'
            },
            {
                key: 'Actions',
                sortable: true,
                headerTitle: 'Actions'
            },
        ],
        inputSalesDetailData: [],
        inputSalesDetailDialog: false,
        totalSales: 0,
        totalTaxSales: 0,
        appointedCastDataList: [],
        stayHourOptions: [
            { value: 0.5, text: '0.5' },
            { value: 1.0, text: '1.0' },
            { value: 1.5, text: '1.5' },
            { value: 2.0, text: '2.0' },
            { value: 2.5, text: '2.5' },
            { value: 3.0, text: '3.0' },
            { value: 3.5, text: '3.5' },
            { value: 4.0, text: '4.0' },
            { value: 4.5, text: '4.5' },
            { value: 5.0, text: '5.0' },
            { value: 5.5, text: '5.5' },
            { value: 6.0, text: '6.0' },
            { value: 6.5, text: '6.5' },
            { value: 7.0, text: '7.0' },
            { value: 7.5, text: '7.5' },
            { value: 8.0, text: '8.0' },
            { value: 8.5, text: '8.5' },
            { value: 9.0, text: '9.0' },
            { value: 9.5, text: '9.5' },
            { value: 10.0, text: '10.0' },
        ],
        appointedCastHeader: [
            { text: '' },
            { text: '名前' },
            { text: '指名' },
            { text: '同伴' },
            { text: '時間' },
            { text: '' },
        ],
        apiPath: 'http://localhost:8000',
        defaultCastIcon: 'http://localhost:8000/media/upload/女性1111.png',
    }),
    created () {
        this.$eventHub.$off('addCast')
        this.$eventHub.$on('addCast', this.addCast)

        this.$eventHub.$off('addSalesDetail')
        this.$eventHub.$on('addSalesDetail', this.addSalesDetail)
    },
    computed: {
        totalPrice () {
            let totalPrice = 0
            // 明細部 そのうち計算量考慮
            for (const item of this.inputSalesDetailData) {
                totalPrice += item.total_price
            }

            // 滞在時間
            if (this.selectedStayHour != null) {
                let planPrice = Con.BASIC_PLAN_PRICE[this.basicPlan]
                totalPrice += (planPrice * this.selectedStayHour)
            }

            // 指名料も画面側に落とすか画面で持つか
            // 指名
            const appointPrice = {
                0: 2000,
                1: 3000,
                2: 2000,
                3: 4000
            }
            for (const item of this.appointedCastDataList) {
                console.log(item)
                totalPrice += (item.isDouhan) ? appointPrice[3] : appointPrice[item.appointType]
            }

            return totalPrice
        },
        totalTaxPrice () {
            let totalTaxPrice = 0
            // そのうち計算量考慮
            for (const item of this.inputSalesDetailData) {
                totalTaxPrice += item.total_tax_price
            }

            // 基本料金も画面側に落としてそこから取得
            // 滞在時間
            if (this.selectedStayHour != null) {
                let planPrice = Con.BASIC_PLAN_PRICE[this.basicPlan]
                let tax = planPrice * this.selectedStayHour * 0.3
                totalTaxPrice += (planPrice * this.selectedStayHour + tax)
            }

            // 指名料も画面側に落とすか画面で持つか
            // 指名
            const appointPrice = {
                0: 2000,
                1: 3000,
                2: 2000,
                3: 4000
            }
            // 指名
            for (const item of this.appointedCastDataList) {
                console.log(item)
                const apo = (item.isDouhan) ? appointPrice[3] : appointPrice[item.appointType]
                let tax = apo * 0.3
                totalTaxPrice += tax + apo
            }



            return totalTaxPrice
        },
        isDisabled () {
            return true
        }
    },
    methods: {
        ...mapMutations([
        ]),
        register () {
            console.log('register', this.inputSalesData)
            // const data = this.inputSalesData
            // this.$axios({
            //     method: 'POST',
            //     url: '/api/sales/',
            //     data: {
            //     }
            // })
            // .then(res => {
            //     console.log(res)
            // })
            // .catch(e => {
            //     console.log(e)
            // })
        },
        init () {
            this.inputSalesData = {}
        },
        test () {
            console.log('test')
        },
        open () {
            this.dialog = true
        },
        close () {
            this.dialog = false
        },
        showAddCastDialog () {
            this.$refs.inputSalesAddcastDialog.open()
        },
        showAddDetailDialog () {
            this.$refs.inputSalesAddDetailDialog.open()
        },
        addCast (data) {
            console.log('addCast', data)
            if (this.selectedStayHour == 0 || this.selectedStayHour < data.stayHour) {
                this.selectedStayHour = data.stayHour
            }
            this.appointedCastDataList.push(data)
        },
        getAppointStr (type) {
            if (type === 0) return '指名'
            if (type === 1) return '本指名'
            if (type === 2) return '場内指名'
            return '-'
        },
        getDouhanStr (isDouhan) {
            if (isDouhan) return '有'
            return '無し'
        },
        deleteCast (castData, idx) {
            this.appointedCastDataList.splice(idx, 1)
        },
        editSalesDetail (data) {
            console.log('editSalesDetail', data)
        },
        deleteSalesDetail (data) {
            this.inputSalesDetailData.splice(data.index, 1)
        },
        addSalesDetail (data) {
            this.inputSalesDetailData.push(data)
        },
        getStayHourStr (stayHour) {
            if (stayHour == 0) return 'full'
            return stayHour
        }
    }
}

</script>

<style lang="scss" scoped>

    .input_sales_form {
        padding: 20px;

        .input_sales_stay_hour_wrap {
            .input_sales_stay_hour {
                padding: 4px 9px;
                border-radius: 3px;
                border: 1px solid rgba(125, 125, 125, 0.6);
            }
        }

        .appointed_cast_area {
            width: 100%;
            th:nth-child(1), td:nth-child(1) {
                width: 8%;
            }
            th:nth-child(2), td:nth-child(2) {
                width: 25%;
            }
            th:nth-child(3), td:nth-child(3) {
                width: 20%;
            }
            th:nth-child(4), td:nth-child(4) {
                width: 15%;
            }
            th:nth-child(5), td:nth-child(5) {
                width: 20%;
            }

            .cast_icon {
                border: 1px solid rgba(200, 200, 200, 0.5);
            }

            .trash_icon {
                cursor: pointer;
            }
        }
    }
    .input-group-text {
        height: 100%;
        border-radius: 5px 0 0 5px !important;
    }


    .table > :not(caption) {
        border-bottom-width: 0;
    }

// .container.form-wrap {
//   padding: 0px 40px;
// }

// .vs-component.vs-con-input-label.vs-input.vs-input-primary::v-deep {
//     width: 100%;
// }
// .vs-input-parent::v-deep {
//     width: 100%;
//     .vs-input {
//         width: 100%;
//     }
// }

// .sales_dialog_footer {
//     position: fixed;
//     bottom: 0;
// }

</style>
