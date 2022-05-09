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
                        <v-col cols="10">
                            <v-card-text class="mt-0 pt-0 mb-0 pb-0">
                                キャスト
                            </v-card-text>
                            <v-btn
                                icon
                                class="ml-4 mb-3 mt-0 pt-0"
                            >
                                <i class='bx bxs-user-plus'></i>
                            </v-btn>
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
        }
    }
}

</script>

<style lang="scss" scoped>
.container.form-wrap {
  padding: 0px 40px;
}

.vs-component.vs-con-input-label.vs-input.vs-input-primary::v-deep {
    width: 100%;
}
.vs-input-parent::v-deep {
    width: 100%;
    .vs-input {
        width: 100%;
    }
}

// .sales_dialog_footer {
//     position: fixed;
//     bottom: 0;
// }

</style>
