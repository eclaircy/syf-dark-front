import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

/* Layout */
import Layout from '@/layout'

/* Router Modules */
import componentsRouter from './modules/components'


/**
 * Note: sub-menu only appear when route children.length >= 1
 * Detail see: https://panjiachen.github.io/vue-element-admin-site/guide/essentials/router-and-nav.html
 *
 * hidden: true                   if set true, item will not show in the sidebar(default is false)
 * alwaysShow: true               if set true, will always show the root menu
 *                                if not set alwaysShow, when item has more than one children route,
 *                                it will becomes nested mode, otherwise not show the root menu
 * redirect: noRedirect           if set noRedirect will no redirect in the breadcrumb
 * name:'router-name'             the name is used by <keep-alive> (must set!!!)
 * meta : {
    roles: ['admin','editor']    control the page roles (you can set multiple roles)
    title: 'title'               the name show in sidebar and breadcrumb (recommend set)
    icon: 'svg-name'/'el-icon-x' the icon show in the sidebar
    noCache: true                if set true, the page will no be cached(default is false)
    affix: true                  if set true, the tag will affix in the tags-view
    breadcrumb: false            if set false, the item will hidden in breadcrumb(default is true)
    activeMenu: '/example/list'  if set path, the sidebar will highlight the path you set
  }
 */

/**
 * constantRoutes
 * a base page that does not have permission requirements
 * all roles can be accessed
 */
