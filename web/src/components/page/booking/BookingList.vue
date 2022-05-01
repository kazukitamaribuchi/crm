<template>
    <div>bookingList</div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
    name: 'BookingListItem',
    data: () => ({
    }),
    created () {
        this.getBookingList()
    },
    methods: {
        ...mapActions([
            'getBookingList',
        ])
    }
}
</script>
