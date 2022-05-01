import { Sales } from '@/views/index'
import { SalesList } from '@/components/index'

const routes = {
    path: '/sales',
    name: 'Sales',
    component: Sales,
    children: [
        {
            path: '',
            name: 'SalesList',
            component: SalesList,
            meta: {
                title: 'SalesListDao'
            }
        }
    ]
}

export default routes
