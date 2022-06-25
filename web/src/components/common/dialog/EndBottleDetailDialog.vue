<template>
    <b-modal
        v-model="dialog"
        title="ボトルデータ空状態更新"
        @ok="endBottleDetail"
        ok-title="はい"
        cancel-title="キャンセル"
    >
        {{ confirmText }}
    </b-modal>
</template>

<script>
import { mapMutations, mapActions } from 'vuex'

export default {
    name: 'EndBottleDetailDialogItem',
    props: {
    },
    data: () => ({
        dialog: false,
        bottleDetail: {},
    }),
    computed: {
        confirmText () {
            if (this.bottleDetail.end_flg) {
                return 'ボトルの空状態を更新しますか？'
            } else {
                return 'ボトルを空状態に更新しますか？'
            }
        }
    },
    methods: {
        ...mapActions([
            'endBottleListAction',
        ]),
        open (data) {
            this.dialog = true
            this.bottleDetail = data
        },
        close () {
            this.dialog = false
            this.bottleDetail = {}
        },
        endBottleDetail () {
            this.endBottleListAction(this.bottleDetail)
            this.close()
        }
    }
}

</script>

<style lang="scss" scoped>
</style>
