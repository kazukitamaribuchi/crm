import { Booking } from '@/views/index'
import { BookingList } from '@/components/index'

const routes = {
    path: '/booking',
    name: 'Booking',
    component: Booking,
    children: [
        {
            path: '',
            name: 'BookingList',
            component: BookingList,
            meta: {
                title: 'BookingListDao'
            }
        }
    ]
}

export default routes
