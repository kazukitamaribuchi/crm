<template>
    <v-container id="sidebar-wrap">
        <v-list>
            <v-list-item
                v-for="(menu, i) in menus"
                :key="i"
            >
                <v-btn
                    text
                    @click="toPage(menu)"
                >
                    <v-list-item-icon>
                        <i :class='menu.icon' :style='menu.style'></i>
                    </v-list-item-icon>
                    <v-list-item-title>{{ menu.title }}</v-list-item-title>
                </v-btn>
            </v-list-item>
        </v-list>

        <SearchCustomerNoDialog
            ref="searchCustomerNo"
        />
    </v-container>
</template>

<script>
import SearchCustomerNoDialog from '@/components/common/dialog/SearchCustomerNoDialog'

export default {
    name: 'SidebarItem',
    components: {
        SearchCustomerNoDialog
    },
    data: () => ({
        active: false,
        menus: [
            {
                title: '顧客管理',
                icon: 'bx bxs-user-badge',
                // icon: 'bx bxs-user',
                style: 'color:#914240',
                link: 'CustomerList',
                type: 'Page'
            },
            {
                title: '売上管理',
                icon: 'bx bx-calculator',
                style: 'color:#757733',
                link: 'SalesList',
                type: 'Page'
            },
            {
                title: '勤怠管理',
                icon: 'bx bxs-calendar',
                style: 'color:#657733',
                link: 'AttendanceList',
                type: 'Page'
            },
            {
                title: 'キャスト管理',
                icon: 'bx bx-user',
                style: 'color:#657733',
                link: 'CastList',
                type: 'Page'
            },
            {
                title: '予約管理',
                icon: 'bx bxs-book',
                style: 'color:#657733',
                link: 'BookingList',
                type: 'Page'
            },
            {
                title: 'ボトル管理',
                icon: 'bx bxs-drink',
                style: 'color:#657733',
                link: 'BottleList',
                type: 'Page'
            },
            {
                title: '顧客No検索',
                icon: 'bx bx-search-alt-2',
                style: 'color:#914240',
                ref: 'searchCustomerNo',
                type: 'Dialog'
            }
        ]
    }),
    methods: {
        toPage (item) {
            if (item.type == 'Dialog') {
                this.$refs[item.ref].open()
            } else {
                this.$router.push({name: item.link})
            }
        }
    }
}
</script>
