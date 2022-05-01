<template>
    <div>attendanceList</div>
</template>

<script>
import { mapGetters, mapMutations, mapActions } from 'vuex'

export default {
    name: 'AttendanceListItem',
    data: () => ({
    }),
    computed: {
        ...mapGetters([
            'attendance'
        ]),
    },
    created () {
        this.getAttendanceList()
        .then(res => {
            this.setAttendanceList(res)
        })
    },
    mounted () {
        console.log('this.attendance', this.attendance)
    },
    methods: {
        ...mapMutations([
            'setAttendanceList',
        ]),
        ...mapActions([
            'getAttendanceList',
        ])
    }
}
</script>
