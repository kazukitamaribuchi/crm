<template>
    <v-dialog
        v-model="dialog"
        max-width="1000px"
    >
        <v-card>
            <v-card-title
                id="login-title"
            >
                顧客登録
            </v-card-title>

            <v-container fluid class="form-wrap">
                <v-row>
                    <v-col cols="6">
                        <v-card
                            flat
                        >
                            <v-row>
                                <v-col cols="4">
                                    <vs-input
                                        v-model="updateCustomerData.customer_no"
                                        placeholder="会員No"
                                        label="会員No"
                                    ></vs-input>
                                </v-col>
                            </v-row>
                            <v-row>
                                <v-col cols="12">
                                    <vs-input
                                        v-model="updateCustomerData.name"
                                        placeholder="お名前"
                                        label="お名前"
                                    ></vs-input>
                                </v-col>
                            </v-row>
                            <v-row>
                                <v-col cols="12">
                                    <vs-input
                                        v-model="updateCustomerData.name_kana"
                                        placeholder="お名前（フリガナ）"
                                        label="お名前（フリガナ）"
                                    ></vs-input>
                                </v-col>
                            </v-row>

                            <v-row>
                                <v-col cols="4">
                                    <vs-input
                                        v-model="updateCustomerData.birthday_year"
                                        placeholder="年"
                                        label="誕生日"
                                    ></vs-input>
                                </v-col>
                                <v-col cols="4" class="mt-6">
                                    <vs-input
                                        v-model="updateCustomerData.birthday_month"
                                        placeholder="月"
                                    ></vs-input>
                                </v-col>
                                <v-col cols="4" class="mt-6">
                                    <vs-input
                                        v-model="updateCustomerData.birthday_day"
                                        placeholder="日"
                                    ></vs-input>
                                </v-col>
                            </v-row>

                            <v-row>
                                <v-col cols="3">
                                    <vs-input
                                        v-model="updateCustomerData.age"
                                        placeholder="年齢"
                                        label="年齢"
                                    ></vs-input>
                                </v-col>
                            </v-row>

                            <v-row>
                                <v-col cols="12">
                                    <vs-input
                                        v-model="updateCustomerData.job"
                                        placeholder="職業"
                                        label="職業"
                                    ></vs-input>
                                </v-col>
                            </v-row>

                            <v-row>
                                <v-col cols="12">
                                    <vs-input
                                        v-model="updateCustomerData.company"
                                        placeholder="会社"
                                        label="会社"
                                    ></vs-input>
                                </v-col>
                            </v-row>
                        </v-card>
                    </v-col>
                    <v-col cols="6">
                        <v-card
                            flat
                            class="edit-customer-dialog-right"
                        >
                            <v-row>
                                <v-col cols="4">
                                    <vs-input
                                        v-model="updateCustomerData.first_visit_year"
                                        placeholder="年"
                                        label="初回来店日"
                                    ></vs-input>
                                </v-col>
                                <v-col cols="4" class="mt-6">
                                    <vs-input
                                        v-model="updateCustomerData.first_visit_month"
                                        placeholder="月"
                                    ></vs-input>
                                </v-col>
                                <v-col cols="4" class="mt-6">
                                    <vs-input
                                        v-model="updateCustomerData.first_visit_day"
                                        placeholder="日"
                                    ></vs-input>
                                </v-col>
                            </v-row>

                            <!-- こんぽーねんとかしてselectでvalueはint -->
                            <v-row>
                                <v-col cols="12">
                                    <vs-input
                                        v-model="updateCustomerData.rank_id"
                                        label="ランク"
                                    ></vs-input>
                                </v-col>
                            </v-row>

                        </v-card>
                    </v-col>
                </v-row>
                <v-row>
                    <v-spacer/>
                    <v-card-actions>
                        <vs-button
                            color="primary"
                            type="filled"
                            icon="done"
                            @click="update"
                        >更新</vs-button>
                        <vs-button
                            color="primary"
                            type="border"
                            icon="done"
                            @click="dialog = false"
                        >閉じる</vs-button>
                    </v-card-actions>
                </v-row>
            </v-container>
        </v-card>
    </v-dialog>
</template>

<script>
import _ from 'lodash'
import { mapMutations } from 'vuex'
import { Const } from '@/assets/js/const'
const Con = new Const()

export default {
    name: 'EreateCustomerDialogItem',
    props: {
    },
    data: () => ({
        dialog: false,
        customer: {},
        updateCustomerData: {},
    }),
    computed: {
        localEditCustomerDialog: {
            get: function () {
                return this.createCustomerDialog
            },
            set: function (value) {
                this.$emit('update', value)
            },
        },
    },
    methods: {
        open (customer) {
            this.customer = _.cloneDeep(customer)
            let updateCustomerData = _.cloneDeep(customer)
            const birthday_array = updateCustomerData.birthday.split('/')
            updateCustomerData.birthday_year = birthday_array[0]
            updateCustomerData.birthday_month = birthday_array[1]
            updateCustomerData.birthday_day = birthday_array[2]
            delete updateCustomerData.birthday
            // const first_visit_array = updateCustomerData.first_visit.split('-')
            // updateCustomerData.first_visit_year = first_visit_array[0]
            // updateCustomerData.first_visit_month = first_visit_array[1]
            // updateCustomerData.first_visit_day = first_visit_array[2]
            // delete updateCustomerData.first_visit
            this.updateCustomerData = updateCustomerData
            this.dialog = true
        },
        close () {
            this.customer = {}
            this.updateCustomerData = {}
            this.dialog = false
        },
        update () {
            const data = this.updateCustomerData
            const birthday = [data.birthday_year, data.birthday_month, data.birthday_day].join('/')
            console.log(data)

            this.close()
            this.$axios({
                url: `/api/customer/${this.$route.params['id']}/`,
                method: 'PUT',
                data: {
                    id: this.$route.params['id'],
                    name: data.name,
                    name_kana: data.name_kana,
                    age: data.age,
                    birthday_str: birthday,
                    job: data.job,
                    company: data.company,
                    customer_no: data.customer_no,
                    first_visit: data.first_visit,
                    rank_id: 1,
                }
            })
            .then(res => {
                console.log(res)
                this.$emit('update', res.data)
                this.close()
            })
            .catch(e => {
                console.log(e)
            })
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

.edit-customer-dialog-right {
    padding-top: 86px;
}

</style>
