<template>
    <v-container
        id="attendance-wrap"
        fluid
    >
        <vs-row vs-w="12">
            <Header/>
        </vs-row>
        <vs-row vs-w="12">
            <vs-col vs-w="2">
                <Sidebar/>
            </vs-col>
            <vs-col vs-w="10">
                <router-view/>
            </vs-col>
        </vs-row>
    </v-container>
</template>

<script>
import Header from '@/components/common/Header'
import Sidebar from '@/components/common/Sidebar'

export default {
    name: 'AttendanceItem',
    data: () => ({
    }),
    components: {
        Header,
        Sidebar,
    }
}
</script>

<style lang="scss" scoped>
#attendance-wrap {
    padding: 0;
}
</style>
