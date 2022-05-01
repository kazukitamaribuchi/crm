import { Bottle } from '@/views/index'
import { BottleList } from '@/components/index'

const routes = {
    path: '/bottle',
    name: 'Bottle',
    component: Bottle,
    children: [
        {
            path: '',
            name: 'BottleList',
            component: BottleList,
            meta: {
                title: 'BottleListDao'
            }
        }
    ]
}

export default routes
