import { createRouter, createWebHistory } from "vue-router";
import Login from "../views/Login.vue";
import Home from "../views/Home.vue";
import Signup from "../views/Signup.vue";
import Quotes from "../views/Quotes.vue";
import Settings from "../views/Settings.vue";
import DailyQuote from "../views/DailyQuote.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/login",
    name: "Login",
    component: Login,
  },
  {
    path: "/signup",
    name: "Signup",
    component: Signup,
  },
  {
    path: "/quotes",
    name: "Quotes",
    component: Quotes,
  },
  {
    path: "/settings",
    name: "Settings",
    component: Settings,
    meta: {
      requiresAuth: true,
    },
  },
  {
    path: "/daily",
    name: "DailyQuote",
    component: DailyQuote,
    meta: {
      requiresAuth: true,
    },
  },
];
const router = createRouter({
  history: createWebHistory(),
  routes,
});
export default router;
