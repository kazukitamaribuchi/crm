<template>
    <div>
        <v-dialog
            v-model="localInputSalesDialog"
            max-width="1200px"
            fullscreen
            transition="dialog-bottom-transition"
        >
            <v-card>
                <v-card-title
                    id="login-title"
                >
                    売上入力
                </v-card-title>

                <v-container fluid class="form-wrap">
                    <v-row>
                        <v-col cols="2">
                            <vs-input
                                v-model="inputSalesData.customer_no"
                                placeholder="顧客No"
                                label="顧客No"
                            ></vs-input>
                        </v-col>
                    </v-row>

                    <v-row>
                        <v-col
                            class="d-flex"
                            cols="12"
                            sm="1"
                        >
                            <v-select
                                :items="items"
                                outlined
                                label="基本料金"
                                dense
                            ></v-select>
                        </v-col>
                            <!-- <vs-select
                                v-model="inputSalesData.basic_service"
                                label="基本料金"
                            >
                                <vs-select-item
                                    :key="index"
                                    :value="item.value"
                                    :text="item.text"
                                    v-for="item, index in options1"
                                    @click.stop="test"
                                    @select="test"
                                />
                            </vs-select> -->
                        <v-col cols="1">
                            <vs-checkbox v-model="inputSalesData.vip">vip</vs-checkbox>
                        </v-col>
                    </v-row>

                    <v-row>
                        <v-col cols="12">
                            <vs-button color="primary" type="gradient" icon="favorite">指名登録</vs-button>
                        </v-col>
                    </v-row>

                    <v-row class="mt-10">
                        <v-col cols="2">
                            商品
                        </v-col>
                        <v-col cols="1">
                            個数
                        </v-col>
                        <v-col cols="1">
                            税
                        </v-col>
                        <v-col cols="2">
                            料金(税抜)
                        </v-col>
                        <v-col cols="2">
                            料金(税込)
                        </v-col>
                        <v-col cols="3">
                            備考
                        </v-col>
                        <v-col cols="1">
                            サービス
                        </v-col>
                    </v-row>

                    <v-row>
                        <!-- <v-btn
                            class="mt-10"
                            icon
                        >
                            <i class='bx bxs-user-plus'></i>
                        </v-btn> -->
                        <vs-button
                            color="primary"
                            type="border"
                            icon="add"
                            @click="inputSalesDetailDialog=!inputSalesDetailDialog"
                        >明細追加
                        </vs-button>
                    </v-row>

                    <!-- <v-row class="mt-4">
                        <v-spacer/>
                        <v-col cols="2">
                            <v-card-title>
                                総額(税抜)
                            </v-card-title>
                            <v-card-text>
                                {{ totalSales }} 円
                            </v-card-text>

                        </v-col>
                        <v-col cols="2">
                            <v-card-title>
                                総額(税込)
                            </v-card-title>
                            <v-card-text>
                                {{ totalTaxSales }} 円
                            </v-card-text>
                        </v-col>
                    </v-row> -->

                    <v-row class="sales_dialog_footer">
                        <!-- <v-spacer/> -->
                        <v-spacer/>
                        <v-col cols="2">
                            <v-card-title>
                                総額(税抜)
                            </v-card-title>
                            <v-card-text>
                                {{ totalSales }} 円
                            </v-card-text>

                        </v-col>
                        <v-col cols="2">
                            <v-card-title>
                                総額(税込)
                            </v-card-title>
                            <v-card-text>
                                {{ totalTaxSales }} 円
                            </v-card-text>
                        </v-col>

                        <v-col cols="2">
                            <v-card-actions>
                                <vs-button
                                    color="success"
                                    type="filled"
                                    icon="done"
                                    @click="register"
                                >登録</vs-button>
                                <vs-button
                                    color="primary"
                                    type="border"
                                    icon="done"
                                    @click="localInputSalesDialog = false"
                                >閉じる</vs-button>
                            </v-card-actions>
                        </v-col>
                    </v-row>
                </v-container>
            </v-card>
        </v-dialog>

        <InputSalesDetailDialog
            @update="inputSalesDetailDialog = $event"
            :inputSalesDetailDialog="inputSalesDetailDialog"
        />
    </div>
</template>

<script>
import InputSalesDetailDialog from '@/components/common/dialog/InputSalesDetailDialog'
import { mapMutations } from 'vuex'
import { Const } from '@/assets/js/const'
const Con = new Const()

export default {
    name: 'InputSalesDialogItem',
    props: {
        inputSalesDialog: {
            type: Boolean,
            required: true,
        },
    },
    components: {
        InputSalesDetailDialog,
    },
    data: () => ({
        inputSalesData: {},
        inputSalesDetailDialog: false,
        totalSales: 0,
        totalTaxSales: 0,
        options1: [
            {text:'0.5',value:0.5},
            {text:'1',value:1},
            {text:'1.5',value:1.5},
            {text:'2',value:2},
            {text:'2.5',value:2.5},
            {text:'3',value:3},
            {text:'3.5',value:3.5},
            {text:'4',value:4},
        ],
        items: [0.5, 1, 1.5, 2]
    }),
    computed: {
        localInputSalesDialog: {
            get: function () {
                return this.inputSalesDialog
            },
            set: function (value) {
                this.$emit('update', value)
            },
        },
    },
    methods: {
        ...mapMutations([
        ]),
        register () {
            console.log('register', this.inputSalesData)
            const data = this.inputSalesData
            this.$axios({
                method: 'POST',
                url: '/api/sales/',
                data: {
                }
            })
            .then(res => {
                console.log(res)
            })
            .catch(e => {
                console.log(e)
            })
        },
        init () {
            this.inputSalesData = {}
            this.localInputSalesDialog = false
        },
        test () {
            console.log('test')
        }
    }
}

</script>

<style lang="scss" scoped>
.container.form-wrap {
  padding: 0px 40px;
}

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
