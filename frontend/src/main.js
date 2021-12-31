import Vue from 'vue'
import App from './App.vue'
import MenuIcon from 'vue-material-design-icons/Menu.vue';
import VueMdijs from 'vue-mdijs'
import {  mdiPlusThick, mdiMinusThick, mdiSend, mdiChevronLeft, mdiChevronRight, mdiPlusBox, mdiMinusBox, mdiChevronLeftCircle, mdiChevronRightCircle, mdiCamera } from '@mdi/js';
import { MdButton, MdContent, MdTabs, MdIcon, MdToolbar, MdDrawer, MdList, MdCard, MdField, MdMenu  } from 'vue-material/dist/components'
import 'vue-material/dist/vue-material.min.css'
import 'vue-material/dist/theme/default.css'
import VueRouter from 'vue-router'
import { routes } from './router/index.js'
import moment from 'moment';
import vuetify from './plugins/vuetify';
import VueI18n from 'vue-i18n'
import {pl} from '@/language/pl.ts';

Vue.config.productionTip = false
Vue.component('menu-icon', MenuIcon);
VueMdijs.add({ mdiPlusThick, mdiMinusThick, mdiSend, mdiChevronLeft, mdiChevronRight, mdiPlusBox, mdiMinusBox, mdiChevronLeftCircle, mdiChevronRightCircle, mdiCamera })
Vue.use(VueMdijs)
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
Vue.use(VueI18n)
Vue.prototype.moment = moment;

Vue.use(VueRouter)


const router = new VueRouter({
  routes
})

export const i18n = new VueI18n({
  locale: 'pl',
  fallbackLocale: 'pl',
  messages: {en: {hello: 'Hello'}, pl: pl}
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
  vuetify,
  render: h => h(App),
  i18n,
  router,
}).$mount('#app')
