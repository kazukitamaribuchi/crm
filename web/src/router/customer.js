import { Customer } from '@/views/index'
import { CustomerList } from '@/components/index'

const routes = {
    path: '/customer',
    name: 'Customer',
    component: Customer,
    children: [
        {
            path: '',
            name: 'CustomerList',
            component: CustomerList,
            meta: {
                title: 'CustomerListDao'
            }
        }
    ]
}

export default routes
