import Vue from 'vue'

import Cookies from 'js-cookie'

import 'normalize.css/normalize.css' // a modern alternative to CSS resets
import Element from 'element-ui'
import './styles/element-variables.scss'
import enLang from 'element-ui/lib/locale/lang/en'// 如果使用中文语言包请默认支持，无需额外引入，请删除该依赖
import '@/styles/index.scss' // global css

import App from './App'
import store from './store'
import router from './router'
import './icons' // icon
import './permission' // permission control
import './utils/error-log' // error log
import * as filters from './filters' // global filters

import 'element-theme-dark';


import 'ant-design-vue/dist/antd.css';
import { Button, Timeline,List,Avatar,Table,Collapse,Badge,Input,Tag } from "ant-design-vue";
Vue.use(Button).use(Timeline).use(List).use(Avatar).use(Table).use(Collapse).use(Badge).use(Input).use(Tag);


import VueParticles from 'vue-particles'  
Vue.use(VueParticles)  



// 将自动注册所有组件为全局组件
import dataV from '@jiaminghi/data-view'
Vue.use(dataV)



// var cors = require('cors');
// Vue.use(cors({
//     origin:['http://localhost:8888','https://06f6e7ea-4025-4c64-8f97-1d340bdc1dae.mock.pstmn.io'],  // 要设置白名单的 地址
//     methods:['GET','POST'],  // 请求方式
//     alloweHeaders:['Conten-Type', 'Authorization']
// }));


// 引入axios
import axios from 'axios';
// 挂载到vue原型链上
Vue.prototype.axios = axios;
//配置axios请求base url
// axios.defaults.baseURL='https://06f6e7ea-4025-4c64-8f97-1d340bdc1dae.mock.pstmn.io';
// axios.defaults.baseURL='http://localhost:8888';


/**
 * If you don't want to use mock-server
 * you want to use MockJs for mock api
 * you can execute: mockXHR()
 *
 * Currently MockJs will be used in the production environment,
 * please remove it before going online ! ! !
 */
if (process.env.NODE_ENV === 'production') {
  const { mockXHR } = require('../mock')
  mockXHR()
}

Vue.use(Element, {
  size: Cookies.get('size') || 'medium', // set element-ui default size
  locale: enLang // 如果使用中文，无需设置，请删除
})

// register global utility filters
Object.keys(filters).forEach(key => {
  Vue.filter(key, filters[key])
})

Vue.config.productionTip = false

new Vue({
  el: '#app',
  router,
  store,
  render: h => h(App)
})
