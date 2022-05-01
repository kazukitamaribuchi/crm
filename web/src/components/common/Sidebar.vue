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
    </v-container>
</template>

<script>
export default {
    name: 'SidebarItem',
    data: () => ({
        active: false,
        menus: [
            {
                title: '顧客管理',
                icon: 'bx bxs-user-badge',
                // icon: 'bx bxs-user',
                style: 'color:#914240',
                link: 'CustomerList',
            },
            {
                title: '売上管理',
                icon: 'bx bx-calculator',
                style: 'color:#757733',
                link: 'SalesList',
            },
            {
                title: '勤怠管理',
                icon: 'bx bxs-calendar',
                style: 'color:#657733',
                link: 'AttendanceList',
            },
            {
                title: 'キャスト管理',
                icon: 'bx bx-user',
                style: 'color:#657733',
                link: 'CastList',
            },
            {
                title: '予約管理',
                icon: 'bx bxs-book',
                style: 'color:#657733',
                link: 'BookingList',
            },
            {
                title: 'ボトル管理',
                icon: 'bx bxs-drink',
                style: 'color:#657733',
                link: 'BottleList',
            },
        ]
    }),
    methods: {
        toPage (item) {
            this.$router.push({name: item.link})
        }
    }
}
</script>
