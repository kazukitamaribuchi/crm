<template>
    <div>
        <b-card-title>
            {{ categoryTitle }}
        </b-card-title>
        <b-list-group horizontal>
            <b-list-group-item
                v-for="(item, id) in categoryList"
                :key=id
                button
                variant="dark"
                class="header_menu"
                @click="filterProductCategory(item)"
            >
                {{ item.text }}
            </b-list-group-item>
        </b-list-group>
    </div>
</template>

<script>
import { Const } from '@/assets/js/const'
import _ from 'lodash'
const Con = new Const()

export default {
    name: 'ListViewItem',
    props: {
        productType: {
            type: Number,
            required: true,
            default: 0,
        },
    },
    data: () => ({
        alcoholHeader: [
            { text: 'シャンパン', largeCategory: 1, middleCategory: 0, smallCategory: 0 },
            { text: 'ワイン', largeCategory: 1, middleCategory: 0, smallCategory: 1 },
            { text: '焼酎', largeCategory: 1, middleCategory: 0, smallCategory: 2 },
            { text: 'サワー', largeCategory: 1, middleCategory: 0, smallCategory: 3 },
            { text: 'カクテル', largeCategory: 1, middleCategory: 0, smallCategory: 4 },
            { text: '日本酒', largeCategory: 1, middleCategory: 0, smallCategory: 5 },
            { text: 'ビール', largeCategory: 1, middleCategory: 0, smallCategory: 6 },
        ],
        nonAlcoholHeader: [
            { text: 'ノンアルコール', largeCategory: 1, middleCategory: 1, smallCategory: 0 }
        ],
        softDrinkHeader: [
            { text: 'ソフトドリンク', largeCategory: 1, middleCategory: 2, smallCategory: 0 }
        ],
        mainHeader: [
            { text: 'メイン', largeCategory: 2, middleCategory: 0, smallCategory: 0 },
            // { text: '和食' },
            // { text: '洋食' },
            // { text: 'ファストフード' },
        ],
        otumamiHeader: [
            { text: 'おつまみ', largeCategory: 2, middleCategory: 1, smallCategory: 0 }
        ],
        saradaHeader: [
            { text: 'サラダ', largeCategory: 2, middleCategory: 2, smallCategory: 0 }
        ],
        dezartHeader: [
            { text: 'デザート', largeCategory: 2, middleCategory: 3, smallCategory: 0 }
        ],
        categoryTitleList: {
            0: 'アルコール',
            1: 'ノンアルコール',
            2: 'ソフトドリンク',
            3: 'メイン',
            4: 'おつまみ',
            5: 'サラダ',
            6: 'デザート',
        },
    }),
    computed: {
        categoryTitle () {
            return this.categoryTitleList[this.productType]
        },
        categoryList () {
            switch (this.productType) {
                case 0:
                    return this.alcoholHeader
                case 1:
                    return this.nonAlcoholHeader
                case 2:
                    return this.softDrinkHeader
                case 3:
                    return this.mainHeader
                case 4:
                    return this.otumamiHeader
                case 5:
                    return this.saradaHeader
                case 6:
                    return this.dezartHeader
                default:
                    return []
            }
        }
    },
    methods: {
        filterProductCategory (item) {
            this.$eventHub.$emit('filterProductCategory', item)
        }
    }
}

</script>

<style lang="scss" scoped>
    .header_menu {
        color: white;
        background-color: rgba(70, 70, 70, 0.7);
        text-align: center;
        border: 1px solid white;

        // ぼこっと出す？
        // border: 1px solid #838383;
        // box-shadow: 1px 1px 1px rgba(101, 101, 101, 0.7);
    }
</style>
