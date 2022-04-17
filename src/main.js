import { createApp } from 'vue'
import {createStore} from 'vuex'
import App from './App.vue'
import router from './router'
import vSelect from 'vue-select'
import VueToast from 'vue-toast-notification';
import 'vue-toast-notification/dist/theme-sugar.css';
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
app.use(VueToast, {
   position: 'top',
   duration: 2000,
});
app.mount('#app')
app.component("v-select", vSelect)
