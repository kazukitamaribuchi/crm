<template>
    <b-modal
        v-model="dialog"
        title="キャスト追加"
        header-bg-variant="secondary"
        header-text-variant="light"
        ok-title="追加"
        cancel-title="閉じる"
        size="lg"
    >
        <b-row>
            <b-col cols="6">
                <b-input-group>
                    <b-input-group-prepend is-text>
                        <b-icon icon="search"></b-icon>
                    </b-input-group-prepend>
                    <b-form-input
                        v-model="searchWord"
                        type="text"
                        placeholder="キャスト名で検索"
                    ></b-form-input>
                </b-input-group>
            </b-col>
            <b-col cols="6" align="right">
                <b-button
                    variant="outline-primary"
                >
                    <b-icon
                        icon="filter"
                    ></b-icon>
                </b-button>
            </b-col>
        </b-row>
        <b-row>
            <b-col
                cols="3"
                v-for="item in filterdCast"
                :key=item.id
            >
                <b-card
                    class="addCastCard"
                    @click="select(item)"
                    :class="{'isAppointed': isAppointed(item)}"
                >
                    <b-card-img
                        :src="apiPath + item.icon"
                        alt="castImage"
                        top
                        height="100px"
                        :class="{'isAppointed': isAppointed(item)}"
                        v-if="item.icon != null"
                    ></b-card-img>
                    <b-card-img
                        :src="defaultIcon"
                        alt="castImage"
                        top
                        height="100px"
                        :class="{'isAppointed': isAppointed(item)}"
                        v-else
                    ></b-card-img>
                    <b-card-text>
                        {{ item.name }} ({{ item.age }})
                        <!-- <span><small>{{ getIsAppointedStr(item) }}</small></span> -->
                    </b-card-text>
                </b-card>
            </b-col>
        </b-row>
        <template #modal-footer>
            <b-container fluid>
            <b-row>
                <b-col cols="3" class="add_cast_footer_col">
                    <b-card-sub-title>選択キャスト</b-card-sub-title>
                    <div class="selected_cast_area">
                        <b-avatar :src="apiPath + selected.icon" v-if="selected.icon != null"></b-avatar>
                        <b-avatar :src="defaultIcon" v-else></b-avatar>
                        <span v-if="Object.keys(selected).length">{{ selected.name }}</span>
                        <span v-else> - </span>
                    </div>
                </b-col>
                <b-col cols="9" class="add_cast_footer_col">
                    <b-row align="center">
                        <b-col cols="7" class="add_cast_footer_col">
                            <b-card-sub-title>指名タイプ</b-card-sub-title>
                            <b-form-group>
                                <b-form-radio-group
                                    v-model="appointType"
                                    :options=appointOptions
                                    buttons
                                ></b-form-radio-group>
                            </b-form-group>
                        </b-col>
                        <b-col class="add_cast_footer_col">
                            <b-card-sub-title>同伴出勤</b-card-sub-title>
                            <b-form-group>
                                <b-form-checkbox-group
                                    v-model="isDouhan"
                                    :options=douhanOptions
                                    buttons
                                    @change="douhanClick"
                                ></b-form-checkbox-group>
                            </b-form-group>
                        </b-col>
                        <b-col class="add_cast_footer_col">
                            <b-card-sub-title>滞在時間</b-card-sub-title>
                            <b-form-group
                                class="add_cast_stay_hour_wrap"
                            >
                                <b-form-select
                                    v-model="stayHour"
                                    :options="stayHourOptions"
                                    stayHourOptions
                                    value-field="value"
                                    text-field="text"
                                    class="add_cast_stay_hour"
                                ></b-form-select>
                            </b-form-group>
                        </b-col>
                    </b-row>
                </b-col>
            </b-row>
            <b-row class="add_cast_footer_bottom_area mt-5">
                <b-col align="right" class="add_cast_footer_col">
                    <b-button
                        variant="secondary"
                        @click="close"
                        class="btn_close add_cast_footer_area4"
                    >
                        閉じる
                    </b-button>
                    <b-button
                        variant="primary"
                        @click="add"
                        class="add_cast_footer_area4"
                        :disabled=isDisabled
                    >
                        追加
                    </b-button>
                </b-col>
            </b-row>
            </b-container>
        </template>
    </b-modal>
</template>

