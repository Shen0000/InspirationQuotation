import { createRouter, createWebHistory } from 'vue-router'
import Login from "../views/Login.vue"
import Home from "../views/Home.vue"
import Signup from "../views/Signup.vue"
import Quotes from "../views/Quotes.vue"

const routes = [
    {
        path: "/",
        name: "Home",
        component: Home, 
    },
    {
        path: "/login",
        name: "Login",
        component: Login
    },
    {
        path: "/signup",
        name: "Signup",
        component: Signup
    },
    {
        path: '/quotes',
        name: "Quotes",
        component: Quotes
    }

]
const router = createRouter({
    history: createWebHistory(),
    routes
  })
export default router