export const constantRoutes = [
  {
    path: '/redirect',
    component: Layout,
    hidden: true,
    children: [
      {
        path: '/redirect/:path(.*)',
        component: () => import('@/views/redirect/index')
      }
    ]
  },
  {
    path: '/login',
    component: () => import('@/views/login/index'),
    hidden: true
  },
  
  
    // ////////////////////////////////////////////////////////////////////////////////////
      // ////////////////////////////////////////////////////////////////////////////////////
        // ////////////////////////////////////////////////////////////////////////////////////
          // ////////////////////////////////////////////////////////////////////////////////////
            // ////////////////////////////////////////////////////////////////////////////////////
  {
    path: '/',
    component: Layout,
    redirect: '/dashboard',
    meta: {
      title: '网站分析系统', //网站分析
      icon: 'el-icon-s-help'
    },
    children: [
      {
        path: 'dashboard',
        component: () => import('@/views/mydashboard/index'),
        name: 'Dashboard',
        meta: { title: '网站情报总览', icon: 'dashboard', affix: true }
      },
      {
        path: '/sites/detail',
        component: () => import('@/views/malwaresites/detail/index'),
        name: 'detail',
        meta: { title: '详情页', icon: 'documentation', affix: true },
        hidden: true
      },
      {
        path: '/sites/search',
        component: () => import('@/views/malwaresites/search/index'),
        name: 'search',
        meta: { title: '网站画像', icon: 'documentation', affix: true },
      },
    ]
  },
  {
    path: '/regulate',
    component: Layout,
    name:'regulate',
    // hidden:true,
    meta: {
      title: '实时审查系统',
      icon: 'el-icon-share'
    },
    children: [
      {
        path: 'detect',
        component: () => import('@/views/malwaresites/detect/index'),
        name: 'detect',
        meta: { title: '实时检测', icon: 'el-icon-search', affix: true },
      },
      {
        path: 'task',
        component: () => import('@/views/spider/ComplexTable'),
        name: 'task-manage',
        meta: { title: '检测任务配置', icon: 'el-icon-search', affix: true }
      },

    ]
  },
  {
    path: '/trace',
    component: Layout,
    name: 'trace',
    // redirect: '/overview',
    meta: {
      title: '追踪溯源系统',//溯源与团伙挖掘
      icon: 'el-icon-view'
    },
    alwaysShow: true,
    children: [
      {
        path: 'similar',
        component: () => import('@/views/malware-group/similar/index'),
        name: 'similar',
        meta: { title: '同源性分析', icon: 'el-icon-map-location', affix: true },
      },
      {
        path: 'person',
        component: () => import('@/views/person/index'),
        name: 'person',
        meta: { title: '人员追踪', icon: 'el-icon-aim', affix: true },
      },
      {
        path: 'person/detail',
        component: () => import('@/views/person/detail/index'),
        name: 'person-detail',
        meta: { title: '人员画像', icon: 'documentation', affix: true },
        hidden: true
      },
      {
        path: 'overview',
        component: () => import('@/views/malware-group/overview/index'),
        name: 'overview',
        meta: { title: '团伙挖掘', icon: 'dashboard', affix: true },
        // children: [
        //   {
        //     path: 'analyse',
        //     component: () => import('@/views/malware-group/analyse/index'),
        //     name: 'analyse',
        //     meta: { title: '团伙详情', icon: 'documentation', affix: true },
        //     hidden:true,
        //   }
        // ]
      },
      {
        path: 'analyse',
        component: () => import('@/views/malware-group/analyse/index'),
        name: 'analyse',
        meta: { title: '团伙详情', icon: 'documentation', affix: true },
        hidden:true,
      },
    ]
  },

  {
    path: '/area',
    component: Layout,
    // redirect: '/manage',
    children: [
      {
        path: 'manage',
        component: () => import('@/views/area-manage/index'),
        name: 'area-manage',
        meta: { title: '区域监管', icon: 'el-icon-s-help', affix: true }
      }
    ],
    hidden:true,
  },
  {
    path: '/robot',
    component: Layout,
    children: [
      {
        path: 'index',
        component: () => import('@/views/robot/index'),
        name: 'robot-answer',
        meta: { title: '智能问答系统', icon: 'el-icon-chat-dot-round', affix: true }
      }
    ]
  },

  {
    path: '/manage',
    component: Layout,
    meta: {
      title: '系统管理',
      icon: 'el-icon-s-tools'
    },
    children: [
      // {
      //   path: 'spider',
      //   component: () => import('@/views/spider/system-spider/index'),
      //   name: 'system-spider',
      //   meta: { title: '系统爬虫', icon: 'bug', affix: true }
      // },
      {
        path: 'user',
        component: () => import('@/views/user-manage/index'),
        name: 'user-manage',
        meta: { title: '用户管理', icon: 'el-icon-s-tools', affix: true }
      },
      {
        path: 'plugin',
        component: () => import('@/views/plugin-manage/index'),
        name: 'plugin-manage',
        meta: { title: '系统插件', icon: 'el-icon-s-promotion', affix: true }
      },
    ]
  },
  // {
  //   path: '/complaint',
  //   component: Layout,
  //   name:"complaint",
  //   children: [
  //     {
  //       path: 'index',
  //       component: () => import('@/views/malware-complaint/index'),
  //       name: 'user-complaint',
  //       meta: { title: '用户举报', icon: 'documentation', affix: true }
  //     }
  //   ]
  // },
  // ////////////////////////////////////////////////////////////////////////////////////
        // ////////////////////////////////////////////////////////////////////////////////////
        // ////////////////////////////////////////////////////////////////////////////////////
          // ////////////////////////////////////////////////////////////////////////////////////
            // ////////////////////////////////////////////////////////////////////////////////////
  
]

/**
 * asyncRoutes
 * the routes that need to be dynamically loaded based on user roles
 */
export const asyncRoutes = [
  
  
  /** when your routing map is too long, you can split it into small modules **/
  componentsRouter,

  // 404 page must be placed at the end !!!
  { path: '*', redirect: '/404', hidden: true }
]

const createRouter = () => new Router({
  // mode: 'history', // require service support
  scrollBehavior: () => ({ y: 0 }),
  routes: constantRoutes
})

const router = createRouter()

// Detail see: https://github.com/vuejs/vue-router/issues/1234#issuecomment-357941465
export function resetRouter() {
  const newRouter = createRouter()
  router.matcher = newRouter.matcher // reset router
}

export default router
