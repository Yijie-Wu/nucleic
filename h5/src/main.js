import Vue from 'vue'
import App from './App.vue'
import Vant from 'vant';
import 'vant/lib/index.css';
import axios from 'axios'
import './styles/theme.less';
import dayjs from 'dayjs'
Vue.prototype.$http = axios
Vue.prototype.$bus = new Vue()
Vue.prototype.$dayjs = dayjs
import {router} from './router'

Vue.config.productionTip = false
import store from './store'
Vue.use(Vant)

const whiteList = ['/login','/person', '/qrcode'] 
router.beforeEach(async(to, from, next) => {
    const hasToken = window.sessionStorage.getItem('Authorization') 
    // console.log(hasToken)
    if (hasToken) {
        if (to.path === '/login') {
          // if is logged in, redirect to the home page
          next({ path: '/' })
        } else {
            next()
        }
    } else {
        if (whiteList.indexOf(to.path) !== -1) {
            // in the free login whitelist, go directly
            next()
          } else {
            // other pages that do not have permission to access are redirected to the login page.
            next('/login')
          }
    }
})

new Vue({
  el: '#app',
  router,
  store,
  render: h => h(App),
})