<script>
import _ from 'lodash'
import { mapGetters } from 'vuex'
import { Const } from '@/assets/js/const'
const Con = new Const()

export default {
    name: 'InputSalesAddCastDialogItem',
    props: {
        appointed: {
            type: Array,
            required: true,
            default: () => ([])
        },
    },
    data: () => ({
        dialog: false,
        selected: {},
        filterdCast: [],
        searchWord: '',
        appointType: 0,
        appointedCastId: new Set(),
        isDouhan: [],
        stayHour: 0,
        douhanOptions: [
            { text: '同伴', value: 1 }
        ],
        appointOptions: [
            { text: '指名', value: 0 },
            { text: '本指名', value: 1 },
            { text: '場内指名', value: 2 },
        ],
        stayHourOptions: [
            { value: 0, text: 'full' },
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
        defaultIcon: 'http://localhost:8000/media/upload/女性1111.png',
        apiPath: 'http://localhost:8000',
    }),
    computed: {
        ...mapGetters([
            'cast',
        ]),
        isDisabled () {
            if (this.isEmptyObject(this.selected)) return true
            return false
        }
    },
    watch: {
        searchWord: function (val) {
            if (val.length > 0) {
                this.search(val)
            } else {
                // このメソッドは重くないか?
                this.filterdCast = _.cloneDeep(this.cast)
            }
        }
    },
    created () {
        // console.log(this.cast)
        // this.filterdCast = _.cloneDeep(this.cast)
    },
    methods: {
        open () {
            this.dialog = true
            this.filterdCast = _.cloneDeep(this.cast)
            this.appointedCastId = new Set()
            for (const i in this.appointed) {
                const item = this.appointed[i]
                this.appointedCastId.add(item.cast.id)
            }
        },
        close () {
            this.dialog = false
            this.init()
        },
        add () {
            const castData = {
                cast: this.selected,
                appointType: this.appointType,
                isDouhan: this.isDouhan.length !== 0,
                stayHour: this.stayHour,
            }
            this.$eventHub.$emit('addCast', castData)
            this.close()
        },
        init () {
            this.selected = {}
            this.filterdCast = {}
            this.searchWord = ''
            this.appointType = 0
            this.isDouhan = []
            this.stayHour = 0
            this.appointedCastId = new Set()
            this.errorMsg = []
        },
        select (item) {
            if (this.isAppointed(item)) return
            this.selected = item
        },
        search: _.debounce(function search (searchText) {
            const targetCastList = _.cloneDeep(this.cast)
            const reg = new RegExp("^" + searchText)
            const res = targetCastList.filter(target => {
                // 検索に本名は含める？・・・
                if (target.name.match(reg) || target.real_name.match(reg)) {
                    return true
                }
            }, 4000)
            this.filterdCast = res
        }),
        getIsAppointedStr (cast) {
            if (this.isAppointed(cast)) return '選択済み'
            return ''
        },
        isAppointed (cast) {
            if(this.appointedCastId.has(cast.id)) return true
            return false
        },
        isEmptyObject (obj) {
            return !Object.keys(obj).length
        },
        douhanClick () {
            if (this.isDouhan.length != 0) {
                this.appointType = 1
            }
        }
    },
}

</script>

<style lang="scss" scoped>

.input-group-text {
    height: 100%;
    border-radius: 5px 0 0 5px !important;
}

.addCastCard {
    cursor: pointer;
}

.addCastCard:hover {
    box-shadow: 1px 1px 2px 1px rgba(150, 150, 150, 0.5);
}

.add_cast_footer_col {
    margin: 0;
    padding: 0;
}

.btn_close {
    display: inline-block;
    margin-right: 8px;
}

.selected_cast_area {
    margin-top: 2px;
}

.add_cast_footer_area3 {
    display: inline-block;
}

.add_cast_stay_hour {
    height: 38px;
    padding: 4px 9px;
    border-radius: 3px;
    border: 1px solid rgba(125, 125, 125, 0.6);
}

.add_cast_footer_area4 {
    margin-top: 15px;
    margin-bottom: 13px;
}

.add_cast_footer_bottom_area {
    margin-top: 20px;
    border-top: 1px solid rgba(155, 155, 155, 0.5);
}

.isAppointed {
    background-color: rgba(255, 255, 255, 1);
    filter: opacity(30%);
}
</style>
