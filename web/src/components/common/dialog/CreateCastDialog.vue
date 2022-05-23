<template>
    <div>
        <b-modal
            v-model="dialog"
            size="xl"
            screenable
            title="キャスト入力"
            header-bg-variant="dark"
            header-text-variant="light"
            ok-title="登録"
            cancel-title="閉じる"
            @ok="register"
            :ok-disabled=isDisabled
            @cancel="close"
        >
            <b-form class="create_cast_form">
                <b-container fluid>
                    <b-card class="mt-4" bg-variant="light">
                        <b-card-title>
                            キャスト情報
                        </b-card-title>

                        <b-row class="mb-0 pb-0 mt-0 pt-0">
                            <b-col cols="12" class="mb-1 pb-0">
                                <b-form-group
                                    label="源氏名"
                                >
                                    <b-input-group>
                                        <b-form-input
                                            v-model="createCastData.name"
                                            type="text"
                                            placeholder="源氏名"
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
                                            v-model="createCastData.name_kana"
                                            type="text"
                                            placeholder="源氏名(カナ)"
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
                                            v-model="createCastData.age"
                                            type="number"
                                            placeholder="年齢"
                                        ></b-form-input>
                                    </b-input-group>
                                </b-form-group>
                            </b-col>
                        </b-row>

                        <b-row class="mb-0 pb-0">
                            <b-col cols="12" class="mb-1 pb-0">
                                <b-form-group
                                    label="本名"
                                >
                                    <b-input-group>
                                        <b-form-input
                                            v-model="createCastData.real_name"
                                            type="text"
                                            placeholder="本名"
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
                                            v-model="createCastData.real_name_kana"
                                            type="text"
                                            placeholder="本名(カナ)"
                                        ></b-form-input>
                                    </b-input-group>
                                </b-form-group>
                            </b-col>
                        </b-row>
                        <b-row>
                            <b-col cols="4">
                                <b-form-group
                                    label="実年齢"
                                >
                                    <b-input-group>
                                        <b-form-input
                                            v-model="createCastData.real_age"
                                            type="number"
                                            placeholder="実年齢"
                                        ></b-form-input>
                                    </b-input-group>
                                </b-form-group>
                            </b-col>
                        </b-row>
                        <b-row>
                            <b-col cols="4">
                                <b-form-group
                                    label="勤務開始時"
                                >
                                    <b-form-datepicker
                                        v-model="createCastData.first_visit"
                                        placeholder="勤務開始日を選択してください"
                                    ></b-form-datepicker>
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
                                            v-model="createCastData.birthday_year"
                                            type="text"
                                            placeholder="YYYY"
                                        ></b-form-input>
                                        <b-form-input
                                            v-model="createCastData.birthday_month"
                                            type="text"
                                            placeholder="MM"
                                        ></b-form-input>
                                        <b-form-input
                                            v-model="createCastData.birthday_day"
                                            type="text"
                                            placeholder="DD"
                                        ></b-form-input>
                                    </b-input-group>
                                </b-form-group>
                            </b-col>
                        </b-row>
                        <b-row>
                            <b-col cols="12">
                                <b-form-group
                                    label="顔写真"
                                    label-cols-sm="2"
                                    label-size="sm"
                                >
                                    <b-form-file
                                        id="file-small"
                                        size="sm"
                                    ></b-form-file>
                                </b-form-group>
                            </b-col>
                        </b-row>
                        <b-row>
                            <b-col cols="12">
                                <b-form-group
                                    label="住所"
                                >
                                    <b-input-group>
                                        <b-form-input
                                            v-model="createCastData.address"
                                            type="text"
                                            placeholder="住所"
                                        ></b-form-input>
                                    </b-input-group>
                                </b-form-group>
                            </b-col>
                        </b-row>
                        <b-row>
                            <b-col cols="12">
                                <b-form-group
                                    label="備考"
                                >
                                    <b-form-textarea
                                        rows="2"
                                        no-resize
                                        v-model="createCastData.remark"
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

export default {
    name: 'CreateCastDialogItem',
    props: {
    },
    data: () => ({
        createCastData: {},
        year: Con.SELECT_BIRTHDAY_YEAR,
        dialog: false,
    }),
    computed: {
        isDisabled () {
            return true
        },
    },
    methods: {
        ...mapMutations([
            'addCastList',
        ]),
        register () {
            console.log('register', this.createCastData)
        },
        init () {
            this.createCastData = {}
        },
        close () {
            this.dialog = false
            this.init()
        },
        open () {
            this.dialog = true
        }
    }
}

</script>

<style lang="scss" scoped>

</style>
