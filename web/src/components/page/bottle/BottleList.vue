<template>
    <div id="bottle_list_wrap">
        <b-row>
            <b-col cols="4">
                <b-card class="bottle_list_1">
                </b-card>
            </b-col>
            <b-col>
                <b-card class="bottle_list_2">
                </b-card>
            </b-col>
            <b-col>
                <b-card class="bottle_list_2">
                </b-card>
            </b-col>
        </b-row>
        <b-row>
            <b-col cols="8">
                <b-card class="bottle_list_3">
                </b-card>
            </b-col>
            <b-col>
                <b-card class="bottle_list_5">
                </b-card>
            </b-col>
        </b-row>
    </div>
</template>

<script>
import { mapGetters, mapMutations, mapActions } from 'vuex'

export default {
    name: 'BottleListItem',
    data: () => ({
    }),
    computed: {
        ...mapGetters([
            'bottle'
        ]),
    },
    created () {
        this.getBottleList()
        .then(res => {
            this.setBottleList(res)
        })
    },
    mounted () {
        console.log('this.bottle', this.bottle)
    },
    methods: {
        ...mapMutations([
            'setBottleList',
        ]),
        ...mapActions([
            'getBottleList',
        ])
    }
}
</script>

<style lang="scss" scoped>
    #bottle_list_wrap {
        // background-color: $theme-color;
        // background-color: white;
        margin-top: $main-top-margin;
        margin-left: $main-top-side-margin;
        margin-right: $main-top-side-margin;
        height: $main-height;
        padding: 20px;

        .bottle_list_1 {
            background-color: $theme-color;
            height: 25rem;
        }
        .bottle_list_2 {
            background-color: $theme-color;
            height: 25rem;
        }
        .bottle_list_3 {
            background-color: $theme-color;
            height: 25rem;
        }
        .bottle_list_4 {
            background-color: $theme-color;
            height: 25rem;
        }
        .bottle_list_5 {
            background-color: $theme-color;
            height: 25rem;
        }
    }
</style>
