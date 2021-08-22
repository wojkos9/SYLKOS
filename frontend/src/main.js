import Vue from 'vue'
import App from './App.vue'
import MenuIcon from 'vue-material-design-icons/Menu.vue';
import VueMdijs from 'vue-mdijs'
// import { mdiMagnify } from '@mdi/js'
import { mdiArrowRightBoldCircleOutline } from '@mdi/js';
import { MdButton, MdContent, MdTabs, MdIcon, MdToolbar, MdDrawer, MdList, MdCard, MdField, MdMenu  } from 'vue-material/dist/components'
import 'vue-material/dist/vue-material.min.css'
import 'vue-material/dist/theme/default.css'
import VueRouter from 'vue-router'
import { routes } from './router/index.js'
import moment from 'moment';

Vue.config.productionTip = false
Vue.component('menu-icon', MenuIcon);
VueMdijs.add({ mdiPlusThick, mdiMinusThick, mdiSend, mdiChevronLeft, mdiChevronRight })
Vue.use(VueMdijs)
Vue.component(mdiArrowRightBoldCircleOutline)
Vue.use(MdButton)
Vue.use(MdContent)
Vue.use(MdTabs)
Vue.use(MdIcon)
Vue.use(MdToolbar)
Vue.use(MdDrawer)
Vue.use(MdList)
Vue.use(MdCard)
Vue.use(MdField)
Vue.use(MdMenu)
Vue.prototype.moment = moment;

Vue.use(VueRouter)

const router = new VueRouter({
  routes
})

Vue.config.errorHandler = (err) => {
  if (process.env.NODE_ENV !== 'production') {
    // Show any error but this one
    if (err.message !== "Cannot read property 'badInput' of undefined") {
      console.error(err);
    }
  }
};



new Vue({
  render: h => h(App),
  router,
}).$mount('#app')
