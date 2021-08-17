import Vue from 'vue'
import App from './App.vue'
import MenuIcon from 'vue-material-design-icons/Menu.vue';
import VueMdijs from 'vue-mdijs'
// import { mdiMagnify } from '@mdi/js'
import { mdiArrowRightBoldCircleOutline } from '@mdi/js';
import { MdButton, MdContent, MdTabs, MdIcon, MdToolbar, MdDrawer, MdList, MdCard, MdField } from 'vue-material/dist/components'
import 'vue-material/dist/vue-material.min.css'
import 'vue-material/dist/theme/default.css'


Vue.config.productionTip = false
Vue.component('menu-icon', MenuIcon);
VueMdijs.add({ mdiArrowRightBoldCircleOutline })
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


new Vue({
  render: h => h(App),
}).$mount('#app')
