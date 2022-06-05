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
                            <b-col>
                                <b-form-group
                                    label="Q&A1"
                                >
                                    <span class="basic_select_wrap">
                                        <b-form-select
                                            v-model="createCastData.question_one"
                                            :options=qanda
                                            value-field="value"
                                            text-field="text"
                                            class="basic_select"
                                        >
                                            <template #first>
                                                <b-form-select-option :value="null" disabled>質問を選択してください</b-form-select-option>
                                            </template>
                                        </b-form-select>
                                    </span>
                                    <b-input-group>
                                        <b-form-input
                                            v-model="createCastData.answer_one"
                                            type="text"
                                            placeholder="回答を入力してください"
                                            required
                                        ></b-form-input>
                                    </b-input-group>
                                </b-form-group>
                            </b-col>
                            <b-col>
                                <b-form-group
                                    label="Q&A2"
                                >
                                    <span class="basic_select_wrap">
                                        <b-form-select
                                            v-model="createCastData.question_two"
                                            :options=qanda
                                            value-field="value"
                                            text-field="text"
                                            class="basic_select"
                                        >
                                            <template #first>
                                                <b-form-select-option :value="null" disabled>質問を選択してください</b-form-select-option>
                                            </template>
                                        </b-form-select>
                                    </span>
                                    <b-input-group>
                                        <b-form-input
                                            v-model="createCastData.answer_two"
                                            type="text"
                                            placeholder="回答を入力してください"
                                            required
                                        ></b-form-input>
                                    </b-input-group>
                                </b-form-group>
                            </b-col>
                            <b-col>
                                <b-form-group
                                    label="Q&A3"
                                >
                                    <span class="basic_select_wrap">
                                        <b-form-select
                                            v-model="createCastData.question_three"
                                            :options=qanda
                                            value-field="value"
                                            text-field="text"
                                            class="basic_select"
                                        >
                                            <template #first>
                                                <b-form-select-option :value="null" disabled>質問を選択してください</b-form-select-option>
                                            </template>
                                        </b-form-select>
                                    </span>
                                    <b-input-group>
                                        <b-form-input
                                            v-model="createCastData.answer_three"
                                            type="text"
                                            placeholder="回答を入力してください"
                                            required
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
import { mapGetters, mapMutations } from 'vuex'
import { Const } from '@/assets/js/const'
const Con = new Const()

export default {
    name: 'CreateCastDialogItem',
    props: {
    },
    data: () => ({
        createCastData: {
            question_one: null,
            question_two: null,
            question_three: null,
        },
        year: Con.SELECT_BIRTHDAY_YEAR,
        dialog: false,
    }),
    computed: {
        ...mapGetters([
            'question',
        ]),
        isDisabled () {
            return true
        },
        // 質問内容の絞り込み（後で
        qanda () {
            return this.question
        },
    },
    created () {
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
    .basic_select_wrap {
        width: 100%;
        display: grid;
        .basic_select {
            background: white;
            border-radius: 4px;
            border: 1px solid rgba(125, 125, 125, 0.4);
            padding: 6px 20px 6px 7px;
            font-size: 16px;
            font-weight: 200;
            width: 100%;
        }
    }

    .basic_select_wrap::after {
        border-left: 4px solid transparent;
        border-right: 4px solid transparent;
        border-top: 4.5px solid rgba(50, 50, 50, 1);
        content: "";
        position: relative;
        // right: 12px;
        // top: 13px;
        right: -315px;
        top: -18px;
        width: 0;
    }
</style>
