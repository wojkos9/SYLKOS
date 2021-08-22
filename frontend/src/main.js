import Vue from 'vue'
import App from './App.vue'
import VueMdijs from 'vue-mdijs'
import { mdiPlusThick } from '@mdi/js';
import { mdiMinusThick } from '@mdi/js';
import { mdiSend } from '@mdi/js';
import { mdiChevronLeft } from '@mdi/js';  
import { mdiChevronRight } from '@mdi/js'; 
import { MdIcon, MdList } from 'vue-material/dist/components'; 
import 'vue-material/dist/vue-material.min.css';
import 'vue-material/dist/theme/default.css';
import moment from 'moment';

Vue.config.productionTip = false
VueMdijs.add({ mdiPlusThick, mdiMinusThick, mdiSend, mdiChevronLeft, mdiChevronRight })
Vue.use(MdIcon)
Vue.use(MdList)
Vue.use(VueMdijs)
Vue.prototype.moment = moment;

new Vue({
  render: h => h(App),
}).$mount('#app')
