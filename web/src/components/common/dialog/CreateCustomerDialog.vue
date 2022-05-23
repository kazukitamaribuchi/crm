<template>
    <div>
        <b-modal
            v-model="dialog"
            size="lg"
            screenable
            title="顧客入力"
            header-bg-variant="dark"
            header-text-variant="light"
            ok-title="登録"
            cancel-title="閉じる"
            @ok="register"
            :ok-disabled=isDisabled
            @cancel="close"
        >
            <b-form class="create_customer_form">
                <b-container fluid>
                    <b-row>
                        <b-col cols="3">
                            <b-form-group
                                label="会員No"
                            >
                                <b-input-group>
                                    <b-form-input
                                        v-model="createCustomerData.customer_no"
                                        type="text"
                                        placeholder="会員No"
                                        required
                                    ></b-form-input>
                                </b-input-group>
                            </b-form-group>
                        </b-col>
                        <b-col cols="5">
                        </b-col>
                        <b-col cols="4">
                            <b-form-group
                                label="来店日"
                            >
                                <b-form-datepicker
                                    v-model="createCustomerData.first_visit"
                                    placeholder="来店日を選択してください"
                                ></b-form-datepicker>
                            </b-form-group>
                        </b-col>
                    </b-row>
                    <b-card class="mt-4" bg-variant="light">
                        <b-card-title>
                            顧客情報
                        </b-card-title>
                        <b-row class="mb-0 pb-0 mt-0 pt-0">
                            <b-col cols="12" class="mb-1 pb-0">
                                <b-form-group
                                    label="名前"
                                >
                                    <b-input-group>
                                        <b-form-input
                                            v-model="createCustomerData.name"
                                            type="text"
                                            placeholder="名前"
                                            required
                                        ></b-form-input>
                                    </b-input-group>
                                </b-form-group>
                            </b-col>
                        </b-row>
                        <b-row class="mt-0 pt-0">
                            <b-col cols="12" class="mt-0 pt-0">
                                <b-form-group>
                                    <b-input-group>
                                        <b-form-input
                                            v-model="createCustomerData.name_kana"
                                            type="text"
                                            placeholder="名前(カナ)"
                                        ></b-form-input>
                                    </b-input-group>
                                </b-form-group>
                            </b-col>
                        </b-row>
                        <b-row>
                            <b-col cols="4">
                                <b-form-group
                                    label="年齢"
                                >
                                    <b-input-group>
                                        <b-form-input
                                            v-model="createCustomerData.age"
                                            type="number"
                                            placeholder="年齢"
                                        ></b-form-input>
                                    </b-input-group>
                                </b-form-group>
                            </b-col>
                        </b-row>
                        <b-row>
                            <b-col cols="12">
                                <b-form-group
                                    label="誕生日"
                                >
                                    <b-input-group>
                                        <b-form-input
                                            v-model="createCustomerData.birthday_year"
                                            type="text"
                                            placeholder="YYYY"
                                        ></b-form-input>
                                        <b-form-input
                                            v-model="createCustomerData.birthday_month"
                                            type="text"
                                            placeholder="MM"
                                        ></b-form-input>
                                        <b-form-input
                                            v-model="createCustomerData.birthday_day"
                                            type="text"
                                            placeholder="DD"
                                        ></b-form-input>
                                    </b-input-group>
                                </b-form-group>
                            </b-col>
                        </b-row>
                        <b-row>
                            <b-col cols="5">
                                <b-form-group
                                    label="職業"
                                >
                                    <b-input-group>
                                        <b-form-input
                                            v-model="createCustomerData.job"
                                            type="text"
                                            placeholder="職業"
                                        ></b-form-input>
                                    </b-input-group>
                                </b-form-group>
                            </b-col>
                        </b-row>
                        <b-row>
                            <b-col cols="12">
                                <b-form-group
                                    label="会社"
                                >
                                    <b-input-group>
                                        <b-form-input
                                            v-model="createCustomerData.company"
                                            type="text"
                                            placeholder="会社"
                                        ></b-form-input>
                                    </b-input-group>
                                </b-form-group>
                            </b-col>
                        </b-row>
                        <b-row>
                            <b-form-group
                                label="要注意人物"
                            >
                                <b-form-checkbox
                                    v-model="createCustomerData.caution_flg"
                                ></b-form-checkbox>
                            </b-form-group>
                        </b-row>
                        <b-row>
                            <b-col cols="12">
                                <b-form-group
                                    label="備考"
                                >
                                    <b-form-textarea
                                        rows="2"
                                        no-resize
                                        v-model="createCustomerData.remark"
                                    ></b-form-textarea>
                                </b-form-group>
                            </b-col>
                        </b-row>
                    </b-card>
                </b-container>
            </b-form>
        </b-modal>
    </div>
</template>

<script>
import { mapMutations } from 'vuex'
import { Const } from '@/assets/js/const'
const Con = new Const()
import moment from 'moment'

export default {
    name: 'CreateCustomerDialogItem',
    props: {
    },
    data: () => ({
        createCustomerData: {
        },
        year: Con.SELECT_BIRTHDAY_YEAR,
        dialog: false,
    }),
    computed: {
        isDisabled () {
            if (this.createCustomerData.name
                && this.createCustomerData.customer_no) {
                return false
            }
            return true
        },
        today () {
            const today = moment()
            return today.format("YYYY-MM-DD")
        }
    },
    created () {
        this.createCustomerData.first_visit = this.today
    },
    methods: {
        ...mapMutations([
            'addCustomerList',
        ]),
        register () {
            console.log('register', this.createCustomerData)
            const data = this.createCustomerData
            const birthday = [data.birthday_year, data.birthday_month, data.birthday_day].join('/')
            this.$axios({
                method: 'POST',
                url: '/api/customer/',
                data: {
                    name: data.name,
                    name_kana: data.name_kana,
                    age: data.age,
                    birthday_str: birthday,
                    job: data.job,
                    company: data.company,
                    customer_no: data.customer_no,
                    // ランクは最初から上位で作る事も許容させるか? => マスタでやらせる。
                    rank_id: 1,
                }
            })
            .then(res => {
                console.log(res)
                this.addCustomerList(res)
                this.init()
            })
            .catch(e => {
                console.log(e)
            })
        },
        init () {
            this.createCustomerData = {
                first_visit: this.today
            }
            // this.createCustomerData.first_visit = this.today
        },
        close () {
            this.init()
            this.dialog = false
        },
        open () {
            this.dialog = true
        }
    }
}

</script>

<style lang="scss" scoped>
    .create_customer_form {
        .input-group-text {
            height: 100%;
            border-radius: 5px 0 0 5px !important;
        }
    }
</style>
