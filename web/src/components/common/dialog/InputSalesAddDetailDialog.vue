<template>
    <b-modal
        v-model="dialog"
        title="明細追加"
        header-bg-variant="secondary"
        header-text-variant="light"
        ok-title="追加"
        cancel-title="閉じる"
        size="xl"
    >
        <!-- <b-row>
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
        </b-row> -->
        <b-row>
            <b-col cols="2">
                <b-list-group>
                    <b-list-group-item
                        button
                        @click="showTopPopularProduct"
                    >
                        TOP
                    </b-list-group-item>
                    <label
                        v-for="(head, id) in siderbaritems"
                        :key=id
                        button
                        class="mt-3"
                    >
                        {{ head.text }}
                        <b-list-group-item
                            v-for="(item, idx) in head.items"
                            :key=idx
                            button
                            @click="selectProductCategory(item)"
                        >
                            {{ item.text }}
                        </b-list-group-item>
                    </label>
                </b-list-group>
            </b-col>
            <b-col v-if="selectedProductType == null">
                <b-card-title>
                    人気商品
                </b-card-title>
                <b-row>
                    <b-col
                        cols="2"
                        v-for="item in popularProductTestData"
                        :key=item.id
                    >
                        <b-card
                            class="productCard"
                            @click="selectProduct(item)"
                        >
                            <b-card-img
                                :src="apiPath + item.thumbnail"
                                alt="productImage"
                                top
                                height="100px"
                                v-if="item.thumbnail != null"
                            ></b-card-img>
                            <b-card-img
                                :src="defaultIcon"
                                alt="productImage"
                                top
                                height="100px"
                                v-else
                            ></b-card-img>
                            <b-card-text>
                                {{ item.name }}
                            </b-card-text>
                        </b-card>
                    </b-col>
                </b-row>
            </b-col>
            <b-col v-if="selectedProductType != null">
                <!-- <b-card-title>
                    カテゴリ毎
                </b-card-title> -->
                <InputSalesAddDetailDialogHeader
                    :productType=selectedProductType
                />
                <b-row>
                    <b-col
                        cols="2"
                        v-for="item in productByCategoryTestData"
                        :key=item.id
                    >
                        <b-card
                            class="productCard"
                            @click="selectProduct(item)"
                        >
                            <b-card-img
                                :src="apiPath + item.thumbnail"
                                alt="productImage"
                                top
                                height="100px"
                                v-if="item.thumbnail != null"
                            ></b-card-img>
                            <b-card-img
                                :src="defaultIcon"
                                alt="productImage"
                                top
                                height="100px"
                                v-else
                            ></b-card-img>
                            <b-card-text>
                                {{ item.name }}
                            </b-card-text>
                        </b-card>
                    </b-col>
                </b-row>
            </b-col>
        </b-row>
        <template #modal-footer>
            <b-container fluid>
            <b-row>
                <b-col cols="4" class="add_sales_detail_footer_col">
                    <b-card-sub-title>選択商品</b-card-sub-title>
                    <div class="selected_product_area">
                        <b v-if="selectedProduct != null">
                            <b-img
                                v-if="selectedProduct.thumbnail != null"
                                :src="apiPath + selectedProduct.thumbnail"
                                alt="Selected Product"
                                rounded
                                height="50"
                                width="50"
                            ></b-img>
                            <b-img
                                v-else
                                :src="defaultIcon"
                                alt="Selected Product"
                                rounded
                                height="50"
                                width="50"
                            ></b-img>
                        </b>
                        <span v-if="selectedProduct != null">{{ selectedProduct.name }}</span>
                        <span v-else> - </span>
                    </div>
                </b-col>
                <b-col cols="8" class="add_sales_detail_footer_col">
                    <b-row>
                        <b-col cols="3" class="add_sales_detail_footer_col">
                            <b-card-sub-title>定価</b-card-sub-title>
                            <div class="selected_product_area">
                                <div v-if="selectedProduct != null">
                                    ￥{{ selectedProduct.price }}
                                </div>
                                <div v-else> - </div>
                            </div>
                        </b-col>
                        <b-col cols="1" class="add_sales_detail_footer_col">
                            <b-card-sub-title>個数</b-card-sub-title>
                            <b-form-group>
                                <b-form-group
                                    class="add_sales_detail_quantity_wrap"
                                >
                                    <b-form-select
                                        v-model="quantity"
                                        :options="quantityOptions"
                                        value-field="value"
                                        text-field="text"
                                        class="add_sales_detail_quantity"
                                    ></b-form-select>
                                </b-form-group>
                            </b-form-group>
                        </b-col>
                        <b-col cols="1" class="add_sales_detail_footer_col">
                            <b-card-sub-title>税率</b-card-sub-title>
                            <b-form-group>
                                <b-form-group
                                    class="add_sales_detail_tax_wrap"
                                >
                                    <b-form-select
                                        v-model="tax"
                                        :options="taxOptions"
                                        value-field="value"
                                        text-field="text"
                                        class="add_sales_detail_tax"
                                    ></b-form-select>
                                </b-form-group>
                            </b-form-group>
                        </b-col>
                        <b-col cols="4" class="add_sales_detail_footer_col">
                            <b-card-sub-title>実価格</b-card-sub-title>
                            <b-form-input
                                v-model="actuallyPrice"
                                type="number"
                                placeholder="実価格"
                                required
                            ></b-form-input>
                        </b-col>
                        <b-col align="center" class="add_sales_detail_footer_col">
                            <b-card-sub-title>ボトル登録</b-card-sub-title>
                            <b-form-group>
                                <b-form-checkbox-group
                                    v-model="isBottle"
                                    :options=bottleOptions
                                    buttons
                                    :disabled=!isDrink
                                ></b-form-checkbox-group>
                            </b-form-group>
                        </b-col>
                    </b-row>
                </b-col>
            </b-row>
            <b-row class="pt-3">
                <b-col cols="5" class="add_sales_detail_footer_col">
                    <b-card-sub-title>備考</b-card-sub-title>
                    <b-form-textarea
                        rows="2"
                        no-resize
                        v-model="remark"
                    ></b-form-textarea>
                </b-col>
            </b-row>
            <b-row class="add_cast_footer_bottom_area mt-5">
                <b-col cols="2">
                    <b-card-sub-title>
                        総計(税抜)
                    </b-card-sub-title>
                    <b-card-title class="mb-0">
                        ￥ {{ totalPrice }}
                    </b-card-title>
                </b-col>
                <b-col cols="2">
                    <b-card-sub-title>
                        総計(税込)
                    </b-card-sub-title>
                    <b-card-title class="mb-0">
                        ￥ {{ totalTaxPrice }}
                    </b-card-title>
                </b-col>
                <b-col align="right" class="add_sales_detail_footer_col">
                    <b-button
                        variant="secondary"
                        @click="close"
                        class="btn_close add_sales_detail_footer_area4"
                    >
                        閉じる
                    </b-button>
                    <b-button
                        variant="primary"
                        @click="add"
                        class="add_sales_detail_footer_area4"
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
import InputSalesAddDetailDialogHeader from '@/components/parts/InputSalesAddDetailDialogHeader'
import Decimal from 'decimal.js'

