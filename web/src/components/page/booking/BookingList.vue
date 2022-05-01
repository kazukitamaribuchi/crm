<template>
    <div>bookingList</div>
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
