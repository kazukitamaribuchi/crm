import { Home, Login } from '@/views/index'

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home,
    },
    {
        path: '/login',
        name: 'Login',
        components: Login,
    }
]

export default routes
