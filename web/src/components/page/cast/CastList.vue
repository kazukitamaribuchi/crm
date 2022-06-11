<template>
    <div id="cast_list_wrap">
        <b-row>
            <b-tabs pill card>
                <b-tab
                    title="管理画面"
                    :active=topActive
                    @click="setCastTopActive(0)"
                >
                </b-tab>
                <b-tab
                    title="キャスト一覧"
                    :active=!topActive
                    @click="setCastTopActive(1)"
                >
                    <!-- <b-card class="cast_list_area"> -->

                        <b-row>
                            <b-col
                                cols="3"
                                v-for="item in filterdCast"
                                :key=item.id
                            >
                                <b-card
                                    @click="showCastDetail"
                                    style="cursor: pointer;"
                                >
                                <!-- bg-variant="dark"
                                text-variant="white" -->
                                    <b-row>
                                        <b-col cols="6">
                                            <img
                                                src="@/assets/img/女性11.jpg"
                                                class="cast_list_area_cast_icon"
                                                top
                                            >
                                        </b-col>
                                        <b-col cols="5" align="right">
                                            <b-card-title class="mt-4">
                                                {{ item.name }}
                                            </b-card-title>
                                            <b-card-sub-title>
                                                {{ item.age }}
                                            </b-card-sub-title>
                                        </b-col>
                                        <b-col></b-col>
                                    </b-row>
                                </b-card>
                            </b-col>
                        </b-row>
                    <!-- </b-card> -->
                </b-tab>
            </b-tabs>
        </b-row>
    </div>
</template>

<script>
import { mapGetters, mapMutations, mapActions } from 'vuex'
import _ from 'lodash'
import dayjs from 'dayjs'
import isBetween from 'dayjs/plugin/isBetween';
import isSameOrAfter from 'dayjs/plugin/isSameOrAfter';
import isSameOrBefore from 'dayjs/plugin/isSameOrBefore';
dayjs.extend(isSameOrAfter)
dayjs.extend(isSameOrBefore)
dayjs.extend(isBetween)

export default {
    name: 'CastListItem',
    data: () => ({
        filterdCast: [],
        searchWord: '',
        defaultIcon: 'http://localhost:8000/media/upload/女性1111.png',
        apiPath: 'http://localhost:8000',
    }),
    computed: {
        ...mapGetters([
            'cast',
            'castTopActive',
        ]),
        topActive () {
            if (this.castTopActive == undefined || this.castTopActive == 0) {
                return true
            }
            return false
        }
    },
    created () {
        this.getCastList()
        .then(res => {
            this.setCastList(res)
            this.filterdCast = _.cloneDeep(res.data)
        })
    },
    mounted () {
        console.log('this.cast', this.cast)
    },
    methods: {
        ...mapMutations([
            'setCastList',
            'setCastTopActive',
        ]),
        ...mapActions([
            'getCastList',
        ]),
        showCastDetail () {

        },
    }
}
</script>

<style lang="scss" scoped>
    #cast_list_wrap {
        margin-top: $main-top-margin;
        margin-left: $main-top-side-margin;
        margin-right: $main-top-side-margin;
        height: $main-height;
        padding: 20px;

        .cast_list_area {
            background-color: $theme-color;
            // color: white;

        }
        .cast_list_area_cast_icon {
            border-radius: 50%;
            width: 140px;
            height: 140px;
            // box-shadow: 1px 1px 2px 1px rgba(100, 100, 100, 0.5);
            // border: 1px solid rgba(100, 100, 100, 0.3);
        }

    }
    .card-header {
        background-color: $theme-color !important;
        border-bottom: 0px !important;
    }
</style>
