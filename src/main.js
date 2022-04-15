import { createApp } from 'vue'
import {createStore} from 'vuex'
import App from './App.vue'
import router from './router'
import './components/firebaseInit'


const store = createStore({
   state() {
      return {
         loggedIn: false,
         uid: "",
         username: ""
      }
   },
   mutations: {
      setLogin (state, loginStatus) {
         state.loggedIn = loginStatus
      },
      setUsername(state, username) {
         state.username = username;
      }
   }
})
const app = createApp(App)
app.use(router)
app.use(store)
app.mount('#app')
