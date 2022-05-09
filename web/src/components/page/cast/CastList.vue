<template>
    <div>
        <vs-table
            :data="cast"
        >
            <template slot="header">
                <h3>
                    キャスト一覧
                </h3>
            </template>
            <template slot="thead">
                <vs-th>
                    名前
                </vs-th>
                <vs-th>
                    年齢
                </vs-th>
                <vs-th>
                    本名
                </vs-th>
                <vs-th>
                    実年齢
                </vs-th>
                <vs-th>
                    誕生日
                </vs-th>
                <vs-th>
                    勤務開始日
                </vs-th>
            </template>
            <template slot-scope="{data}">
                <vs-tr :data="tr" :key="indextr" v-for="(tr, indextr) in data">
                    <vs-td>
                        {{ tr.name }}
                    </vs-td>
                    <vs-td>
                        {{ tr.age }}
                    </vs-td>
                    <vs-td>
                        {{ tr.real_name }}
                    </vs-td>
                    <vs-td>
                        {{ tr.real_age }}
                    </vs-td>
                    <vs-td>
                        {{ tr.birthday }}
                    </vs-td>
                    <vs-td>
                        {{ tr.start_working_date }}
                    </vs-td>
                </vs-tr>
            </template>
            <template slot="expand">

            </template>
        </vs-table>
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