export default {
    name: 'InputSalesAddDetailDialogItem',
    props: {
        // appointed: {
        //     type: Array,
        //     required: true,
        //     default: () => ([])
        // },
    },
    components: {
        InputSalesAddDetailDialogHeader,
    },
    data: () => ({
        dialog: false,
        selected: {},
        filterdCast: [],
        searchWord: '',
        appointedCastId: new Set(),
        isBottle: [],
        quantity: 1,
        actuallyPrice: 0,
        bottleOptions: [
            { text: '登録', value: 1 }
        ],
        appointOptions: [
            { text: '指名', value: 0 },
            { text: '本指名', value: 1 },
            { text: '場内指名', value: 2 },
        ],
        quantityOptions: [
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
        taxOptions: [
            { value: 30, text: '30' },
            { value: 0, text: '0' },
        ],
        siderbaritems: [
            {
                text: '飲み物',
                items: [
                    { text: 'アルコール', productType: 0 },
                    { text: 'ノンアルコール', productType: 1 },
                    { text: 'ソフトドリンク', productType: 2 },
                ]
            },
            {
                text: '食べ物',
                items: [
                    { text: 'メイン', productType: 3 },
                    { text: 'おつまみ', productType: 4 },
                    { text: 'サラダ', productType: 5 },
                    { text: 'デザート', productType: 6 },
                ]
            },
        ],
        selectedProductType: null,
        popularProductTestData: [
            {
                name: 'NOT BOTTLE',
                price: '20000',
                thumbnail: '/media/upload/酒2.png',
                category: {
                    large_category: 0,
                    middle_category: 0,
                }
            },
            {
                name: 'NOT BOTTLE',
                price: '20000',
                thumbnail: '/media/upload/酒2.png',
                category: {
                    large_category: 1,
                    middle_category: 1,
                }
            },
            {
                name: 'KRUG',
                price: '20000',
                thumbnail: '/media/upload/酒2.png',
                category: {
                    large_category: 1,
                    middle_category: 0,
                }
            },
            {
                name: 'KRUG',
                price: '20000',
                thumbnail: '/media/upload/酒2.png',
                category: {
                    large_category: 1,
                    middle_category: 0,
                }
            },
            {
                name: 'KRUG',
                price: '20000',
                thumbnail: '/media/upload/酒2.png',
                category: {
                    large_category: 1,
                    middle_category: 0,
                }
            },
            {
                name: 'KRUG',
                price: '20000',
                thumbnail: '/media/upload/酒2.png',
                category: {
                    large_category: 1,
                    middle_category: 0,
                }
            },
            {
                name: 'KRUG',
                price: '20000',
                thumbnail: '/media/upload/酒2.png',
                category: {
                    large_category: 1,
                    middle_category: 0,
                }
            },
            {
                name: 'KRUG',
                price: '20000',
                thumbnail: '/media/upload/酒2.png',
                category: {
                    large_category: 1,
                    middle_category: 0,
                }
            },
            {
                name: 'KRUG',
                price: '20000',
                thumbnail: '/media/upload/酒2.png',
                category: {
                    large_category: 1,
                    middle_category: 0,
                }
            },
            {
                name: 'KRUG',
                price: '20000',
                thumbnail: '/media/upload/酒2.png',
                category: {
                    large_category: 1,
                    middle_category: 0,
                }
            },
            {
                name: 'KRUG',
                price: '20000',
                thumbnail: '/media/upload/酒2.png',
                category: {
                    large_category: 1,
                    middle_category: 0,
                }
            },
            {
                name: 'KRUG',
                price: '20000',
                thumbnail: '/media/upload/酒2.png',
                category: {
                    large_category: 1,
                    middle_category: 0,
                }
            },
        ],
        defaultIcon: 'http://localhost:8000/media/upload/酒2.png',
        productByCategoryTestData: [
            {
                name: '侍',
                price: '20000',
                thumbnail: '/media/upload/酒1.jpg',
                category: {
                    large_category: 1,
                    middle_category: 0,
                }
            },
            {
                name: 'KRUG',
                price: '20000',
                thumbnail: '/media/upload/酒2.png',
                category: {
                    large_category: 1,
                    middle_category: 0,
                }
            },
            {
                name: '侍',
                price: '20000',
                thumbnail: '/media/upload/酒2.png',
                category: {
                    large_category: 1,
                    middle_category: 0,
                }
            },
            {
                name: 'KRUG',
                price: '20000',
                thumbnail: '/media/upload/酒2.png',
                category: {
                    large_category: 1,
                    middle_category: 0,
                }
            },
            {
                name: '侍',
                price: '20000',
                thumbnail: '/media/upload/酒2.png',
                category: {
                    large_category: 1,
                    middle_category: 0,
                }
            },
            {
                name: 'KRUG',
                price: '20000',
                thumbnail: '/media/upload/酒2.png',
                category: {
                    large_category: 1,
                    middle_category: 0,
                }
            },
            {
                name: '侍',
                price: '20000',
                thumbnail: '/media/upload/酒2.png',
                category: {
                    large_category: 1,
                    middle_category: 0,
                }
            },
            {
                name: '侍',
                price: '20000',
                thumbnail: '/media/upload/酒1.jpg',
                category: {
                    large_category: 1,
                    middle_category: 0,
                }
            },
            {
                name: 'KRUG',
                price: '20000',
                thumbnail: '/media/upload/酒2.png',
                category: {
                    large_category: 1,
                    middle_category: 0,
                }
            },
            {
                name: '侍',
                price: '20000',
                thumbnail: '/media/upload/酒2.png',
                category: {
                    large_category: 1,
                    middle_category: 0,
                }
            },
            {
                name: 'KRUG',
                price: '20000',
                thumbnail: '/media/upload/酒2.png',
                category: {
                    large_category: 1,
                    middle_category: 0,
                }
            },
            {
                name: '侍',
                price: '20000',
                thumbnail: '/media/upload/酒2.png',
                category: {
                    large_category: 1,
                    middle_category: 0,
                }
            },
        ],
        topProductTestData: {
            0: [
                {
                    name: '侍',
                    price: '20000',
                    thumbnail: '/media/upload/酒1.jpg',
                    category: {
                        large_category: 1,
                        middle_category: 0,
                    }
                },
                {
                    name: 'KRUG',
                    price: '20000',
                    thumbnail: '/media/upload/酒2.png',
                    category: {
                        large_category: 1,
                        middle_category: 0,
                    }
                },
                {
                    name: '侍',
                    price: '20000',
                    thumbnail: '/media/upload/酒2.png',
                    category: {
                        large_category: 1,
                        middle_category: 0,
                    }
                },
            ],
            1: [
                {
                    name: 'ノンアルコールトップ',
                    price: '20000',
                    thumbnail: '/media/upload/酒1.jpg',
                    category: {
                        large_category: 1,
                        middle_category: 0,
                    }
                },
            ],
            2: [
                {
                    name: 'ソフトドリンクトップ',
                    price: '20000',
                    thumbnail: '/media/upload/酒1.jpg',
                    category: {
                        large_category: 1,
                        middle_category: 0,
                    }
                },
                {
                    name: 'ソフトドリンクトップ2',
                    price: '20000',
                    thumbnail: '/media/upload/酒2.png',
                    category: {
                        large_category: 1,
                        middle_category: 0,
                    }
                },
                {
                    name: 'ソフトドリンクトップ3',
                    price: '20000',
                    thumbnail: '/media/upload/酒2.png',
                    category: {
                        large_category: 1,
                        middle_category: 0,
                    }
                },
            ],
            3: [
                {
                    name: 'メインフードトップ',
                    price: '20000',
                    thumbnail: '/media/upload/酒1.jpg',
                    category: {
                        large_category: 1,
                        middle_category: 0,
                    }
                },
                {
                    name: 'メインフードトップ2',
                    price: '20000',
                    thumbnail: '/media/upload/酒2.png',
                    category: {
                        large_category: 1,
                        middle_category: 0,
                    }
                },
            ],
            4: [
                {
                    name: 'おつまみトプ',
                    price: '20000',
                    thumbnail: '/media/upload/酒2.png',
                    category: {
                        large_category: 1,
                        middle_category: 0,
                    }
                },
            ],
            5: [
                {
                    name: 'サラダトプ',
                    price: '20000',
                    thumbnail: '/media/upload/酒2.png',
                    category: {
                        large_category: 1,
                        middle_category: 0,
                    }
                },
            ],
            6: [
                {
                    name: 'デザートトップ',
                    price: '20000',
                    thumbnail: '/media/upload/酒2.png',
                    category: {
                        large_category: 1,
                        middle_category: 0,
                    }
                },
            ],
            100: [
                {
                    name: 'TOP not bottle',
                    price: '20000',
                    thumbnail: '/media/upload/酒2.png',
                    category: {
                        large_category: 0,
                        middle_category: 0,
                    }
                },
                {
                    name: 'NOT BOTTLE',
                    price: '20000',
                    thumbnail: '/media/upload/酒2.png',
                    category: {
                        large_category: 1,
                        middle_category: 1,
                    }
                },
                {
                    name: 'KRUG',
                    price: '20000',
                    thumbnail: '/media/upload/酒2.png',
                    category: {
                        large_category: 1,
                        middle_category: 0,
                    }
                },
                {
                    name: 'KRUG',
                    price: '20000',
                    thumbnail: '/media/upload/酒2.png',
                    category: {
                        large_category: 1,
                        middle_category: 0,
                    }
                },
                {
                    name: 'KRUG',
                    price: '20000',
                    thumbnail: '/media/upload/酒2.png',
                    category: {
                        large_category: 1,
                        middle_category: 0,
                    }
                },
                {
                    name: 'KRUG',
                    price: '20000',
                    thumbnail: '/media/upload/酒2.png',
                    category: {
                        large_category: 1,
                        middle_category: 0,
                    }
                },
                {
                    name: 'KRUG',
                    price: '20000',
                    thumbnail: '/media/upload/酒2.png',
                    category: {
                        large_category: 1,
                        middle_category: 0,
                    }
                },
                {
                    name: 'KRUG',
                    price: '20000',
                    thumbnail: '/media/upload/酒2.png',
                    category: {
                        large_category: 1,
                        middle_category: 0,
                    }
                },
                {
                    name: 'KRUG',
                    price: '20000',
                    thumbnail: '/media/upload/酒2.png',
                    category: {
                        large_category: 1,
                        middle_category: 0,
                    }
                },
                {
                    name: 'KRUG',
                    price: '20000',
                    thumbnail: '/media/upload/酒2.png',
                    category: {
                        large_category: 1,
                        middle_category: 0,
                    }
                },
                {
                    name: 'KRUG',
                    price: '20000',
                    thumbnail: '/media/upload/酒2.png',
                    category: {
                        large_category: 1,
                        middle_category: 0,
                    }
                },
                {
                    name: 'KRUG',
                    price: '20000',
                    thumbnail: '/media/upload/酒2.png',
                    category: {
                        large_category: 1,
                        middle_category: 0,
                    }
                },
            ]
        },
        selectedProduct: null,
        remark: '',
        tax: 30,
        apiPath: 'http://localhost:8000',
    }),
    computed: {
        ...mapGetters([
            'cast',
            // ↓人気商品、カテゴリ別の商品を取るようにする
            'product',
            'productByCategory',
        ]),
        isDisabled () {
            return this.selectedProduct == null
        },
        isDrink () {
            if (this.selectedProduct == null) return false
            if (this.selectedProduct.category.large_category == 1
                && this.selectedProduct.category.middle_category == 0) {
                return true
            }
            return false
        },
        totalPrice () {
            if (this.selectedProduct == null) return 0
            const quantity = new Decimal(this.quantity)
            return Math.ceil(quantity.times(this.actuallyPrice).toNumber())
        },
        totalTaxPrice () {
            if (this.selectedProduct == null) return 0
            const tax_rate = new Decimal(this.tax / 100)
            return Math.ceil(tax_rate.times(this.totalPrice).toNumber() + this.totalPrice)
        },
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
        this.$eventHub.$off('filterProductCategory')
        this.$eventHub.$on('filterProductCategory', this.filterProductCategory)

        // console.log(this.cast)
        // this.filterdCast = _.cloneDeep(this.cast)
        console.log(this.product)
        console.log(this.productByCategory)
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
            // const data = {
            //     product: this.selectedProduct,
            //     tax: this.tax,
            //     actually_price: this.actuallyPrice,
            //     bottle: this.isBottle.length != 0,
            //     total_price: this.totalPrice,
            //     total_tax_price: this.totalTaxPrice,
            // }
            const product = this.selectedProduct

            const data = {
                name: product.name,
                price: product.price,
                actually_price: this.actuallyPrice,
                tax_rate: this.tax,
                quantity: this.quantity,
                total_price: this.totalPrice,
                total_tax_price: this.totalTaxPrice,
                bottle: this.isBottle.length != 0,
                thumbnail: product.thumbnail,
                category: product.category,
            }
            console.log(this.selectedProduct)
            // console.log(data)
            this.$eventHub.$emit('addSalesDetail', data)
            this.close()
        },
        init () {
            this.selected = {}
            this.filterdCast = {}
            this.searchWord = ''
            this.appointedCastId = new Set()
            this.selectedProductType = null
            this.selectedProduct = null
            this.remark = ''
            this.actuallyPrice = 0
            this.isBottle = []
            this.quantity = 1
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
        selectProductCategory (item) {
            this.productByCategoryTestData = this.topProductTestData[item.productType]
            this.selectedProductType = item.productType
        },
        selectProduct (item) {
            this.selectedProduct = item
            this.actuallyPrice = item.price
            if (!this.isDrink) {
                this.isBottle = []
            }
        },
        filterProductCategory (data) {
            const large = data.largeCategory
            const middle = data.middleCategory
            const small = data.smallCategory
            const res = this.productByCategory[large][middle][small]
            this.productByCategoryTestData = _.cloneDeep(res)
        },
        showTopPopularProduct () {
            this.selectedProductType = null
        }
    },
}

</script>

<style lang="scss" scoped>

.input-group-text {
    height: 100%;
    border-radius: 5px 0 0 5px !important;
}

.productCard {
    cursor: pointer;
}

.productCard:hover {
    box-shadow: 1px 1px 2px 1px rgba(150, 150, 150, 0.5);
}

.add_sales_detail_footer_col {
    margin: 0;
    padding: 0;
}

.btn_close {
    display: inline-block;
    margin-right: 8px;
}

.selected_product_area {
    margin-top: 2px;
    min-height: 50px;
}

.add_cast_footer_area3 {
    display: inline-block;
}

.add_sales_detail_quantity, .add_sales_detail_tax {
    height: 38px;
    padding: 4px 9px;
    border-radius: 3px;
    border: 1px solid rgba(125, 125, 125, 0.6);
}


.add_sales_detail_footer_area4 {
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
