import Vue from 'vue'
import App from './App.vue'
import MenuIcon from 'vue-material-design-icons/Menu.vue';
import VueMdijs from 'vue-mdijs'
// import { mdiMagnify } from '@mdi/js'
import { mdiArrowRightBoldCircleOutline } from '@mdi/js';

Vue.config.productionTip = false
Vue.component('menu-icon', MenuIcon);
VueMdijs.add({ mdiArrowRightBoldCircleOutline })
Vue.use(VueMdijs)
// Vue.component(mdiArrowRightBoldCircleOutline)

new Vue({
  render: h => h(App),
}).$mount('#app')
