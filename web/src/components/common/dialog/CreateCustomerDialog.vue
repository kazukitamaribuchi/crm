<template>
    <v-dialog
        v-model="localcreateCustomerDialog"
        max-width="800px"
        transition="dialog-bottom-transition"
    >
        <v-card>
            <v-card-title
                id="login-title"
            >
                顧客登録
            </v-card-title>

            <v-container fluid class="form-wrap">
                <v-row>
                    <v-col cols="4">
                        <vs-input
                            v-model="createCustomerData.customer_no"
                            placeholder="会員No"
                            label="会員No"
                        ></vs-input>
                    </v-col>
                </v-row>
                <v-row>
                    <v-col cols="12">
                        <vs-input
                            v-model="createCustomerData.name"
                            placeholder="お名前"
                            label="お名前"
                        ></vs-input>
                    </v-col>
                </v-row>
                <v-row>
                    <v-col cols="12">
                        <vs-input
                            v-model="createCustomerData.name_kana"
                            placeholder="お名前（フリガナ）"
                            label="お名前（フリガナ）"
                        ></vs-input>
                    </v-col>
                </v-row>

                <v-row>
                    <v-col cols="4">
                        <vs-input
                            v-model="createCustomerData.birthday_year"
                            placeholder="年"
                            label="誕生日"
                        ></vs-input>
                    </v-col>
                    <v-col cols="4" class="mt-6">
                        <vs-input
                            v-model="createCustomerData.birthday_month"
                            placeholder="月"
                        ></vs-input>
                    </v-col>
                    <v-col cols="4" class="mt-6">
                        <vs-input
                            v-model="createCustomerData.birthday_day"
                            placeholder="日"
                        ></vs-input>
                    </v-col>
                </v-row>

                <v-row>
                    <v-col cols="3">
                        <vs-input
                            v-model="createCustomerData.age"
                            placeholder="年齢"
                            label="年齢"
                        ></vs-input>
                    </v-col>
                </v-row>

                <v-row>
                    <v-col cols="12">
                        <vs-input
                            v-model="createCustomerData.job"
                            placeholder="職業"
                            label="職業"
                        ></vs-input>
                    </v-col>
                </v-row>

                <v-row>
                    <v-col cols="12">
                        <vs-input
                            v-model="createCustomerData.company"
                            placeholder="会社"
                            label="会社"
                        ></vs-input>
                    </v-col>
                </v-row>

                <v-row>
                    <v-spacer/>
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
                            @click="localcreateCustomerDialog = false"
                        >閉じる</vs-button>
                    </v-card-actions>
                </v-row>
            </v-container>
        </v-card>
    </v-dialog>
</template>

<script>
import { mapMutations } from 'vuex'
import { Const } from '@/assets/js/const'
const Con = new Const()

export default {
    name: 'CreateCustomerDialogItem',
    props: {
        createCustomerDialog: {
            type: Boolean,
            required: true,
        },
    },
    data: () => ({
        createCustomerData: {},
        year: Con.SELECT_BIRTHDAY_YEAR,

    }),
    computed: {
        localcreateCustomerDialog: {
            get: function () {
                return this.createCustomerDialog
            },
            set: function (value) {
                this.$emit('update', value)
            },
        },
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
                    // ランクは最初から上位で作る事も許容させるか？
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
            this.createCustomerData = {}
            this.localcreateCustomerDialog = false
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

</style>
