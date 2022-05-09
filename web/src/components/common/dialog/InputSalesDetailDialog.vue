<template>
    <v-dialog
        v-model="localInputSalesDetailDialog"
        max-width="1200px"
        transition="dialog-bottom-transition"
        fullscreen
    >
        <v-card>
            <v-card-title
                id="login-title"
            >
                明細入力
            </v-card-title>

            <v-container fluid class="form-wrap">
                <v-row>
                    <v-col cols="2">
                        <v-list>
                            <v-list-item
                                class="base_service"
                                @click="showBaseService"
                            >
                                <v-list-item-icon>
                                    <v-icon>
                                        mdi-information-outline
                                    </v-icon>
                                </v-list-item-icon>
                                <v-list-item-content>
                                    <v-list-item-title>
                                        基本料金
                                    </v-list-item-title>
                                </v-list-item-content>
                            </v-list-item>
                            <v-list-group
                                v-for="item in items"
                                :key="item.title"
                                v-model="item.active"
                                :prepend-icon="item.action"
                                no-action
                            >
                                <template v-slot:activator>
                                    <v-list-item-content>
                                        <v-list-item-title v-text="item.title">
                                        </v-list-item-title>
                                    </v-list-item-content>
                                </template>
                                <v-list-item
                                    v-for="child in item.items"
                                    :key="child.title"
                                    :class="`service_${child.category}_${child.id}`"
                                >
                                    <v-list-item-content>
                                        <v-list-item-title v-text="child.title"></v-list-item-title>
                                    </v-list-item-content>
                                </v-list-item>
                            </v-list-group>
                        </v-list>
                    </v-col>
                    <v-col cols="10">
                        content
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
                            @click="localInputSalesDetailDialog = false"
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
    name: 'InputSalesDetailDialogItem',
    props: {
        inputSalesDetailDialog: {
            type: Boolean,
            required: true,
        },
    },
    data: () => ({
        inputSalesDetailData: {},
        items: [
            {
                action: 'mdi-glass-cocktail',
                active: true,
                items: [
                    {
                        id: 1,
                        category: 'drink',
                        title: 'アルコール',
                    },
                    {
                        id: 2,
                        category: 'drink',
                        title: 'ノンアルコール'
                    },
                    {
                        id: 3,
                        category: 'drink',
                        title: 'ソフトドリンク'
                    },
                ],
                title: 'お酒',
                },
            {
                action: 'mdi-food',
                items: [
                    {
                        id: 1,
                        category: 'food',
                        title: 'おつまみ'
                    },
                    {
                        id: 2,
                        category: 'food',
                        title: 'デザート'
                    },
                ],
                title: '食べ物',
            },
        ]
    }),
    computed: {
        localInputSalesDetailDialog: {
            get: function () {
                return this.inputSalesDetailDialog
            },
            set: function (value) {
                this.$emit('update', value)
            },
        },
    },
    methods: {
        ...mapMutations([
        ]),
        register () {
            console.log('register', this.inputSalesDetailData)
            const data = this.inputSalesDetailData
        },
        init () {
            this.inputSalesDetailData = {}
            this.localInputSalesDetailDialog = false
        },
        showBaseService () {
            console.log('showBase')
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

.base_service {
    cursor: pointer;
}

.base_service:hover {
    background-color: rgba(200,200,200,0.2);
    transition: 0.5s;
}

.service_drink_1,
.service_drink_2,
.service_drink_3,
.service_food_1,
.service_food_2 {
    cursor: pointer;
}
.service_drink_1:hover,
.service_drink_2:hover,
.service_drink_3:hover,
.service_food_1:hover,
.service_food_2:hover {
    background-color: rgba(200,200,200,0.2);
    transition: 0.5s;
}

</style>
