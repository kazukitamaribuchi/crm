import { Customer } from '@/views/index'
import { CustomerList, CustomerDetail } from '@/components/index'

const routes = {
    path: '/customer',
    component: Customer,
    children: [
        {
            path: '',
            name: 'CustomerList',
            component: CustomerList,
            meta: {
                title: 'CustomerListDao'
            }
        },
        {
            path: ':id',
            name: 'CustomerDetail',
            component: CustomerDetail,
            meta: {
                title: 'CustomerDetailDao'
            }
        }
    ]
}

export default routes
