<template>
    <div>
        <vs-table
            :data="booking"
        >
            <template slot="header">
                <h3>
                    予約一覧
                </h3>
            </template>
            <template slot="thead">
                <vs-th>
                    顧客名
                </vs-th>
                <vs-th>
                    予約人数
                </vs-th>
                <vs-th>
                    時間
                </vs-th>
                <vs-th>
                    座席
                </vs-th>
                <vs-th>
                    担当
                </vs-th>
            </template>
            <template slot-scope="{data}">
                <vs-tr :data="tr" :key="indextr" v-for="(tr, indextr) in data">
                    <vs-td>
                        {{ tr.customer.name }}
                    </vs-td>
                    <vs-td>
                        {{ tr.total_person }}
                    </vs-td>
                    <vs-td>
                        {{ tr.booking_start }}
                    </vs-td>
                    <vs-td>
                        {{ tr.seat.seat_type }}
                    </vs-td>
                    <vs-td>
                        {{ tr.cast[0].name }}
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
    name: 'BookingListItem',
    data: () => ({
    }),
    computed: {
        ...mapGetters([
            'booking'
        ]),
    },
    created () {
        this.getBookingList()
        .then(res => {
            this.setBookingList(res)
        })
    },
    mounted () {
        console.log('this.booking', this.booking)
    },
    methods: {
        ...mapMutations([
            'setBookingList',
        ]),
        ...mapActions([
            'getBookingList',
        ])
    }
}
</script>
