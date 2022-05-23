<template>
    <div id="cast_list_wrap">
        <b-row>
            <b-col cols="5">
                <b-card class="cast_list_1">
                </b-card>
            </b-col>
            <b-col>
                <b-card class="cast_list_2">
                </b-card>
            </b-col>
        </b-row>
        <b-row>
            <b-col cols="6">
                <b-card class="cast_list_3">
                </b-card>
            </b-col>
            <b-col cols="2">
                <b-card class="cast_list_4">
                </b-card>
            </b-col>
            <b-col>
                <b-card class="cast_list_5">
                </b-card>
            </b-col>
        </b-row>
    </div>
</template>

<script>
import { mapGetters, mapMutations, mapActions } from 'vuex'

export default {
    name: 'CastListItem',
    data: () => ({
    }),
    computed: {
        ...mapGetters([
            'cast'
        ]),
    },
    created () {
        this.getCastList()
        .then(res => {
            this.setCastList(res)
        })
    },
    mounted () {
        console.log('this.cast', this.cast)
    },
    methods: {
        ...mapMutations([
            'setCastList',
        ]),
        ...mapActions([
            'getCastList',
        ])
    }
}
</script>

<style lang="scss" scoped>
    #cast_list_wrap {
        // background-color: $theme-color;
        // background-color: white;
        margin-top: $main-top-margin;
        margin-left: $main-top-side-margin;
        margin-right: $main-top-side-margin;
        height: $main-height;
        padding: 20px;

        .cast_list_1 {
            background-color: $theme-color;
            height: 25rem;
        }
        .cast_list_2 {
            background-color: $theme-color;
            height: 25rem;
        }
        .cast_list_3 {
            background-color: $theme-color;
            height: 25rem;
        }
        .cast_list_4 {
            background-color: $theme-color;
            height: 25rem;
        }
        .cast_list_5 {
            background-color: $theme-color;
            height: 25rem;
        }
    }
</style>
