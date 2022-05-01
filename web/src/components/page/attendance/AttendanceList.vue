<template>
    <div>attendanceList</div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
    name: 'AttendanceListItem',
    data: () => ({
    }),
    created () {
        this.getAttendanceList()
    },
    methods: {
        ...mapActions([
            'getAttendanceList',
        ])
    }
}
</script>
