<template>
    <v-dialog
        v-model="dialog"
        max-width="400px"
    >
        <v-card>
            <v-card-title
            >
                会員No検索
            </v-card-title>

            <v-container fluid class="form-wrap">
                <v-row>
                    <v-col cols="12">
                        <vs-input
                            v-model="customer_no"
                            placeholder="会員No"
                            label="会員No"
                        ></vs-input>
                    </v-col>
                </v-row>
                <v-row>
                    <v-spacer/>
                    <v-card-actions>
                        <vs-button
                            color="primary"
                            type="filled"
                            icon="done"
                            @click="search"
                        >検索</vs-button>
                        <vs-button
                            color="primary"
                            type="border"
                            icon="done"
                            @click="close"
                        >閉じる</vs-button>
                    </v-card-actions>
                </v-row>
            </v-container>
        </v-card>
    </v-dialog>
</template>

<script>
import _ from 'lodash'
import { mapMutations } from 'vuex'
import { Const } from '@/assets/js/const'
const Con = new Const()

export default {
    name: 'SearchCustomerNoDialogItem',
    props: {
    },
    data: () => ({
        dialog: false,
        customer_no: '',
    }),
    computed: {
    },
    methods: {
        open () {
            this.dialog = true
        },
        close () {
            this.dialog = false
            this.customer_no = ''
        },
        search () {
            if (this.customer_no != '') {
                // 正しいcustoner_noであれば
                this.$router.push({
                    name: 'CustomerDetail',
                    params: {
                        id: this.customer_no
                    }
                })
                this.$router.go({
                    path: this.$router.currentRoute.path,
                    force: true
                })
            }
            this.close()
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

.edit-customer-dialog-right {
    padding-top: 86px;
}

</style>
