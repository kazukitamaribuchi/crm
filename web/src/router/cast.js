import { Cast } from '@/views/index'
import { CastList } from '@/components/index'

const routes = {
    path: '/cast',
    name: 'Cast',
    component: Cast,
    children: [
        {
            path: '',
            name: 'CastList',
            component: CastList,
            meta: {
                title: 'CastListDao'
            }
        }
    ]
}

export default routes
