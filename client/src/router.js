import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Login from './views/Login.vue'
import TravelAlerts from './views/TravelAlerts.vue'
import OidcCallback from './views/OidcCallback.vue'
import OidcCallbackError from './views/OidcCallbackError.vue'
import { vuexOidcCreateRouterMiddleware } from 'vuex-oidc'
import store from '@/store'

Vue.use(Router)

const DEFAULT_TITLE = 'NDI-TAP WebApp'

const router = new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
      meta: {
        isPublic: true
      }
    },
    {
      path: '/travelalerts',
      name: 'travelalerts',
      component: TravelAlerts,
      meta: {
        isPublic: true,
        title: 'Travel Alerts'
      }
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/oidc-callback', // Needs to match redirectUri in oidcSettings
      name: 'oidcCallback',
      component: OidcCallback
    },
    {
      path: '/oidc-callback-error', // Needs to match redirect_uri in oidcSettings
      name: 'oidcCallbackError',
      component: OidcCallbackError,
      meta: {
        isPublic: true
      }
    }
  ]
})

router.beforeEach(vuexOidcCreateRouterMiddleware(store, 'oidcStore'))

router.afterEach((to) => {
  Vue.nextTick(() => {
    document.title = to.meta.title || DEFAULT_TITLE
  })
})

export default router
