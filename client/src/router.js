import Vue from 'vue'
import Router from 'vue-router'
// import About from './views/About.vue'
import Home from './views/Home.vue'
import Profile from './views/Profile.vue';
import authGuard from './auth/authGuard';

Vue.use(Router)

const DEFAULT_TITLE = 'NDI-TAP WebApp';

const router = new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
      meta: { title: 'NDI-TAP WebApp' },
    },
    {
      path: '/profile',
      name: 'profile',
      component: Profile,
      meta: { title: 'MyInfo' },
      beforeEnter: authGuard,
    },
    // {
    //   path: '/about',
    //   name: 'about',
    //   component: About
    //   // // route level code-splitting
    //   // // this generates a separate chunk (about.[hash].js) for this route
    //   // // which is lazy-loaded when the route is visited.
    //   // component: () => import(/* webpackChunkName: "about" */ './views/About.vue')
    // }
  ]
});

router.afterEach((to) => {
  Vue.nextTick(() => {
    document.title = to.meta.title || DEFAULT_TITLE;
  });
});

export default router;
