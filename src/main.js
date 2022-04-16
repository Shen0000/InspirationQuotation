import { createApp } from 'vue'
import {createStore} from 'vuex'
import App from './App.vue'
import router from './router'
import vSelect from 'vue-select'
import '../node_modules/vue-select/dist/vue-select.css'
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
app.component("v-select", vSelect)
