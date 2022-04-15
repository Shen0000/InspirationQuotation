import { createRouter, createWebHistory } from 'vue-router'
import Login from "../views/Login.vue"
import Home from "../views/Home.vue"
import Signup from "../views/Signup.vue"

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
    }

]
const router = createRouter({
    history: createWebHistory(),
    routes
  })
export default router