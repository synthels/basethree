import { createApp } from "vue";
import { createWebHistory, createRouter } from "vue-router";

import "./style.css";
import App from "./App.vue";

import Home from "./Home.vue";
import Auth from "./Auth.vue";
import Signup from "./Signup.vue";
import PageNotFound from "./PageNotFound.vue";

const routes = [
  { path: "/", component: Home },
  { path: "/auth", component: Auth },
  { path: "/signup", component: Signup },
  { path: "/:pathMatch(.*)*", component: PageNotFound },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

createApp(App).use(router).mount("#app");
